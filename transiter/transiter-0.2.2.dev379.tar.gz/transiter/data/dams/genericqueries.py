"""
This module provides some abstract methods to remove code duplication in the DAMs.
"""
from transiter.data import dbconnection
from transiter import models


def create(DbEntity: models.Base, entity=None):
    """
    Create a database entity.

    :param DbEntity: the entity's type
    :param entity: optionally an instance of this type that will instead be added
        to the session
    :return: the entity, which is in the session
    """
    session = dbconnection.get_session()
    if entity is None:
        entity = DbEntity()
    session.add(entity)
    return entity


def list_all(DbEntity: models.Base, order_by_field=None):
    """
    List all entities of a certain type.

    :param DbEntity: the entities' type
    :param order_by_field: field or order the results be
    :return: list of entities of type DbEntity
    """
    session = dbconnection.get_session()
    query = session.query(DbEntity)
    if order_by_field is not None:
        query = query.order_by(order_by_field)
    return query.all()


def get_by_id(DbEntity: models.Base, id_):
    """
    Get an entity by its ID.

    :param DbEntity: the entity's type
    :param id_: the entity's ID
    :return: the entity, if it exists in the DB, or None otherwise
    """
    session = dbconnection.get_session()
    return session.query(DbEntity).filter(DbEntity.id == id_).one_or_none()


def list_all_in_system(DbEntity: models.Base, system_id, order_by_field=None):
    """
    List all entities of a certain type that are in a given system. Note this method
    only works with entities that are direct children of the system.

    :param DbEntity: the entity's type
    :param system_id: the system's ID
    :param order_by_field: optional field to order the results by
    :return: list of entities of type DbEntity
    """
    session = dbconnection.get_session()
    query = session.query(DbEntity).filter(DbEntity.system_id == system_id)
    if order_by_field is not None:
        query = query.order_by(order_by_field)
    return query.all()


def get_in_system_by_id(DbEntity: models.Base, system_id, id_):
    """
    Get an entity of a certain type that is in a given system. Note this method
    only works with entities that are direct children of the system.

    :param DbEntity: the entity's type
    :param system_id: the system's ID
    :param id_: the entity's ID
    :return: list of entities of type DbEntity
    """
    session = dbconnection.get_session()
    return (
        session.query(DbEntity)
        .filter(DbEntity.system_id == system_id)
        .filter(DbEntity.id == id_)
        .one_or_none()
    )


def get_id_to_pk_map(DbEntity: models.Base, system_id=None, ids=None):
    """
    Get an map of entity ID to entity PK for all entities of a given type in a system.
    Note this method only works with entities that are direct children of the system.

    :param DbEntity: the entity's type
    :param system_id: the system's ID
    :param ids_: optional, the entity's IDs
    :return: map of ID to PK
    """
    if ids is not None:
        id_to_pk = {id_: None for id_ in ids}
    else:
        id_to_pk = {}
    session = dbconnection.get_session()
    query = session.query(DbEntity.id, DbEntity.pk)
    if system_id is not None:
        query = query.filter(DbEntity.system_id == system_id)
    if ids is not None:
        query = query.filter(DbEntity.id.in_(ids))
    for (id_, pk) in query.all():
        id_to_pk[id_] = pk
    return id_to_pk
