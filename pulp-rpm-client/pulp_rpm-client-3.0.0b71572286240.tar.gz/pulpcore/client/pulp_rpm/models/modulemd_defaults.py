# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class ModulemdDefaults(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'artifact': 'str',
        'relative_path': 'str',
        'file': 'str',
        'repository': 'str',
        'module': 'str',
        'stream': 'str',
        'profiles': 'object'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'file': 'file',
        'repository': 'repository',
        'module': 'module',
        'stream': 'stream',
        'profiles': 'profiles'
    }

    def __init__(self, pulp_href=None, pulp_created=None, artifact=None, relative_path=None, file=None, repository=None, module=None, stream=None, profiles=None, local_vars_configuration=None):  # noqa: E501
        """ModulemdDefaults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._artifact = None
        self._relative_path = None
        self._file = None
        self._repository = None
        self._module = None
        self._stream = None
        self._profiles = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if artifact is not None:
            self.artifact = artifact
        self.relative_path = relative_path
        if file is not None:
            self.file = file
        if repository is not None:
            self.repository = repository
        self.module = module
        self.stream = stream
        self.profiles = profiles

    @property
    def pulp_href(self):
        """Gets the pulp_href of this ModulemdDefaults.  # noqa: E501


        :return: The pulp_href of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this ModulemdDefaults.


        :param pulp_href: The pulp_href of this ModulemdDefaults.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this ModulemdDefaults.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this ModulemdDefaults.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this ModulemdDefaults.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this ModulemdDefaults.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def artifact(self):
        """Gets the artifact of this ModulemdDefaults.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this ModulemdDefaults.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this ModulemdDefaults.  # noqa: E501
        :type: str
        """

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this ModulemdDefaults.  # noqa: E501

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :return: The relative_path of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this ModulemdDefaults.

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :param relative_path: The relative_path of this ModulemdDefaults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_path is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_path is not None and len(relative_path) < 1):
            raise ValueError("Invalid value for `relative_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def file(self):
        """Gets the file of this ModulemdDefaults.  # noqa: E501

        An uploaded file that should be turned into the artifact of the content unit.  # noqa: E501

        :return: The file of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ModulemdDefaults.

        An uploaded file that should be turned into the artifact of the content unit.  # noqa: E501

        :param file: The file of this ModulemdDefaults.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def repository(self):
        """Gets the repository of this ModulemdDefaults.  # noqa: E501

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :return: The repository of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ModulemdDefaults.

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :param repository: The repository of this ModulemdDefaults.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def module(self):
        """Gets the module of this ModulemdDefaults.  # noqa: E501

        Modulemd name.  # noqa: E501

        :return: The module of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this ModulemdDefaults.

        Modulemd name.  # noqa: E501

        :param module: The module of this ModulemdDefaults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and module is None:  # noqa: E501
            raise ValueError("Invalid value for `module`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                module is not None and len(module) < 1):
            raise ValueError("Invalid value for `module`, length must be greater than or equal to `1`")  # noqa: E501

        self._module = module

    @property
    def stream(self):
        """Gets the stream of this ModulemdDefaults.  # noqa: E501

        Modulemd default stream.  # noqa: E501

        :return: The stream of this ModulemdDefaults.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ModulemdDefaults.

        Modulemd default stream.  # noqa: E501

        :param stream: The stream of this ModulemdDefaults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and stream is None:  # noqa: E501
            raise ValueError("Invalid value for `stream`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                stream is not None and len(stream) < 1):
            raise ValueError("Invalid value for `stream`, length must be greater than or equal to `1`")  # noqa: E501

        self._stream = stream

    @property
    def profiles(self):
        """Gets the profiles of this ModulemdDefaults.  # noqa: E501

        Default profiles for modulemd streams.  # noqa: E501

        :return: The profiles of this ModulemdDefaults.  # noqa: E501
        :rtype: object
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this ModulemdDefaults.

        Default profiles for modulemd streams.  # noqa: E501

        :param profiles: The profiles of this ModulemdDefaults.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and profiles is None:  # noqa: E501
            raise ValueError("Invalid value for `profiles`, must not be `None`")  # noqa: E501

        self._profiles = profiles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModulemdDefaults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModulemdDefaults):
            return True

        return self.to_dict() != other.to_dict()
