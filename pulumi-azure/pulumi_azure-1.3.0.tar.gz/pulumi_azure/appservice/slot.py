# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Slot(pulumi.CustomResource):
    app_service_name: pulumi.Output[str]
    """
    The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.
    """
    app_service_plan_id: pulumi.Output[str]
    """
    The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.
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
      * `enabled` (`bool`) - Is the App Service Slot Enabled?
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
    Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?
    """
    connection_strings: pulumi.Output[list]
    """
    An `connection_string` block as defined below.
    
      * `name` (`str`) - The name of the Connection String.
      * `type` (`str`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
      * `value` (`str`) - The value for the Connection String.
    """
    default_site_hostname: pulumi.Output[str]
    """
    The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`
    """
    enabled: pulumi.Output[bool]
    """
    Is the App Service Slot Enabled?
    """
    https_only: pulumi.Output[bool]
    """
    Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.
    """
    identity: pulumi.Output[dict]
    """
    A Managed Service Identity block as defined below.
    
      * `identityIds` (`list`)
      * `principalId` (`str`)
      * `tenantId` (`str`)
      * `type` (`str`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    logs: pulumi.Output[dict]
    name: pulumi.Output[str]
    """
    The name of the Connection String.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the App Service Slot component.
    """
    site_config: pulumi.Output[dict]
    """
    A `site_config` object as defined below.
    
      * `alwaysOn` (`bool`) - Should the app be loaded at all times? Defaults to `false`.
      * `appCommandLine` (`str`) - App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
      * `cors` (`dict`) - A `cors` block as defined below.
    
        * `allowedOrigins` (`list`)
        * `supportCredentials` (`bool`)
    
      * `defaultDocuments` (`list`) - The ordering of default documents to load, if an address isn't specified.
      * `dotnetFrameworkVersion` (`str`) - The version of the .net framework's CLR used in this App Service Slot. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
      * `ftpsState` (`str`)
      * `http2Enabled` (`bool`) - Is HTTP2 Enabled on this App Service? Defaults to `false`.
      * `ipRestrictions` (`list`) - A [List of objects](https://www.terraform.io/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.
    
        * `ipAddress` (`str`)
        * `subnetMask` (`str`)
        * `virtualNetworkSubnetId` (`str`)
    
      * `javaContainer` (`str`) - The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JETTY` and `TOMCAT`.
      * `javaContainerVersion` (`str`) - The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
      * `javaVersion` (`str`) - The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11`.
      * `linuxFxVersion` (`str`)
      * `localMysqlEnabled` (`bool`) - Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
      * `managedPipelineMode` (`str`) - The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
      * `minTlsVersion` (`str`) - The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
      * `phpVersion` (`str`) - The version of PHP to use in this App Service Slot. Possible values are `5.5`, `5.6`, `7.0`, `7.1` and `7.2`.
      * `pythonVersion` (`str`) - The version of Python to use in this App Service Slot. Possible values are `2.7` and `3.4`.
      * `remoteDebuggingEnabled` (`bool`) - Is Remote Debugging Enabled? Defaults to `false`.
      * `remoteDebuggingVersion` (`str`) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
      * `scmType` (`str`) - The type of Source Control enabled for this App Service Slot. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO` and `VSTSRM`
      * `use32BitWorkerProcess` (`bool`) - Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?
      * `virtualNetworkName` (`str`) - The name of the Virtual Network which this App Service Slot should be attached to.
      * `websocketsEnabled` (`bool`) - Should WebSockets be enabled?
      * `windowsFxVersion` (`str`)
    """
    site_credential: pulumi.Output[dict]
    """
    A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
    
      * `password` (`str`) - The password associated with the username, which can be used to publish to this App Service.
      * `username` (`str`) - The username which can be used to publish to this App Service
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, app_service_name=None, app_service_plan_id=None, app_settings=None, auth_settings=None, client_affinity_enabled=None, connection_strings=None, enabled=None, https_only=None, identity=None, location=None, logs=None, name=None, resource_group_name=None, site_config=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an App Service Slot (within an App Service).
        
        > **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `appservice.AppService` resource will be overwritten when promoting a Slot using the `appservice.ActiveSlot` resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.
        :param pulumi.Input[str] app_service_plan_id: The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[dict] auth_settings: A `auth_settings` block as defined below.
        :param pulumi.Input[bool] client_affinity_enabled: Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?
        :param pulumi.Input[list] connection_strings: An `connection_string` block as defined below.
        :param pulumi.Input[bool] enabled: Is the App Service Slot Enabled?
        :param pulumi.Input[bool] https_only: Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.
        :param pulumi.Input[dict] identity: A Managed Service Identity block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Connection String.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Service Slot component.
        :param pulumi.Input[dict] site_config: A `site_config` object as defined below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        
        The **auth_settings** object supports the following:
        
          * `activeDirectory` (`pulumi.Input[dict]`)
        
            * `allowedAudiences` (`pulumi.Input[list]`)
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
        
          * `additionalLoginParams` (`pulumi.Input[dict]`)
          * `allowedExternalRedirectUrls` (`pulumi.Input[list]`)
          * `defaultProvider` (`pulumi.Input[str]`)
          * `enabled` (`pulumi.Input[bool]`) - Is the App Service Slot Enabled?
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
        
          * `identityIds` (`pulumi.Input[list]`)
          * `principalId` (`pulumi.Input[str]`)
          * `tenantId` (`pulumi.Input[str]`)
          * `type` (`pulumi.Input[str]`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
        
        The **logs** object supports the following:
        
          * `applicationLogs` (`pulumi.Input[dict]`)
        
            * `azureBlobStorage` (`pulumi.Input[dict]`)
        
              * `level` (`pulumi.Input[str]`)
              * `retentionInDays` (`pulumi.Input[float]`)
              * `sasUrl` (`pulumi.Input[str]`)
        
          * `httpLogs` (`pulumi.Input[dict]`)
        
            * `azureBlobStorage` (`pulumi.Input[dict]`)
        
              * `retentionInDays` (`pulumi.Input[float]`)
              * `sasUrl` (`pulumi.Input[str]`)
        
            * `fileSystem` (`pulumi.Input[dict]`)
        
              * `retentionInDays` (`pulumi.Input[float]`)
              * `retentionInMb` (`pulumi.Input[float]`)
        
        The **site_config** object supports the following:
        
          * `alwaysOn` (`pulumi.Input[bool]`) - Should the app be loaded at all times? Defaults to `false`.
          * `appCommandLine` (`pulumi.Input[str]`) - App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
          * `cors` (`pulumi.Input[dict]`) - A `cors` block as defined below.
        
            * `allowedOrigins` (`pulumi.Input[list]`)
            * `supportCredentials` (`pulumi.Input[bool]`)
        
          * `defaultDocuments` (`pulumi.Input[list]`) - The ordering of default documents to load, if an address isn't specified.
          * `dotnetFrameworkVersion` (`pulumi.Input[str]`) - The version of the .net framework's CLR used in this App Service Slot. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
          * `ftpsState` (`pulumi.Input[str]`)
          * `http2Enabled` (`pulumi.Input[bool]`) - Is HTTP2 Enabled on this App Service? Defaults to `false`.
          * `ipRestrictions` (`pulumi.Input[list]`) - A [List of objects](https://www.terraform.io/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.
        
            * `ipAddress` (`pulumi.Input[str]`)
            * `subnetMask` (`pulumi.Input[str]`)
            * `virtualNetworkSubnetId` (`pulumi.Input[str]`)
        
          * `javaContainer` (`pulumi.Input[str]`) - The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JETTY` and `TOMCAT`.
          * `javaContainerVersion` (`pulumi.Input[str]`) - The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
          * `javaVersion` (`pulumi.Input[str]`) - The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11`.
          * `linuxFxVersion` (`pulumi.Input[str]`)
          * `localMysqlEnabled` (`pulumi.Input[bool]`) - Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
          * `managedPipelineMode` (`pulumi.Input[str]`) - The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
          * `minTlsVersion` (`pulumi.Input[str]`) - The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
          * `phpVersion` (`pulumi.Input[str]`) - The version of PHP to use in this App Service Slot. Possible values are `5.5`, `5.6`, `7.0`, `7.1` and `7.2`.
          * `pythonVersion` (`pulumi.Input[str]`) - The version of Python to use in this App Service Slot. Possible values are `2.7` and `3.4`.
          * `remoteDebuggingEnabled` (`pulumi.Input[bool]`) - Is Remote Debugging Enabled? Defaults to `false`.
          * `remoteDebuggingVersion` (`pulumi.Input[str]`) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
          * `scmType` (`pulumi.Input[str]`) - The type of Source Control enabled for this App Service Slot. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO` and `VSTSRM`
          * `use32BitWorkerProcess` (`pulumi.Input[bool]`) - Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?
          * `virtualNetworkName` (`pulumi.Input[str]`) - The name of the Virtual Network which this App Service Slot should be attached to.
          * `websocketsEnabled` (`pulumi.Input[bool]`) - Should WebSockets be enabled?
          * `windowsFxVersion` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/app_service_slot.html.markdown.
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

            if app_service_name is None:
                raise TypeError("Missing required property 'app_service_name'")
            __props__['app_service_name'] = app_service_name
            if app_service_plan_id is None:
                raise TypeError("Missing required property 'app_service_plan_id'")
            __props__['app_service_plan_id'] = app_service_plan_id
            __props__['app_settings'] = app_settings
            __props__['auth_settings'] = auth_settings
            __props__['client_affinity_enabled'] = client_affinity_enabled
            __props__['connection_strings'] = connection_strings
            __props__['enabled'] = enabled
            __props__['https_only'] = https_only
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['logs'] = logs
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['site_config'] = site_config
            __props__['tags'] = tags
            __props__['default_site_hostname'] = None
            __props__['site_credential'] = None
        super(Slot, __self__).__init__(
            'azure:appservice/slot:Slot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, app_service_name=None, app_service_plan_id=None, app_settings=None, auth_settings=None, client_affinity_enabled=None, connection_strings=None, default_site_hostname=None, enabled=None, https_only=None, identity=None, location=None, logs=None, name=None, resource_group_name=None, site_config=None, site_credential=None, tags=None):
        """
        Get an existing Slot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.
        :param pulumi.Input[str] app_service_plan_id: The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[dict] auth_settings: A `auth_settings` block as defined below.
        :param pulumi.Input[bool] client_affinity_enabled: Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?
        :param pulumi.Input[list] connection_strings: An `connection_string` block as defined below.
        :param pulumi.Input[str] default_site_hostname: The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`
        :param pulumi.Input[bool] enabled: Is the App Service Slot Enabled?
        :param pulumi.Input[bool] https_only: Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.
        :param pulumi.Input[dict] identity: A Managed Service Identity block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Connection String.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Service Slot component.
        :param pulumi.Input[dict] site_config: A `site_config` object as defined below.
        :param pulumi.Input[dict] site_credential: A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        
        The **auth_settings** object supports the following:
        
          * `activeDirectory` (`pulumi.Input[dict]`)
        
            * `allowedAudiences` (`pulumi.Input[list]`)
            * `client_id` (`pulumi.Input[str]`)
            * `client_secret` (`pulumi.Input[str]`)
        
          * `additionalLoginParams` (`pulumi.Input[dict]`)
          * `allowedExternalRedirectUrls` (`pulumi.Input[list]`)
          * `defaultProvider` (`pulumi.Input[str]`)
          * `enabled` (`pulumi.Input[bool]`) - Is the App Service Slot Enabled?
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
        
          * `identityIds` (`pulumi.Input[list]`)
          * `principalId` (`pulumi.Input[str]`)
          * `tenantId` (`pulumi.Input[str]`)
          * `type` (`pulumi.Input[str]`) - The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
        
        The **logs** object supports the following:
        
          * `applicationLogs` (`pulumi.Input[dict]`)
        
            * `azureBlobStorage` (`pulumi.Input[dict]`)
        
              * `level` (`pulumi.Input[str]`)
              * `retentionInDays` (`pulumi.Input[float]`)
              * `sasUrl` (`pulumi.Input[str]`)
        
          * `httpLogs` (`pulumi.Input[dict]`)
        
            * `azureBlobStorage` (`pulumi.Input[dict]`)
        
              * `retentionInDays` (`pulumi.Input[float]`)
              * `sasUrl` (`pulumi.Input[str]`)
        
            * `fileSystem` (`pulumi.Input[dict]`)
        
              * `retentionInDays` (`pulumi.Input[float]`)
              * `retentionInMb` (`pulumi.Input[float]`)
        
        The **site_config** object supports the following:
        
          * `alwaysOn` (`pulumi.Input[bool]`) - Should the app be loaded at all times? Defaults to `false`.
          * `appCommandLine` (`pulumi.Input[str]`) - App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
          * `cors` (`pulumi.Input[dict]`) - A `cors` block as defined below.
        
            * `allowedOrigins` (`pulumi.Input[list]`)
            * `supportCredentials` (`pulumi.Input[bool]`)
        
          * `defaultDocuments` (`pulumi.Input[list]`) - The ordering of default documents to load, if an address isn't specified.
          * `dotnetFrameworkVersion` (`pulumi.Input[str]`) - The version of the .net framework's CLR used in this App Service Slot. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
          * `ftpsState` (`pulumi.Input[str]`)
          * `http2Enabled` (`pulumi.Input[bool]`) - Is HTTP2 Enabled on this App Service? Defaults to `false`.
          * `ipRestrictions` (`pulumi.Input[list]`) - A [List of objects](https://www.terraform.io/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.
        
            * `ipAddress` (`pulumi.Input[str]`)
            * `subnetMask` (`pulumi.Input[str]`)
            * `virtualNetworkSubnetId` (`pulumi.Input[str]`)
        
          * `javaContainer` (`pulumi.Input[str]`) - The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JETTY` and `TOMCAT`.
          * `javaContainerVersion` (`pulumi.Input[str]`) - The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
          * `javaVersion` (`pulumi.Input[str]`) - The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11`.
          * `linuxFxVersion` (`pulumi.Input[str]`)
          * `localMysqlEnabled` (`pulumi.Input[bool]`) - Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
          * `managedPipelineMode` (`pulumi.Input[str]`) - The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
          * `minTlsVersion` (`pulumi.Input[str]`) - The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
          * `phpVersion` (`pulumi.Input[str]`) - The version of PHP to use in this App Service Slot. Possible values are `5.5`, `5.6`, `7.0`, `7.1` and `7.2`.
          * `pythonVersion` (`pulumi.Input[str]`) - The version of Python to use in this App Service Slot. Possible values are `2.7` and `3.4`.
          * `remoteDebuggingEnabled` (`pulumi.Input[bool]`) - Is Remote Debugging Enabled? Defaults to `false`.
          * `remoteDebuggingVersion` (`pulumi.Input[str]`) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
          * `scmType` (`pulumi.Input[str]`) - The type of Source Control enabled for this App Service Slot. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO` and `VSTSRM`
          * `use32BitWorkerProcess` (`pulumi.Input[bool]`) - Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?
          * `virtualNetworkName` (`pulumi.Input[str]`) - The name of the Virtual Network which this App Service Slot should be attached to.
          * `websocketsEnabled` (`pulumi.Input[bool]`) - Should WebSockets be enabled?
          * `windowsFxVersion` (`pulumi.Input[str]`)
        
        The **site_credential** object supports the following:
        
          * `password` (`pulumi.Input[str]`) - The password associated with the username, which can be used to publish to this App Service.
          * `username` (`pulumi.Input[str]`) - The username which can be used to publish to this App Service

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/app_service_slot.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["app_service_name"] = app_service_name
        __props__["app_service_plan_id"] = app_service_plan_id
        __props__["app_settings"] = app_settings
        __props__["auth_settings"] = auth_settings
        __props__["client_affinity_enabled"] = client_affinity_enabled
        __props__["connection_strings"] = connection_strings
        __props__["default_site_hostname"] = default_site_hostname
        __props__["enabled"] = enabled
        __props__["https_only"] = https_only
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["logs"] = logs
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["site_config"] = site_config
        __props__["site_credential"] = site_credential
        __props__["tags"] = tags
        return Slot(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

