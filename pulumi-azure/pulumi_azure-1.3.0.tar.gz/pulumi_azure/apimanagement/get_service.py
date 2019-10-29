# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetServiceResult:
    """
    A collection of values returned by getService.
    """
    def __init__(__self__, additional_locations=None, gateway_regional_url=None, gateway_url=None, hostname_configurations=None, location=None, management_api_url=None, name=None, notification_sender_email=None, portal_url=None, public_ip_addresses=None, publisher_email=None, publisher_name=None, resource_group_name=None, scm_url=None, sku=None, sku_name=None, tags=None, id=None):
        if additional_locations and not isinstance(additional_locations, list):
            raise TypeError("Expected argument 'additional_locations' to be a list")
        __self__.additional_locations = additional_locations
        """
        One or more `additional_location` blocks as defined below
        """
        if gateway_regional_url and not isinstance(gateway_regional_url, str):
            raise TypeError("Expected argument 'gateway_regional_url' to be a str")
        __self__.gateway_regional_url = gateway_regional_url
        """
        Gateway URL of the API Management service in the Region.
        """
        if gateway_url and not isinstance(gateway_url, str):
            raise TypeError("Expected argument 'gateway_url' to be a str")
        __self__.gateway_url = gateway_url
        """
        The URL for the API Management Service's Gateway.
        """
        if hostname_configurations and not isinstance(hostname_configurations, list):
            raise TypeError("Expected argument 'hostname_configurations' to be a list")
        __self__.hostname_configurations = hostname_configurations
        """
        A `hostname_configuration` block as defined below.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The location name of the additional region among Azure Data center regions.
        """
        if management_api_url and not isinstance(management_api_url, str):
            raise TypeError("Expected argument 'management_api_url' to be a str")
        __self__.management_api_url = management_api_url
        """
        The URL for the Management API.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        Specifies the plan's pricing tier.
        """
        if notification_sender_email and not isinstance(notification_sender_email, str):
            raise TypeError("Expected argument 'notification_sender_email' to be a str")
        __self__.notification_sender_email = notification_sender_email
        """
        The email address from which the notification will be sent.
        """
        if portal_url and not isinstance(portal_url, str):
            raise TypeError("Expected argument 'portal_url' to be a str")
        __self__.portal_url = portal_url
        """
        The URL of the Publisher Portal.
        """
        if public_ip_addresses and not isinstance(public_ip_addresses, list):
            raise TypeError("Expected argument 'public_ip_addresses' to be a list")
        __self__.public_ip_addresses = public_ip_addresses
        """
        Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
        """
        if publisher_email and not isinstance(publisher_email, str):
            raise TypeError("Expected argument 'publisher_email' to be a str")
        __self__.publisher_email = publisher_email
        """
        The email of Publisher/Company of the API Management Service.
        """
        if publisher_name and not isinstance(publisher_name, str):
            raise TypeError("Expected argument 'publisher_name' to be a str")
        __self__.publisher_name = publisher_name
        """
        The name of the Publisher/Company of the API Management Service.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if scm_url and not isinstance(scm_url, str):
            raise TypeError("Expected argument 'scm_url' to be a str")
        __self__.scm_url = scm_url
        """
        The SCM (Source Code Management) endpoint.
        """
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        __self__.sku = sku
        """
        A `sku` block as documented below.
        """
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        __self__.sku_name = sku_name
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            additional_locations=self.additional_locations,
            gateway_regional_url=self.gateway_regional_url,
            gateway_url=self.gateway_url,
            hostname_configurations=self.hostname_configurations,
            location=self.location,
            management_api_url=self.management_api_url,
            name=self.name,
            notification_sender_email=self.notification_sender_email,
            portal_url=self.portal_url,
            public_ip_addresses=self.public_ip_addresses,
            publisher_email=self.publisher_email,
            publisher_name=self.publisher_name,
            resource_group_name=self.resource_group_name,
            scm_url=self.scm_url,
            sku=self.sku,
            sku_name=self.sku_name,
            tags=self.tags,
            id=self.id)

def get_service(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing API Management Service.
    
    :param str name: The name of the API Management service.
    :param str resource_group_name: The Name of the Resource Group in which the API Management Service exists.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:apimanagement/getService:getService', __args__, opts=opts).value

    return AwaitableGetServiceResult(
        additional_locations=__ret__.get('additionalLocations'),
        gateway_regional_url=__ret__.get('gatewayRegionalUrl'),
        gateway_url=__ret__.get('gatewayUrl'),
        hostname_configurations=__ret__.get('hostnameConfigurations'),
        location=__ret__.get('location'),
        management_api_url=__ret__.get('managementApiUrl'),
        name=__ret__.get('name'),
        notification_sender_email=__ret__.get('notificationSenderEmail'),
        portal_url=__ret__.get('portalUrl'),
        public_ip_addresses=__ret__.get('publicIpAddresses'),
        publisher_email=__ret__.get('publisherEmail'),
        publisher_name=__ret__.get('publisherName'),
        resource_group_name=__ret__.get('resourceGroupName'),
        scm_url=__ret__.get('scmUrl'),
        sku=__ret__.get('sku'),
        sku_name=__ret__.get('skuName'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
