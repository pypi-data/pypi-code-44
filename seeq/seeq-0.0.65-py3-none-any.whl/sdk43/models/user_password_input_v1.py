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


class UserPasswordInputV1(object):
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
        'current_password': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'current_password': 'currentPassword',
        'new_password': 'newPassword'
    }

    def __init__(self, current_password=None, new_password=None):
        """
        UserPasswordInputV1 - a model defined in Swagger
        """

        self._current_password = None
        self._new_password = None

        if current_password is not None:
          self.current_password = current_password
        if new_password is not None:
          self.new_password = new_password

    @property
    def current_password(self):
        """
        Gets the current_password of this UserPasswordInputV1.
        The current password of this user

        :return: The current_password of this UserPasswordInputV1.
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """
        Sets the current_password of this UserPasswordInputV1.
        The current password of this user

        :param current_password: The current_password of this UserPasswordInputV1.
        :type: str
        """

        self._current_password = current_password

    @property
    def new_password(self):
        """
        Gets the new_password of this UserPasswordInputV1.
        The new password of this user

        :return: The new_password of this UserPasswordInputV1.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """
        Sets the new_password of this UserPasswordInputV1.
        The new password of this user

        :param new_password: The new_password of this UserPasswordInputV1.
        :type: str
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")

        self._new_password = new_password

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
        if not isinstance(other, UserPasswordInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
