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


class RepoMetadataFile(object):
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
        'data_type': 'str',
        'checksum_type': 'str',
        'checksum': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'file': 'file',
        'repository': 'repository',
        'data_type': 'data_type',
        'checksum_type': 'checksum_type',
        'checksum': 'checksum'
    }

    def __init__(self, pulp_href=None, pulp_created=None, artifact=None, relative_path=None, file=None, repository=None, data_type=None, checksum_type=None, checksum=None, local_vars_configuration=None):  # noqa: E501
        """RepoMetadataFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._artifact = None
        self._relative_path = None
        self._file = None
        self._repository = None
        self._data_type = None
        self._checksum_type = None
        self._checksum = None
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
        self.data_type = data_type
        self.checksum_type = checksum_type
        self.checksum = checksum

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RepoMetadataFile.  # noqa: E501


        :return: The pulp_href of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RepoMetadataFile.


        :param pulp_href: The pulp_href of this RepoMetadataFile.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RepoMetadataFile.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RepoMetadataFile.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RepoMetadataFile.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RepoMetadataFile.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def artifact(self):
        """Gets the artifact of this RepoMetadataFile.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this RepoMetadataFile.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this RepoMetadataFile.  # noqa: E501
        :type: str
        """

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this RepoMetadataFile.  # noqa: E501

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :return: The relative_path of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this RepoMetadataFile.

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :param relative_path: The relative_path of this RepoMetadataFile.  # noqa: E501
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
        """Gets the file of this RepoMetadataFile.  # noqa: E501

        An uploaded file that should be turned into the artifact of the content unit.  # noqa: E501

        :return: The file of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this RepoMetadataFile.

        An uploaded file that should be turned into the artifact of the content unit.  # noqa: E501

        :param file: The file of this RepoMetadataFile.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def repository(self):
        """Gets the repository of this RepoMetadataFile.  # noqa: E501

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :return: The repository of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RepoMetadataFile.

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :param repository: The repository of this RepoMetadataFile.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def data_type(self):
        """Gets the data_type of this RepoMetadataFile.  # noqa: E501

        Metadata type.  # noqa: E501

        :return: The data_type of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this RepoMetadataFile.

        Metadata type.  # noqa: E501

        :param data_type: The data_type of this RepoMetadataFile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_type is not None and len(data_type) < 1):
            raise ValueError("Invalid value for `data_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._data_type = data_type

    @property
    def checksum_type(self):
        """Gets the checksum_type of this RepoMetadataFile.  # noqa: E501

        Checksum type for the file.  # noqa: E501

        :return: The checksum_type of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """Sets the checksum_type of this RepoMetadataFile.

        Checksum type for the file.  # noqa: E501

        :param checksum_type: The checksum_type of this RepoMetadataFile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and checksum_type is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                checksum_type is not None and len(checksum_type) < 1):
            raise ValueError("Invalid value for `checksum_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._checksum_type = checksum_type

    @property
    def checksum(self):
        """Gets the checksum of this RepoMetadataFile.  # noqa: E501

        Checksum for the file.  # noqa: E501

        :return: The checksum of this RepoMetadataFile.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this RepoMetadataFile.

        Checksum for the file.  # noqa: E501

        :param checksum: The checksum of this RepoMetadataFile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                checksum is not None and len(checksum) < 1):
            raise ValueError("Invalid value for `checksum`, length must be greater than or equal to `1`")  # noqa: E501

        self._checksum = checksum

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
        if not isinstance(other, RepoMetadataFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepoMetadataFile):
            return True

        return self.to_dict() != other.to_dict()
