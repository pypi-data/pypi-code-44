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


class UpdateResponse(object):
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
        'failures': 'list[Failure]',
        'failed': 'int',
        'updated': 'int',
        'action': 'str'
    }

    attribute_map = {
        'failures': 'failures',
        'failed': 'failed',
        'updated': 'updated',
        'action': 'action'
    }

    def __init__(self, failures=None, failed=None, updated=None, action=None):
        """
        UpdateResponse - a model defined in Swagger
        """

        self._failures = None
        self._failed = None
        self._updated = None
        self._action = None

        if failures is not None:
          self.failures = failures
        if failed is not None:
          self.failed = failed
        if updated is not None:
          self.updated = updated
        if action is not None:
          self.action = action

    @property
    def failures(self):
        """
        Gets the failures of this UpdateResponse.

        :return: The failures of this UpdateResponse.
        :rtype: list[Failure]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """
        Sets the failures of this UpdateResponse.

        :param failures: The failures of this UpdateResponse.
        :type: list[Failure]
        """

        self._failures = failures

    @property
    def failed(self):
        """
        Gets the failed of this UpdateResponse.

        :return: The failed of this UpdateResponse.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this UpdateResponse.

        :param failed: The failed of this UpdateResponse.
        :type: int
        """

        self._failed = failed

    @property
    def updated(self):
        """
        Gets the updated of this UpdateResponse.

        :return: The updated of this UpdateResponse.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this UpdateResponse.

        :param updated: The updated of this UpdateResponse.
        :type: int
        """

        self._updated = updated

    @property
    def action(self):
        """
        Gets the action of this UpdateResponse.

        :return: The action of this UpdateResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UpdateResponse.

        :param action: The action of this UpdateResponse.
        :type: str
        """
        allowed_values = ["ADD", "REMOVE", "REMOVEALL"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

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
        if not isinstance(other, UpdateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
