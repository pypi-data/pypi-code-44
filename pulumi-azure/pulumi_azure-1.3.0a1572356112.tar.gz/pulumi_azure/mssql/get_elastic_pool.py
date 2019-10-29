# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetElasticPoolResult:
    """
    A collection of values returned by getElasticPool.
    """
    def __init__(__self__, location=None, max_size_bytes=None, max_size_gb=None, name=None, per_db_max_capacity=None, per_db_min_capacity=None, resource_group_name=None, server_name=None, tags=None, zone_redundant=None, id=None):
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists.
        """
        if max_size_bytes and not isinstance(max_size_bytes, float):
            raise TypeError("Expected argument 'max_size_bytes' to be a float")
        __self__.max_size_bytes = max_size_bytes
        """
        The max data size of the elastic pool in bytes.
        """
        if max_size_gb and not isinstance(max_size_gb, float):
            raise TypeError("Expected argument 'max_size_gb' to be a float")
        __self__.max_size_gb = max_size_gb
        """
        The max data size of the elastic pool in gigabytes.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if per_db_max_capacity and not isinstance(per_db_max_capacity, float):
            raise TypeError("Expected argument 'per_db_max_capacity' to be a float")
        __self__.per_db_max_capacity = per_db_max_capacity
        """
        The maximum capacity any one database can consume.
        """
        if per_db_min_capacity and not isinstance(per_db_min_capacity, float):
            raise TypeError("Expected argument 'per_db_min_capacity' to be a float")
        __self__.per_db_min_capacity = per_db_min_capacity
        """
        The minimum capacity all databases are guaranteed.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if server_name and not isinstance(server_name, str):
            raise TypeError("Expected argument 'server_name' to be a str")
        __self__.server_name = server_name
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        __self__.zone_redundant = zone_redundant
        """
        Whether or not this elastic pool is zone redundant.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetElasticPoolResult(GetElasticPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetElasticPoolResult(
            location=self.location,
            max_size_bytes=self.max_size_bytes,
            max_size_gb=self.max_size_gb,
            name=self.name,
            per_db_max_capacity=self.per_db_max_capacity,
            per_db_min_capacity=self.per_db_min_capacity,
            resource_group_name=self.resource_group_name,
            server_name=self.server_name,
            tags=self.tags,
            zone_redundant=self.zone_redundant,
            id=self.id)

def get_elastic_pool(name=None,resource_group_name=None,server_name=None,opts=None):
    """
    Use this data source to access information about an existing SQL elastic pool.
    
    :param str name: The name of the elastic pool.
    :param str resource_group_name: The name of the resource group which contains the elastic pool.
    :param str server_name: The name of the SQL Server which contains the elastic pool.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/mssql_elasticpool.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:mssql/getElasticPool:getElasticPool', __args__, opts=opts).value

    return AwaitableGetElasticPoolResult(
        location=__ret__.get('location'),
        max_size_bytes=__ret__.get('maxSizeBytes'),
        max_size_gb=__ret__.get('maxSizeGb'),
        name=__ret__.get('name'),
        per_db_max_capacity=__ret__.get('perDbMaxCapacity'),
        per_db_min_capacity=__ret__.get('perDbMinCapacity'),
        resource_group_name=__ret__.get('resourceGroupName'),
        server_name=__ret__.get('serverName'),
        tags=__ret__.get('tags'),
        zone_redundant=__ret__.get('zoneRedundant'),
        id=__ret__.get('id'))
