# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.44.00-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SeriesOutputV1(object):
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
        'data_id': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'formula': 'str',
        'href': 'str',
        'id': 'str',
        'interpolation_method': 'str',
        'is_archived': 'bool',
        'key_unit_of_measure': 'str',
        'maximum_interpolation': 'str',
        'name': 'str',
        'parameters': 'list[FormulaParameterOutputV1]',
        'scoped_to': 'str',
        'status_message': 'str',
        'type': 'str',
        'value_unit_of_measure': 'str'
    }

    attribute_map = {
        'data_id': 'dataId',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'formula': 'formula',
        'href': 'href',
        'id': 'id',
        'interpolation_method': 'interpolationMethod',
        'is_archived': 'isArchived',
        'key_unit_of_measure': 'keyUnitOfMeasure',
        'maximum_interpolation': 'maximumInterpolation',
        'name': 'name',
        'parameters': 'parameters',
        'scoped_to': 'scopedTo',
        'status_message': 'statusMessage',
        'type': 'type',
        'value_unit_of_measure': 'valueUnitOfMeasure'
    }

    def __init__(self, data_id=None, datasource_class=None, datasource_id=None, description=None, formula=None, href=None, id=None, interpolation_method=None, is_archived=False, key_unit_of_measure=None, maximum_interpolation=None, name=None, parameters=None, scoped_to=None, status_message=None, type=None, value_unit_of_measure=None):
        """
        SeriesOutputV1 - a model defined in Swagger
        """

        self._data_id = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._formula = None
        self._href = None
        self._id = None
        self._interpolation_method = None
        self._is_archived = None
        self._key_unit_of_measure = None
        self._maximum_interpolation = None
        self._name = None
        self._parameters = None
        self._scoped_to = None
        self._status_message = None
        self._type = None
        self._value_unit_of_measure = None

        if data_id is not None:
          self.data_id = data_id
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if formula is not None:
          self.formula = formula
        if href is not None:
          self.href = href
        if id is not None:
          self.id = id
        if interpolation_method is not None:
          self.interpolation_method = interpolation_method
        if is_archived is not None:
          self.is_archived = is_archived
        if key_unit_of_measure is not None:
          self.key_unit_of_measure = key_unit_of_measure
        if maximum_interpolation is not None:
          self.maximum_interpolation = maximum_interpolation
        if name is not None:
          self.name = name
        if parameters is not None:
          self.parameters = parameters
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if status_message is not None:
          self.status_message = status_message
        if type is not None:
          self.type = type
        if value_unit_of_measure is not None:
          self.value_unit_of_measure = value_unit_of_measure

    @property
    def data_id(self):
        """
        Gets the data_id of this SeriesOutputV1.
        The data ID of this asset. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this SeriesOutputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this SeriesOutputV1.
        The data ID of this asset. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this SeriesOutputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this SeriesOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :return: The datasource_class of this SeriesOutputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this SeriesOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :param datasource_class: The datasource_class of this SeriesOutputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this SeriesOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :return: The datasource_id of this SeriesOutputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this SeriesOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :param datasource_id: The datasource_id of this SeriesOutputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this SeriesOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this SeriesOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SeriesOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this SeriesOutputV1.
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """
        Gets the formula of this SeriesOutputV1.
        The formula for the calculated item

        :return: The formula of this SeriesOutputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this SeriesOutputV1.
        The formula for the calculated item

        :param formula: The formula of this SeriesOutputV1.
        :type: str
        """

        self._formula = formula

    @property
    def href(self):
        """
        Gets the href of this SeriesOutputV1.
        The href that can be used to interact with the item

        :return: The href of this SeriesOutputV1.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this SeriesOutputV1.
        The href that can be used to interact with the item

        :param href: The href of this SeriesOutputV1.
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def id(self):
        """
        Gets the id of this SeriesOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this SeriesOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SeriesOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this SeriesOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def interpolation_method(self):
        """
        Gets the interpolation_method of this SeriesOutputV1.
        The interpolation method used when resampling the series. The options are: linear, pilinear, and step.

        :return: The interpolation_method of this SeriesOutputV1.
        :rtype: str
        """
        return self._interpolation_method

    @interpolation_method.setter
    def interpolation_method(self, interpolation_method):
        """
        Sets the interpolation_method of this SeriesOutputV1.
        The interpolation method used when resampling the series. The options are: linear, pilinear, and step.

        :param interpolation_method: The interpolation_method of this SeriesOutputV1.
        :type: str
        """
        if interpolation_method is None:
            raise ValueError("Invalid value for `interpolation_method`, must not be `None`")

        self._interpolation_method = interpolation_method

    @property
    def is_archived(self):
        """
        Gets the is_archived of this SeriesOutputV1.
        Whether item is isArchived

        :return: The is_archived of this SeriesOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this SeriesOutputV1.
        Whether item is isArchived

        :param is_archived: The is_archived of this SeriesOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def key_unit_of_measure(self):
        """
        Gets the key_unit_of_measure of this SeriesOutputV1.
        The unit of measure for the series keys

        :return: The key_unit_of_measure of this SeriesOutputV1.
        :rtype: str
        """
        return self._key_unit_of_measure

    @key_unit_of_measure.setter
    def key_unit_of_measure(self, key_unit_of_measure):
        """
        Sets the key_unit_of_measure of this SeriesOutputV1.
        The unit of measure for the series keys

        :param key_unit_of_measure: The key_unit_of_measure of this SeriesOutputV1.
        :type: str
        """

        self._key_unit_of_measure = key_unit_of_measure

    @property
    def maximum_interpolation(self):
        """
        Gets the maximum_interpolation of this SeriesOutputV1.
        The maximum gap that can exist between samples in the series. This setting affects interpolation behavior when the interpolation period is smaller than the maximum interpolation. If the interpolation period is smaller than the maximum interpolation, the following two statements describe the behavior. When the gap between samples is smaller than the maximum interpolation, the gap will be populated with interpolated samples at the rate specified by the interpolation period. When the gap is larger than the maximum interpolation, the gap will be populated with samples of invalid at the rate specified by the interpolation period. Example settings: 5h, 2min, 3 days, 4 years

        :return: The maximum_interpolation of this SeriesOutputV1.
        :rtype: str
        """
        return self._maximum_interpolation

    @maximum_interpolation.setter
    def maximum_interpolation(self, maximum_interpolation):
        """
        Sets the maximum_interpolation of this SeriesOutputV1.
        The maximum gap that can exist between samples in the series. This setting affects interpolation behavior when the interpolation period is smaller than the maximum interpolation. If the interpolation period is smaller than the maximum interpolation, the following two statements describe the behavior. When the gap between samples is smaller than the maximum interpolation, the gap will be populated with interpolated samples at the rate specified by the interpolation period. When the gap is larger than the maximum interpolation, the gap will be populated with samples of invalid at the rate specified by the interpolation period. Example settings: 5h, 2min, 3 days, 4 years

        :param maximum_interpolation: The maximum_interpolation of this SeriesOutputV1.
        :type: str
        """
        if maximum_interpolation is None:
            raise ValueError("Invalid value for `maximum_interpolation`, must not be `None`")

        self._maximum_interpolation = maximum_interpolation

    @property
    def name(self):
        """
        Gets the name of this SeriesOutputV1.
        The human readable name

        :return: The name of this SeriesOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SeriesOutputV1.
        The human readable name

        :param name: The name of this SeriesOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parameters(self):
        """
        Gets the parameters of this SeriesOutputV1.
        Parameters that are used in the context of executing the formula

        :return: The parameters of this SeriesOutputV1.
        :rtype: list[FormulaParameterOutputV1]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this SeriesOutputV1.
        Parameters that are used in the context of executing the formula

        :param parameters: The parameters of this SeriesOutputV1.
        :type: list[FormulaParameterOutputV1]
        """

        self._parameters = parameters

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this SeriesOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :return: The scoped_to of this SeriesOutputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this SeriesOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :param scoped_to: The scoped_to of this SeriesOutputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def status_message(self):
        """
        Gets the status_message of this SeriesOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this SeriesOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this SeriesOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this SeriesOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def type(self):
        """
        Gets the type of this SeriesOutputV1.
        The type of the item

        :return: The type of this SeriesOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SeriesOutputV1.
        The type of the item

        :param type: The type of this SeriesOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def value_unit_of_measure(self):
        """
        Gets the value_unit_of_measure of this SeriesOutputV1.
        The unit of measure for the series values

        :return: The value_unit_of_measure of this SeriesOutputV1.
        :rtype: str
        """
        return self._value_unit_of_measure

    @value_unit_of_measure.setter
    def value_unit_of_measure(self, value_unit_of_measure):
        """
        Sets the value_unit_of_measure of this SeriesOutputV1.
        The unit of measure for the series values

        :param value_unit_of_measure: The value_unit_of_measure of this SeriesOutputV1.
        :type: str
        """

        self._value_unit_of_measure = value_unit_of_measure

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
        if not isinstance(other, SeriesOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
