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


class AggregationMetric(object):
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
        'type': 'str',
        'field': 'str',
        'value': 'object'
    }

    attribute_map = {
        'type': 'type',
        'field': 'field',
        'value': 'value'
    }

    def __init__(self, type=None, field=None, value=None):
        """
        AggregationMetric - a model defined in Swagger
        """

        self._type = None
        self._field = None
        self._value = None

        if type is not None:
          self.type = type
        if field is not None:
          self.field = field
        if value is not None:
          self.value = value

    @property
    def type(self):
        """
        Gets the type of this AggregationMetric.

        :return: The type of this AggregationMetric.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AggregationMetric.

        :param type: The type of this AggregationMetric.
        :type: str
        """

        self._type = type

    @property
    def field(self):
        """
        Gets the field of this AggregationMetric.

        :return: The field of this AggregationMetric.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this AggregationMetric.

        :param field: The field of this AggregationMetric.
        :type: str
        """

        self._field = field

    @property
    def value(self):
        """
        Gets the value of this AggregationMetric.

        :return: The value of this AggregationMetric.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AggregationMetric.

        :param value: The value of this AggregationMetric.
        :type: object
        """

        self._value = value

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
        if not isinstance(other, AggregationMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
