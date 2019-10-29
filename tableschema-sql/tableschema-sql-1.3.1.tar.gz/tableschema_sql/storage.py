# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import collections
from functools import partial

import re
import six
import sqlalchemy
import tableschema
from sqlalchemy import Table, MetaData

from .mapper import Mapper
from .writer import Writer


# Module API

class Storage(tableschema.Storage):

    # Public

    def __init__(self, engine, dbschema=None, prefix='', reflect_only=None, autoincrement=None):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Set attributes
        self.__connection = engine.connect()
        self.__dbschema = dbschema
        self.__prefix = prefix
        self.__descriptors = {}
        self.__fallbacks = {}
        self.__autoincrement = autoincrement
        self.__only = reflect_only or (lambda _: True)
        self.__dialect = engine.dialect.name

        # Added regex support to sqlite
        if self.__dialect == 'sqlite':
            def regexp(expr, item):
                reg = re.compile(expr)
                return reg.search(item) is not None
            # It will fail silently if this function already exists
            self.__connection.connection.create_function('REGEXP', 2, regexp)

        # Create mapper
        self.__mapper = Mapper(prefix=prefix, dialect=self.__dialect)

        # Create metadata and reflect
        self.__metadata = MetaData(bind=self.__connection, schema=self.__dbschema)
        self.__reflect()

    def __repr__(self):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Template and format
        template = 'Storage <{engine}/{dbschema}>'
        text = template.format(
            engine=self.__connection.engine,
            dbschema=self.__dbschema)

        return text

    @property
    def buckets(self):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """
        buckets = []
        for table in self.__metadata.sorted_tables:
            bucket = self.__mapper.restore_bucket(table.name)
            if bucket is not None:
                buckets.append(bucket)
        return buckets

    def create(self, bucket, descriptor, force=False, indexes_fields=None):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Make lists
        buckets = bucket
        if isinstance(bucket, six.string_types):
            buckets = [bucket]
        descriptors = descriptor
        if isinstance(descriptor, dict):
            descriptors = [descriptor]
        if indexes_fields is None or len(indexes_fields) == 0:
            indexes_fields = [()] * len(descriptors)
        elif type(indexes_fields[0][0]) not in {list, tuple}:
            indexes_fields = [indexes_fields]

        # Check dimensions
        if not (len(buckets) == len(descriptors) == len(indexes_fields)):
            raise tableschema.exceptions.StorageError('Wrong argument dimensions')

        # Check buckets for existence
        for bucket in reversed(self.buckets):
            if bucket in buckets:
                if not force:
                    message = 'Bucket "%s" already exists.' % bucket
                    raise tableschema.exceptions.StorageError(message)
                self.delete(bucket)

        # Define buckets
        for bucket, descriptor, index_fields in zip(buckets, descriptors, indexes_fields):
            tableschema.validate(descriptor)
            table_name = self.__mapper.convert_bucket(bucket)
            autoincrement = self.__get_autoincrement_for_bucket(bucket)
            columns, constraints, indexes, fallbacks, table_comment = self.__mapper \
                .convert_descriptor(bucket, descriptor, index_fields, autoincrement)
            Table(table_name, self.__metadata, *(columns + constraints + indexes),
                  comment=table_comment)
            self.__descriptors[bucket] = descriptor
            self.__fallbacks[bucket] = fallbacks

        # Create tables, update metadata
        try:
            self.__metadata.create_all()
        except sqlalchemy.exc.ProgrammingError as exception:
            if 'there is no unique constraint matching given keys' in str(exception):
                message = 'Foreign keys can only reference primary key or unique fields\n%s'
                six.raise_from(
                    tableschema.exceptions.ValidationError(message % str(exception)),
                    None)

    def delete(self, bucket=None, ignore=False):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Make lists
        buckets = bucket
        if isinstance(bucket, six.string_types):
            buckets = [bucket]
        elif bucket is None:
            buckets = reversed(self.buckets)

        # Iterate
        tables = []
        for bucket in buckets:

            # Check existent
            if bucket not in self.buckets:
                if not ignore:
                    message = 'Bucket "%s" doesn\'t exist.' % bucket
                    raise tableschema.exceptions.StorageError(message)
                return

            # Remove from buckets
            if bucket in self.__descriptors:
                del self.__descriptors[bucket]

            # Add table to tables
            table = self.__get_table(bucket)
            tables.append(table)

        # Drop tables, update metadata
        self.__metadata.drop_all(tables=tables)
        self.__metadata.clear()
        self.__reflect()

    def describe(self, bucket, descriptor=None):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Set descriptor
        if descriptor is not None:
            self.__descriptors[bucket] = descriptor

        # Get descriptor
        else:
            descriptor = self.__descriptors.get(bucket)
            if descriptor is None:
                table = self.__get_table(bucket)
                autoincrement = self.__get_autoincrement_for_bucket(bucket)
                descriptor = self.__mapper.restore_descriptor(
                    table.name, table.columns, table.constraints, autoincrement)

        return descriptor

    def iter(self, bucket):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Get table and fallbacks
        table = self.__get_table(bucket)
        schema = tableschema.Schema(self.describe(bucket))
        autoincrement = self.__get_autoincrement_for_bucket(bucket)

        # Open and close transaction
        with self.__connection.begin():
            # Streaming could be not working for some backends:
            # http://docs.sqlalchemy.org/en/latest/core/connections.html
            select = table.select().execution_options(stream_results=True)
            result = select.execute()
            for row in result:
                row = self.__mapper.restore_row(
                    row, schema=schema, autoincrement=autoincrement)
                yield row

    def read(self, bucket):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """
        rows = list(self.iter(bucket))
        return rows

    def write(self, bucket, rows, keyed=False, as_generator=False, update_keys=None,
              buffer_size=1000, use_bloom_filter=True):
        """https://github.com/frictionlessdata/tableschema-sql-py#storage
        """

        # Check update keys
        if update_keys is not None and len(update_keys) == 0:
            message = 'Argument "update_keys" cannot be an empty list'
            raise tableschema.exceptions.StorageError(message)

        # Get table and description
        table = self.__get_table(bucket)
        schema = tableschema.Schema(self.describe(bucket))
        fallbacks = self.__fallbacks.get(bucket, [])

        # Write rows to table
        convert_row = partial(self.__mapper.convert_row, schema=schema, fallbacks=fallbacks)
        autoincrement = self.__get_autoincrement_for_bucket(bucket)
        writer = Writer(table, schema,
            # Only PostgreSQL supports "returning" so we don't use autoincrement for all
            autoincrement=autoincrement if self.__dialect in ['postgresql'] else None,
            update_keys=update_keys,
            convert_row=convert_row,
            buffer_size=buffer_size,
            use_bloom_filter=use_bloom_filter)
        with self.__connection.begin():
            gen = writer.write(rows, keyed=keyed)
            if as_generator:
                return gen
            collections.deque(gen, maxlen=0)

    # Private

    def __get_table(self, bucket):
        table_name = self.__mapper.convert_bucket(bucket)
        if self.__dbschema:
            table_name = '.'.join((self.__dbschema, table_name))
        return self.__metadata.tables[table_name]

    def __reflect(self):
        def only(name, _):
            return self.__only(name) and self.__mapper.restore_bucket(name) is not None
        self.__metadata.reflect(only=only)

    def __get_autoincrement_for_bucket(self, bucket):
        if isinstance(self.__autoincrement, dict):
            return self.__autoincrement.get(bucket)
        return self.__autoincrement
