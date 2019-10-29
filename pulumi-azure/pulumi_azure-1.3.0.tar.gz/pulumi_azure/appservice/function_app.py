# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class FunctionApp(pulumi.CustomResource):
    app_service_plan_id: pulumi.Output[str]
    """
    The ID of the App Service Plan within which to create this Function App.
    """
    app_settings: pulumi.Output[dict]
    """
    A key-value pair of App Settings.
    """
    auth_settings: pulumi.Output[dict]
    """
    A `auth_settings` block as defined below.
    
      * `activeDirectory` (`dict`)
    
        * `allowedAudiences` (`list`)
        * `client_id` (`str`)
        * `client_secret` (`str`)
    
      * `additionalLoginParams` (`dict`)
      * `allowedExternalRedirectUrls` (`list`)
      * `defaultProvider` (`str`)
      * `enabled` (`bool`) - Is the Function App enabled?
      * `facebook` (`dict`)
    
        * `app_id` (`str`)
        * `appSecret` (`str`)
        * `oauthScopes` (`list`)
    
      * `google` (`dict`)
    
        * `client_id` (`str`)
        * `client_secret` (`str`)
        * `oauthScopes` (`list`)
    
      * `issuer` (`str`)
      * `microsoft` (`dict`)
    
        * `client_id` (`str`)
        * `client_secret` (`str`)
        * `oauthScopes` (`list`)
    
      * `runtimeVersion` (`str`)
      * `tokenRefreshExtensionHours` (`float`)
      * `tokenStoreEnabled` (`bool`)
      * `twitter` (`dict`)
    
        * `consumerKey` (`str`)
        * `consumerSecret` (`str`)
    
      * `unauthenticatedClientAction` (`str`)
    """
    client_affinity_enabled: pulumi.Output[bool]
    """
    Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?
    """
    connection_strings: pulumi.Output[list]
    """
    An `connection_string` block as defined below.
    
      * `name` (`str`) - The name of the Connection String.
      * `type` (`str`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
      * `value` (`str`) - The value for the Connection String.
    """
    default_hostname: pulumi.Output[str]
    """
    The default hostname associated with the Function App - such as `mysite.azurewebsites.net`
    """
    enable_builtin_logging: pulumi.Output[bool]
    """
    Should the built-in logging of this Function App be enabled? Defaults to `true`.
    """
    enabled: pulumi.Output[bool]
    """
    Is the Function App enabled?
    """
    https_only: pulumi.Output[bool]
    """
    Can the Function App only be accessed via HTTPS? Defaults to `false`.
    """
    identity: pulumi.Output[dict]
    """
    An `identity` block as defined below.
    
      * `principalId` (`str`) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
      * `tenantId` (`str`) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
      * `type` (`str`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
    """
    kind: pulumi.Output[str]
    """
    The Function App kind - such as `functionapp,linux,container`
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the Connection String.
    """
    outbound_ip_addresses: pulumi.Output[str]
    """
    A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
    """
    possible_outbound_ip_addresses: pulumi.Output[str]
    """
    A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the Function App.
    """
    site_config: pulumi.Output[dict]
    """
    A `site_config` object as defined below.
    
      * `alwaysOn` (`bool`) - Should the Function App be loaded at all times? Defaults to `false`.
      * `cors` (`dict`) - A `cors` block as defined below.
    
        * `allowedOrigins` (`list`)
        * `supportCredentials` (`bool`)
    
      * `http2Enabled` (`bool`) - Specifies whether or not the http2 protocol should be enabled. Defaults to `false`.
      * `linuxFxVersion` (`str`) - Linux App Framework and version for the AppService, e.g. `DOCKER|(golang:latest)`.
      * `use32BitWorkerProcess` (`bool`) - Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to `true`.
      * `virtualNetworkName` (`str`) - The name of the Virtual Network which this App Service should be attached to.
      * `websocketsEnabled` (`bool`) - Should WebSockets be enabled?
    """
    site_credential: pulumi.Output[dict]
    """
    A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
    
      * `password` (`str`) - The password associated with the username, which can be used to publish to this App Service.
      * `username` (`str`) - The username which can be used to publish to this App Service
    """
    storage_connection_string: pulumi.Output[str]
    """
    The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    version: pulumi.Output[str]
    """
    The runtime version associated with the Function App. Defaults to `~1`.
    """
    def __init__(__self__, resource_name, opts=None, app_service_plan_id=None, app_settings=None, auth_settings=None, client_affinity_enabled=None, connection_strings=None, enable_builtin_logging=None, enabled=None, https_only=None, identity=None, location=None, name=None, resource_group_name=None, site_config=None, storage_connection_string=None, tags=None, version=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Function App.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_plan_id: The ID of the App Service Plan within which to create this Function App.
        :param pulumi.Input[dict] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[dict] auth_settings: A `auth_settings` block as defined below.
        :param pulumi.Input[bool] client_affinity_enabled: Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?
        :param pulumi.Input[list] connection_strings: An `connection_string` block as defined below.
        :param pulumi.Input[bool] enable_builtin_logging: Should the built-in logging of this Function App be enabled? Defaults to `true`.
        :param pulumi.Input[bool] enabled: Is the Function App enabled?
        :param pulumi.Input[bool] https_only: Can the Function App only be accessed via HTTPS? Defaults to `false`.
        :param pulumi.Input[dict] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Connection String.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Function App.
        :param pulumi.Input[dict] site_config: A `site_config` object as defined below.
        :param pulumi.Input[str] storage_connection_string: The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] version: The runtime version associated with the Function App. Defaults to `~1`.
        
        The **auth_settings** object supports the following:
        
          * `activeDirectory` (`pulumi.Input[dict]`)
        
            * `allowedAudiences` (`pulumi.Input[list]`)
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
        
          * `additionalLoginParams` (`pulumi.Input[dict]`)
          * `allowedExternalRedirectUrls` (`pulumi.Input[list]`)
          * `defaultProvider` (`pulumi.Input[str]`)
          * `enabled` (`pulumi.Input[bool]`) - Is the Function App enabled?
          * `facebook` (`pulumi.Input[dict]`)
        
            * `app_id` (`pulumi.Input[str]`)
            * `appSecret` (`pulumi.Input[str]`)
            * `oauthScopes` (`pulumi.Input[list]`)
        
          * `google` (`pulumi.Input[dict]`)
        
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
            * `oauthScopes` (`pulumi.Input[list]`)
        
          * `issuer` (`pulumi.Input[str]`)
          * `microsoft` (`pulumi.Input[dict]`)
        
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
            * `oauthScopes` (`pulumi.Input[list]`)
        
          * `runtimeVersion` (`pulumi.Input[str]`)
          * `tokenRefreshExtensionHours` (`pulumi.Input[float]`)
          * `tokenStoreEnabled` (`pulumi.Input[bool]`)
          * `twitter` (`pulumi.Input[dict]`)
        
            * `consumerKey` (`pulumi.Input[str]`)
            * `consumerSecret` (`pulumi.Input[str]`)
        
          * `unauthenticatedClientAction` (`pulumi.Input[str]`)
        
        The **connection_strings** object supports the following:
        
          * `name` (`pulumi.Input[str]`) - The name of the Connection String.
          * `type` (`pulumi.Input[str]`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
          * `value` (`pulumi.Input[str]`) - The value for the Connection String.
        
        The **identity** object supports the following:
        
          * `principalId` (`pulumi.Input[str]`) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
          * `tenantId` (`pulumi.Input[str]`) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
          * `type` (`pulumi.Input[str]`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
        
        The **site_config** object supports the following:
        
          * `alwaysOn` (`pulumi.Input[bool]`) - Should the Function App be loaded at all times? Defaults to `false`.
          * `cors` (`pulumi.Input[dict]`) - A `cors` block as defined below.
        
            * `allowedOrigins` (`pulumi.Input[list]`)
            * `supportCredentials` (`pulumi.Input[bool]`)
        
          * `http2Enabled` (`pulumi.Input[bool]`) - Specifies whether or not the http2 protocol should be enabled. Defaults to `false`.
          * `linuxFxVersion` (`pulumi.Input[str]`) - Linux App Framework and version for the AppService, e.g. `DOCKER|(golang:latest)`.
          * `use32BitWorkerProcess` (`pulumi.Input[bool]`) - Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to `true`.
          * `virtualNetworkName` (`pulumi.Input[str]`) - The name of the Virtual Network which this App Service should be attached to.
          * `websocketsEnabled` (`pulumi.Input[bool]`) - Should WebSockets be enabled?

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/function_app.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if app_service_plan_id is None:
                raise TypeError("Missing required property 'app_service_plan_id'")
            __props__['app_service_plan_id'] = app_service_plan_id
            __props__['app_settings'] = app_settings
            __props__['auth_settings'] = auth_settings
            __props__['client_affinity_enabled'] = client_affinity_enabled
            __props__['connection_strings'] = connection_strings
            __props__['enable_builtin_logging'] = enable_builtin_logging
            __props__['enabled'] = enabled
            __props__['https_only'] = https_only
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['site_config'] = site_config
            if storage_connection_string is None:
                raise TypeError("Missing required property 'storage_connection_string'")
            __props__['storage_connection_string'] = storage_connection_string
            __props__['tags'] = tags
            __props__['version'] = version
            __props__['default_hostname'] = None
            __props__['kind'] = None
            __props__['outbound_ip_addresses'] = None
            __props__['possible_outbound_ip_addresses'] = None
            __props__['site_credential'] = None
        super(FunctionApp, __self__).__init__(
            'azure:appservice/functionApp:FunctionApp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, app_service_plan_id=None, app_settings=None, auth_settings=None, client_affinity_enabled=None, connection_strings=None, default_hostname=None, enable_builtin_logging=None, enabled=None, https_only=None, identity=None, kind=None, location=None, name=None, outbound_ip_addresses=None, possible_outbound_ip_addresses=None, resource_group_name=None, site_config=None, site_credential=None, storage_connection_string=None, tags=None, version=None):
        """
        Get an existing FunctionApp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_plan_id: The ID of the App Service Plan within which to create this Function App.
        :param pulumi.Input[dict] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[dict] auth_settings: A `auth_settings` block as defined below.
        :param pulumi.Input[bool] client_affinity_enabled: Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?
        :param pulumi.Input[list] connection_strings: An `connection_string` block as defined below.
        :param pulumi.Input[str] default_hostname: The default hostname associated with the Function App - such as `mysite.azurewebsites.net`
        :param pulumi.Input[bool] enable_builtin_logging: Should the built-in logging of this Function App be enabled? Defaults to `true`.
        :param pulumi.Input[bool] enabled: Is the Function App enabled?
        :param pulumi.Input[bool] https_only: Can the Function App only be accessed via HTTPS? Defaults to `false`.
        :param pulumi.Input[dict] identity: An `identity` block as defined below.
        :param pulumi.Input[str] kind: The Function App kind - such as `functionapp,linux,container`
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Connection String.
        :param pulumi.Input[str] outbound_ip_addresses: A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
        :param pulumi.Input[str] possible_outbound_ip_addresses: A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Function App.
        :param pulumi.Input[dict] site_config: A `site_config` object as defined below.
        :param pulumi.Input[dict] site_credential: A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
        :param pulumi.Input[str] storage_connection_string: The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] version: The runtime version associated with the Function App. Defaults to `~1`.
        
        The **auth_settings** object supports the following:
        
          * `activeDirectory` (`pulumi.Input[dict]`)
        
            * `allowedAudiences` (`pulumi.Input[list]`)
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
        
          * `additionalLoginParams` (`pulumi.Input[dict]`)
          * `allowedExternalRedirectUrls` (`pulumi.Input[list]`)
          * `defaultProvider` (`pulumi.Input[str]`)
          * `enabled` (`pulumi.Input[bool]`) - Is the Function App enabled?
          * `facebook` (`pulumi.Input[dict]`)
        
            * `app_id` (`pulumi.Input[str]`)
            * `appSecret` (`pulumi.Input[str]`)
            * `oauthScopes` (`pulumi.Input[list]`)
        
          * `google` (`pulumi.Input[dict]`)
        
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
            * `oauthScopes` (`pulumi.Input[list]`)
        
          * `issuer` (`pulumi.Input[str]`)
          * `microsoft` (`pulumi.Input[dict]`)
        
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
            * `oauthScopes` (`pulumi.Input[list]`)
        
          * `runtimeVersion` (`pulumi.Input[str]`)
          * `tokenRefreshExtensionHours` (`pulumi.Input[float]`)
          * `tokenStoreEnabled` (`pulumi.Input[bool]`)
          * `twitter` (`pulumi.Input[dict]`)
        
            * `consumerKey` (`pulumi.Input[str]`)
            * `consumerSecret` (`pulumi.Input[str]`)
        
          * `unauthenticatedClientAction` (`pulumi.Input[str]`)
        
        The **connection_strings** object supports the following:
        
          * `name` (`pulumi.Input[str]`) - The name of the Connection String.
          * `type` (`pulumi.Input[str]`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
          * `value` (`pulumi.Input[str]`) - The value for the Connection String.
        
        The **identity** object supports the following:
        
          * `principalId` (`pulumi.Input[str]`) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
          * `tenantId` (`pulumi.Input[str]`) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
          * `type` (`pulumi.Input[str]`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
        
        The **site_config** object supports the following:
        
          * `alwaysOn` (`pulumi.Input[bool]`) - Should the Function App be loaded at all times? Defaults to `false`.
          * `cors` (`pulumi.Input[dict]`) - A `cors` block as defined below.
        
            * `allowedOrigins` (`pulumi.Input[list]`)
            * `supportCredentials` (`pulumi.Input[bool]`)
        
          * `http2Enabled` (`pulumi.Input[bool]`) - Specifies whether or not the http2 protocol should be enabled. Defaults to `false`.
          * `linuxFxVersion` (`pulumi.Input[str]`) - Linux App Framework and version for the AppService, e.g. `DOCKER|(golang:latest)`.
          * `use32BitWorkerProcess` (`pulumi.Input[bool]`) - Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to `true`.
          * `virtualNetworkName` (`pulumi.Input[str]`) - The name of the Virtual Network which this App Service should be attached to.
          * `websocketsEnabled` (`pulumi.Input[bool]`) - Should WebSockets be enabled?
        
        The **site_credential** object supports the following:
        
          * `password` (`pulumi.Input[str]`) - The password associated with the username, which can be used to publish to this App Service.
          * `username` (`pulumi.Input[str]`) - The username which can be used to publish to this App Service

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/function_app.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["app_service_plan_id"] = app_service_plan_id
        __props__["app_settings"] = app_settings
        __props__["auth_settings"] = auth_settings
        __props__["client_affinity_enabled"] = client_affinity_enabled
        __props__["connection_strings"] = connection_strings
        __props__["default_hostname"] = default_hostname
        __props__["enable_builtin_logging"] = enable_builtin_logging
        __props__["enabled"] = enabled
        __props__["https_only"] = https_only
        __props__["identity"] = identity
        __props__["kind"] = kind
        __props__["location"] = location
        __props__["name"] = name
        __props__["outbound_ip_addresses"] = outbound_ip_addresses
        __props__["possible_outbound_ip_addresses"] = possible_outbound_ip_addresses
        __props__["resource_group_name"] = resource_group_name
        __props__["site_config"] = site_config
        __props__["site_credential"] = site_credential
        __props__["storage_connection_string"] = storage_connection_string
        __props__["tags"] = tags
        __props__["version"] = version
        return FunctionApp(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

