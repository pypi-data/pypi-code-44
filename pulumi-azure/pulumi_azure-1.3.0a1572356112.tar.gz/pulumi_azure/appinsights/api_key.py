# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ApiKey(pulumi.CustomResource):
    api_key: pulumi.Output[str]
    """
    The API Key secret (Sensitive).
    """
    application_insights_id: pulumi.Output[str]
    """
    The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Application Insights API key. Changing this forces a
    new resource to be created.
    """
    read_permissions: pulumi.Output[list]
    """
    Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created. 
    """
    write_permissions: pulumi.Output[list]
    """
    Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, application_insights_id=None, name=None, read_permissions=None, write_permissions=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an Application Insights API key.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a
               new resource to be created.
        :param pulumi.Input[list] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created. 
        :param pulumi.Input[list] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/application_insights_api_key.html.markdown.
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

            if application_insights_id is None:
                raise TypeError("Missing required property 'application_insights_id'")
            __props__['application_insights_id'] = application_insights_id
            __props__['name'] = name
            __props__['read_permissions'] = read_permissions
            __props__['write_permissions'] = write_permissions
            __props__['api_key'] = None
        super(ApiKey, __self__).__init__(
            'azure:appinsights/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_key=None, application_insights_id=None, name=None, read_permissions=None, write_permissions=None):
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API Key secret (Sensitive).
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a
               new resource to be created.
        :param pulumi.Input[list] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created. 
        :param pulumi.Input[list] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/application_insights_api_key.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["api_key"] = api_key
        __props__["application_insights_id"] = application_insights_id
        __props__["name"] = name
        __props__["read_permissions"] = read_permissions
        __props__["write_permissions"] = write_permissions
        return ApiKey(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

