# coding: utf-8

"""
    SSPO Service

    The Scrum Software Process Ontology (SSPO) aims at establishing a common conceptualization on the Scrum domain, including roles, teams and projects.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AcceptanceCriteria_(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'uuid': 'str',
        'user_story': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'uuid': 'uuid',
        'user_story': 'user_story'
    }

    def __init__(self, id=None, name=None, description=None, uuid=None, user_story=None):  # noqa: E501
        """AcceptanceCriteria_ - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._uuid = None
        self._user_story = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if uuid is not None:
            self.uuid = uuid
        if user_story is not None:
            self.user_story = user_story

    @property
    def id(self):
        """Gets the id of this AcceptanceCriteria_.  # noqa: E501


        :return: The id of this AcceptanceCriteria_.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AcceptanceCriteria_.


        :param id: The id of this AcceptanceCriteria_.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AcceptanceCriteria_.  # noqa: E501


        :return: The name of this AcceptanceCriteria_.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AcceptanceCriteria_.


        :param name: The name of this AcceptanceCriteria_.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this AcceptanceCriteria_.  # noqa: E501


        :return: The description of this AcceptanceCriteria_.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AcceptanceCriteria_.


        :param description: The description of this AcceptanceCriteria_.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def uuid(self):
        """Gets the uuid of this AcceptanceCriteria_.  # noqa: E501


        :return: The uuid of this AcceptanceCriteria_.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this AcceptanceCriteria_.


        :param uuid: The uuid of this AcceptanceCriteria_.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def user_story(self):
        """Gets the user_story of this AcceptanceCriteria_.  # noqa: E501


        :return: The user_story of this AcceptanceCriteria_.  # noqa: E501
        :rtype: int
        """
        return self._user_story

    @user_story.setter
    def user_story(self, user_story):
        """Sets the user_story of this AcceptanceCriteria_.


        :param user_story: The user_story of this AcceptanceCriteria_.  # noqa: E501
        :type: int
        """

        self._user_story = user_story

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AcceptanceCriteria_, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AcceptanceCriteria_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
