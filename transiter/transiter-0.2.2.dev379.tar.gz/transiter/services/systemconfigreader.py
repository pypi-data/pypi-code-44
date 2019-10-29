import enum

import pytimeparse
import strictyaml
from strictyaml import (
    Map,
    Str,
    Seq,
    MapPattern,
    Optional,
    Bool,
    EmptyList,
    EmptyDict,
    Float,
    ScalarValidator,
    EmptyNone,
)
from strictyaml.exceptions import YAMLSerializationError

from transiter import exceptions
from transiter import models


class HumanReadableTimePeriod(ScalarValidator):
    """
    A validator the converts human readable time period like "10 minutes" into the
    number of seconds in the period, as determined by pytimeparse.
    """

    def __init__(self):
        pass

    def validate_scalar(self, chunk):
        value = pytimeparse.parse(chunk.contents)
        if value is None:
            chunk.expecting_but_found(
                "when expecting something that could be interpreted as a time period",
                "found '{}'".format(chunk.contents),
            )
        return value

    @staticmethod
    def to_yaml(data):
        return "{} seconds".format(data)


class PyEnum(ScalarValidator):
    """
    A validator for enum.Enum types. This validator ensures that the provided string
    in the YAML file is the name of one of the enum's elements, and then casts the
    result to that enum element.
    """

    def __init__(self, enum_):
        self._enum = enum_
        assert issubclass(
            self._enum, enum.Enum
        ), "argument must be a enum.Enum or subclass thereof"

    def validate_scalar(self, chunk):
        try:
            val = self._enum[chunk.contents]
        except KeyError:
            chunk.expecting_but_found(
                "when expecting one of: {0}".format(
                    ", ".join(elem.name for elem in self._enum)
                )
            )
        else:
            return val

    def to_yaml(self, data):
        if data not in self._enum:
            raise YAMLSerializationError(
                "Got '{0}' when  expecting one of: {1}".format(
                    data, ", ".join(str(elem) for elem in self._enum)
                )
            )
        return data.name

    def __repr__(self):
        return u"PyEnum({0})".format(repr(self._enum))


# These are all constants so that reading the JSON response is less fragile
AUTO_UPDATE = "auto_update"
BUILT_IN = "built_in"
CONDITIONS = "conditions"
CUSTOM = "custom"
DIRECTION_RULES_FILES = "direction_rules_files"
ENABLED = "enabled"
FEEDS = "feeds"
HEADERS = "headers"
HTTP = "http"
NAME = "name"
PACKAGES = "packages"
PARSER = "parser"
PERIOD = "period"
REQUIRED_FOR_INSTALL = "required_for_install"
REQUIREMENTS = "requirements"
SERVICE_MAPS = "service_maps"
SETTINGS = "settings"
SOURCE = "source"
THRESHOLD = "threshold"
URL = "url"
USE_FOR_ROUTES_AT_STOP = "use_for_routes_at_stop"
USE_FOR_STOPS_IN_ROUTE = "use_for_stops_in_route"


_schema = Map(
    {
        NAME: Str(),
        Optional(REQUIREMENTS, {PACKAGES: [], SETTINGS: []}): Map(
            {
                Optional(PACKAGES, []): Seq(Str()) | EmptyList(),
                Optional(SETTINGS, []): Seq(Str()) | EmptyList(),
            }
        ),
        FEEDS: MapPattern(
            Str(),
            Map(
                {
                    HTTP: Map(
                        {
                            URL: Str(),
                            Optional(HEADERS, {}): MapPattern(Str(), Str())
                            | EmptyDict(),
                        }
                    ),
                    PARSER: Map(
                        {
                            Optional(BUILT_IN, None): PyEnum(models.Feed.BuiltInParser),
                            Optional(CUSTOM, None): Str(),
                        }
                    ),
                    Optional(AUTO_UPDATE, {ENABLED: False, PERIOD: -1}): Map(
                        {
                            Optional(ENABLED, True): Bool(),
                            Optional(PERIOD, -1): HumanReadableTimePeriod(),
                        }
                    ),
                    Optional(REQUIRED_FOR_INSTALL, False): Bool(),
                }
            ),
        ),
        SERVICE_MAPS: MapPattern(
            Str(),
            Map(
                {
                    SOURCE: PyEnum(models.ServiceMapGroup.ServiceMapSource),
                    Optional(THRESHOLD, 0): Float(),
                    Optional(CONDITIONS, None): Str(),
                    Optional(USE_FOR_STOPS_IN_ROUTE, False): Bool(),
                    Optional(USE_FOR_ROUTES_AT_STOP, False): Bool(),
                }
            ),
        ),
        Optional(DIRECTION_RULES_FILES, []): Seq(Map({HTTP: Map({URL: Str()})}))
        | EmptyList(),
    }
)


def read(yaml, setting_to_value=None, label="transit system config"):

    try:
        raw_config = strictyaml.load(yaml, _schema, label=label).data
    except strictyaml.YAMLValidationError as error:
        raise exceptions.InvalidSystemConfigFile(
            "System config is valid YAML but is not a valid system config\n"
            + str(error)
        )
    except strictyaml.YAMLError as error:
        raise exceptions.InvalidSystemConfigFile(
            "Provided system config file cannot be parsed as YAML\n" + str(error)
        )

    if setting_to_value is None:
        setting_to_value = {}
    required_settings = raw_config[REQUIREMENTS][SETTINGS]

    missing_settings = set(required_settings) - set(setting_to_value.keys())
    if len(missing_settings) > 0:
        raise exceptions.InstallError(
            "Missing required settings: {}".format(", ".join(missing_settings))
        )

    required_setting_to_value = {
        required_setting: setting_to_value[required_setting]
        for required_setting in required_settings
    }
    return _substitute_settings(raw_config, required_setting_to_value)


def _substitute_settings(root_element, setting_to_value):
    def traverse(element):
        if isinstance(element, dict):
            return {key: traverse(value) for key, value in element.items()}
        if isinstance(element, list):
            return [traverse(value) for value in element]
        if isinstance(element, str):
            return element.format(**setting_to_value)
        return element

    return traverse(root_element)
