# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.43.09-v201909272304
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PutSignalsInputV1(object):
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
        'signals': 'list[SignalWithIdInputV1]'
    }

    attribute_map = {
        'signals': 'signals'
    }

    def __init__(self, signals=None):
        """
        PutSignalsInputV1 - a model defined in Swagger
        """

        self._signals = None

        if signals is not None:
          self.signals = signals

    @property
    def signals(self):
        """
        Gets the signals of this PutSignalsInputV1.
        The signals to create or update

        :return: The signals of this PutSignalsInputV1.
        :rtype: list[SignalWithIdInputV1]
        """
        return self._signals

    @signals.setter
    def signals(self, signals):
        """
        Sets the signals of this PutSignalsInputV1.
        The signals to create or update

        :param signals: The signals of this PutSignalsInputV1.
        :type: list[SignalWithIdInputV1]
        """
        if signals is None:
            raise ValueError("Invalid value for `signals`, must not be `None`")

        self._signals = signals

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
        if not isinstance(other, PutSignalsInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
