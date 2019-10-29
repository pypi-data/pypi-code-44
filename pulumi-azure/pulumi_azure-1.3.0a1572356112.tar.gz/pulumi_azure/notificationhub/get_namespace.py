# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetNamespaceResult:
    """
    A collection of values returned by getNamespace.
    """
    def __init__(__self__, enabled=None, location=None, name=None, namespace_type=None, resource_group_name=None, servicebus_endpoint=None, sku=None, id=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        __self__.enabled = enabled
        """
        Is this Notification Hub Namespace enabled?
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The Azure Region in which this Notification Hub Namespace exists.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        (Required) The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard.`
        """
        if namespace_type and not isinstance(namespace_type, str):
            raise TypeError("Expected argument 'namespace_type' to be a str")
        __self__.namespace_type = namespace_type
        """
        The Type of Namespace, such as `Messaging` or `NotificationHub`.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if servicebus_endpoint and not isinstance(servicebus_endpoint, str):
            raise TypeError("Expected argument 'servicebus_endpoint' to be a str")
        __self__.servicebus_endpoint = servicebus_endpoint
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        __self__.sku = sku
        """
        A `sku` block as defined below.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetNamespaceResult(GetNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceResult(
            enabled=self.enabled,
            location=self.location,
            name=self.name,
            namespace_type=self.namespace_type,
            resource_group_name=self.resource_group_name,
            servicebus_endpoint=self.servicebus_endpoint,
            sku=self.sku,
            id=self.id)

def get_namespace(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Notification Hub Namespace.
    
    :param str name: Specifies the Name of the Notification Hub Namespace.
    :param str resource_group_name: Specifies the Name of the Resource Group within which the Notification Hub exists.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub_namespace.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:notificationhub/getNamespace:getNamespace', __args__, opts=opts).value

    return AwaitableGetNamespaceResult(
        enabled=__ret__.get('enabled'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        namespace_type=__ret__.get('namespaceType'),
        resource_group_name=__ret__.get('resourceGroupName'),
        servicebus_endpoint=__ret__.get('servicebusEndpoint'),
        sku=__ret__.get('sku'),
        id=__ret__.get('id'))
