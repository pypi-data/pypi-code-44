# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RelatedStories(object):
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
        'related_stories': 'list[Story]',
        'story_body': 'str',
        'story_language': 'str',
        'story_title': 'str'
    }

    attribute_map = {
        'related_stories': 'related_stories',
        'story_body': 'story_body',
        'story_language': 'story_language',
        'story_title': 'story_title'
    }

    def __init__(self, related_stories=None, story_body=None, story_language=None, story_title=None):  # noqa: E501
        """RelatedStories - a model defined in OpenAPI"""  # noqa: E501

        self._related_stories = None
        self._story_body = None
        self._story_language = None
        self._story_title = None
        self.discriminator = None

        if related_stories is not None:
            self.related_stories = related_stories
        if story_body is not None:
            self.story_body = story_body
        if story_language is not None:
            self.story_language = story_language
        if story_title is not None:
            self.story_title = story_title

    @property
    def related_stories(self):
        """Gets the related_stories of this RelatedStories.  # noqa: E501

        An array of related stories for the input story  # noqa: E501

        :return: The related_stories of this RelatedStories.  # noqa: E501
        :rtype: list[Story]
        """
        return self._related_stories

    @related_stories.setter
    def related_stories(self, related_stories):
        """Sets the related_stories of this RelatedStories.

        An array of related stories for the input story  # noqa: E501

        :param related_stories: The related_stories of this RelatedStories.  # noqa: E501
        :type: list[Story]
        """

        self._related_stories = related_stories

    @property
    def story_body(self):
        """Gets the story_body of this RelatedStories.  # noqa: E501

        The input story body  # noqa: E501

        :return: The story_body of this RelatedStories.  # noqa: E501
        :rtype: str
        """
        return self._story_body

    @story_body.setter
    def story_body(self, story_body):
        """Sets the story_body of this RelatedStories.

        The input story body  # noqa: E501

        :param story_body: The story_body of this RelatedStories.  # noqa: E501
        :type: str
        """

        self._story_body = story_body

    @property
    def story_language(self):
        """Gets the story_language of this RelatedStories.  # noqa: E501

        The input story language  # noqa: E501

        :return: The story_language of this RelatedStories.  # noqa: E501
        :rtype: str
        """
        return self._story_language

    @story_language.setter
    def story_language(self, story_language):
        """Sets the story_language of this RelatedStories.

        The input story language  # noqa: E501

        :param story_language: The story_language of this RelatedStories.  # noqa: E501
        :type: str
        """

        self._story_language = story_language

    @property
    def story_title(self):
        """Gets the story_title of this RelatedStories.  # noqa: E501

        The input story title  # noqa: E501

        :return: The story_title of this RelatedStories.  # noqa: E501
        :rtype: str
        """
        return self._story_title

    @story_title.setter
    def story_title(self, story_title):
        """Sets the story_title of this RelatedStories.

        The input story title  # noqa: E501

        :param story_title: The story_title of this RelatedStories.  # noqa: E501
        :type: str
        """

        self._story_title = story_title

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
        if not isinstance(other, RelatedStories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
