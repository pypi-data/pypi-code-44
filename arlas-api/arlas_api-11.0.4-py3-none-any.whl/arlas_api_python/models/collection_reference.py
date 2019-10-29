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


class CollectionReference(object):
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
        'collection_name': 'str',
        'params': 'CollectionReferenceParameters'
    }

    attribute_map = {
        'collection_name': 'collection_name',
        'params': 'params'
    }

    def __init__(self, collection_name=None, params=None):
        """
        CollectionReference - a model defined in Swagger
        """

        self._collection_name = None
        self._params = None

        self.collection_name = collection_name
        self.params = params

    @property
    def collection_name(self):
        """
        Gets the collection_name of this CollectionReference.

        :return: The collection_name of this CollectionReference.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        """
        Sets the collection_name of this CollectionReference.

        :param collection_name: The collection_name of this CollectionReference.
        :type: str
        """
        if collection_name is None:
            raise ValueError("Invalid value for `collection_name`, must not be `None`")

        self._collection_name = collection_name

    @property
    def params(self):
        """
        Gets the params of this CollectionReference.

        :return: The params of this CollectionReference.
        :rtype: CollectionReferenceParameters
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this CollectionReference.

        :param params: The params of this CollectionReference.
        :type: CollectionReferenceParameters
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")

        self._params = params

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
        if not isinstance(other, CollectionReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
