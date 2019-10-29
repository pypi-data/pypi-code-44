# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections

    OpenAPI spec version: 11.0.4
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DublinCoreElementName(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'creator': 'str',
        'subject': 'str',
        'description': 'str',
        'publisher': 'str',
        'contributor': 'str',
        'type': 'str',
        'format': 'str',
        'identifier': 'str',
        'source': 'str',
        'language': 'str',
        'bbox': 'Bbox',
        'date': 'str',
        'coverage': 'dict(str, object)',
        'coverage_centroid': 'str'
    }

    attribute_map = {
        'title': 'title',
        'creator': 'creator',
        'subject': 'subject',
        'description': 'description',
        'publisher': 'publisher',
        'contributor': 'contributor',
        'type': 'type',
        'format': 'format',
        'identifier': 'identifier',
        'source': 'source',
        'language': 'language',
        'bbox': 'bbox',
        'date': 'date',
        'coverage': 'coverage',
        'coverage_centroid': 'coverage_centroid'
    }

    def __init__(self, title=None, creator=None, subject=None, description=None, publisher=None, contributor=None, type=None, format=None, identifier=None, source=None, language=None, bbox=None, date=None, coverage=None, coverage_centroid=None):
        """
        DublinCoreElementName - a model defined in Swagger
        """

        self._title = None
        self._creator = None
        self._subject = None
        self._description = None
        self._publisher = None
        self._contributor = None
        self._type = None
        self._format = None
        self._identifier = None
        self._source = None
        self._language = None
        self._bbox = None
        self._date = None
        self._coverage = None
        self._coverage_centroid = None

        if title is not None:
          self.title = title
        if creator is not None:
          self.creator = creator
        if subject is not None:
          self.subject = subject
        if description is not None:
          self.description = description
        if publisher is not None:
          self.publisher = publisher
        if contributor is not None:
          self.contributor = contributor
        if type is not None:
          self.type = type
        if format is not None:
          self.format = format
        if identifier is not None:
          self.identifier = identifier
        if source is not None:
          self.source = source
        if language is not None:
          self.language = language
        if bbox is not None:
          self.bbox = bbox
        if date is not None:
          self.date = date
        if coverage is not None:
          self.coverage = coverage
        if coverage_centroid is not None:
          self.coverage_centroid = coverage_centroid

    @property
    def title(self):
        """
        Gets the title of this DublinCoreElementName.

        :return: The title of this DublinCoreElementName.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this DublinCoreElementName.

        :param title: The title of this DublinCoreElementName.
        :type: str
        """

        self._title = title

    @property
    def creator(self):
        """
        Gets the creator of this DublinCoreElementName.

        :return: The creator of this DublinCoreElementName.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this DublinCoreElementName.

        :param creator: The creator of this DublinCoreElementName.
        :type: str
        """

        self._creator = creator

    @property
    def subject(self):
        """
        Gets the subject of this DublinCoreElementName.

        :return: The subject of this DublinCoreElementName.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this DublinCoreElementName.

        :param subject: The subject of this DublinCoreElementName.
        :type: str
        """

        self._subject = subject

    @property
    def description(self):
        """
        Gets the description of this DublinCoreElementName.

        :return: The description of this DublinCoreElementName.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DublinCoreElementName.

        :param description: The description of this DublinCoreElementName.
        :type: str
        """

        self._description = description

    @property
    def publisher(self):
        """
        Gets the publisher of this DublinCoreElementName.

        :return: The publisher of this DublinCoreElementName.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this DublinCoreElementName.

        :param publisher: The publisher of this DublinCoreElementName.
        :type: str
        """

        self._publisher = publisher

    @property
    def contributor(self):
        """
        Gets the contributor of this DublinCoreElementName.

        :return: The contributor of this DublinCoreElementName.
        :rtype: str
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """
        Sets the contributor of this DublinCoreElementName.

        :param contributor: The contributor of this DublinCoreElementName.
        :type: str
        """

        self._contributor = contributor

    @property
    def type(self):
        """
        Gets the type of this DublinCoreElementName.

        :return: The type of this DublinCoreElementName.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DublinCoreElementName.

        :param type: The type of this DublinCoreElementName.
        :type: str
        """

        self._type = type

    @property
    def format(self):
        """
        Gets the format of this DublinCoreElementName.

        :return: The format of this DublinCoreElementName.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this DublinCoreElementName.

        :param format: The format of this DublinCoreElementName.
        :type: str
        """

        self._format = format

    @property
    def identifier(self):
        """
        Gets the identifier of this DublinCoreElementName.

        :return: The identifier of this DublinCoreElementName.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DublinCoreElementName.

        :param identifier: The identifier of this DublinCoreElementName.
        :type: str
        """

        self._identifier = identifier

    @property
    def source(self):
        """
        Gets the source of this DublinCoreElementName.

        :return: The source of this DublinCoreElementName.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DublinCoreElementName.

        :param source: The source of this DublinCoreElementName.
        :type: str
        """

        self._source = source

    @property
    def language(self):
        """
        Gets the language of this DublinCoreElementName.

        :return: The language of this DublinCoreElementName.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this DublinCoreElementName.

        :param language: The language of this DublinCoreElementName.
        :type: str
        """

        self._language = language

    @property
    def bbox(self):
        """
        Gets the bbox of this DublinCoreElementName.

        :return: The bbox of this DublinCoreElementName.
        :rtype: Bbox
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """
        Sets the bbox of this DublinCoreElementName.

        :param bbox: The bbox of this DublinCoreElementName.
        :type: Bbox
        """

        self._bbox = bbox

    @property
    def date(self):
        """
        Gets the date of this DublinCoreElementName.

        :return: The date of this DublinCoreElementName.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this DublinCoreElementName.

        :param date: The date of this DublinCoreElementName.
        :type: str
        """

        self._date = date

    @property
    def coverage(self):
        """
        Gets the coverage of this DublinCoreElementName.

        :return: The coverage of this DublinCoreElementName.
        :rtype: dict(str, object)
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """
        Sets the coverage of this DublinCoreElementName.

        :param coverage: The coverage of this DublinCoreElementName.
        :type: dict(str, object)
        """

        self._coverage = coverage

    @property
    def coverage_centroid(self):
        """
        Gets the coverage_centroid of this DublinCoreElementName.

        :return: The coverage_centroid of this DublinCoreElementName.
        :rtype: str
        """
        return self._coverage_centroid

    @coverage_centroid.setter
    def coverage_centroid(self, coverage_centroid):
        """
        Sets the coverage_centroid of this DublinCoreElementName.

        :param coverage_centroid: The coverage_centroid of this DublinCoreElementName.
        :type: str
        """

        self._coverage_centroid = coverage_centroid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DublinCoreElementName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
