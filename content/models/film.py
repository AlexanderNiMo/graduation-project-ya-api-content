# coding: utf-8

"""
    Read-only API для онлайн-кинотеатра

    Информация о фильмах, жанрах и людях, участвовавших в создании произведения  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Film(object):
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
        'uuid': 'str',
        'title': 'str',
        'imdb_rating': 'float'
    }

    attribute_map = {
        'uuid': 'uuid',
        'title': 'title',
        'imdb_rating': 'imdb_rating'
    }

    def __init__(self, uuid=None, title=None, imdb_rating=None):  # noqa: E501
        """Film - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._title = None
        self._imdb_rating = None
        self.discriminator = None
        self.uuid = uuid
        self.title = title
        self.imdb_rating = imdb_rating

    @property
    def uuid(self):
        """Gets the uuid of this Film.  # noqa: E501


        :return: The uuid of this Film.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Film.


        :param uuid: The uuid of this Film.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def title(self):
        """Gets the title of this Film.  # noqa: E501


        :return: The title of this Film.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Film.


        :param title: The title of this Film.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def imdb_rating(self):
        """Gets the imdb_rating of this Film.  # noqa: E501


        :return: The imdb_rating of this Film.  # noqa: E501
        :rtype: float
        """
        return self._imdb_rating

    @imdb_rating.setter
    def imdb_rating(self, imdb_rating):
        """Sets the imdb_rating of this Film.


        :param imdb_rating: The imdb_rating of this Film.  # noqa: E501
        :type: float
        """
        if imdb_rating is None:
            raise ValueError("Invalid value for `imdb_rating`, must not be `None`")  # noqa: E501

        self._imdb_rating = imdb_rating

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
        if issubclass(Film, dict):
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
        if not isinstance(other, Film):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
