# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class AuthorizationRule(pulumi.CustomResource):
    listen: pulumi.Output[bool]
    """
    Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.
    """
    manage: pulumi.Output[bool]
    """
    Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.
    """
    name: pulumi.Output[str]
    """
    The name to use for this Authorization Rule. Changing this forces a new resource to be created.
    """
    namespace_name: pulumi.Output[str]
    """
    The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.
    """
    notification_hub_name: pulumi.Output[str]
    """
    The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.
    """
    primary_access_key: pulumi.Output[str]
    """
    The Primary Access Key associated with this Authorization Rule.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
    """
    secondary_access_key: pulumi.Output[str]
    """
    The Secondary Access Key associated with this Authorization Rule.
    """
    send: pulumi.Output[bool]
    """
    Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.
    """
    def __init__(__self__, resource_name, opts=None, listen=None, manage=None, name=None, namespace_name=None, notification_hub_name=None, resource_group_name=None, send=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an Authorization Rule associated with a Notification Hub within a Notification Hub Namespace.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] listen: Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.
        :param pulumi.Input[bool] manage: Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.
        :param pulumi.Input[str] name: The name to use for this Authorization Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] notification_hub_name: The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] send: Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_authorization_rule.html.markdown.
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

            __props__['listen'] = listen
            __props__['manage'] = manage
            __props__['name'] = name
            if namespace_name is None:
                raise TypeError("Missing required property 'namespace_name'")
            __props__['namespace_name'] = namespace_name
            if notification_hub_name is None:
                raise TypeError("Missing required property 'notification_hub_name'")
            __props__['notification_hub_name'] = notification_hub_name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['send'] = send
            __props__['primary_access_key'] = None
            __props__['secondary_access_key'] = None
        super(AuthorizationRule, __self__).__init__(
            'azure:notificationhub/authorizationRule:AuthorizationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, listen=None, manage=None, name=None, namespace_name=None, notification_hub_name=None, primary_access_key=None, resource_group_name=None, secondary_access_key=None, send=None):
        """
        Get an existing AuthorizationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] listen: Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.
        :param pulumi.Input[bool] manage: Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.
        :param pulumi.Input[str] name: The name to use for this Authorization Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] notification_hub_name: The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] primary_access_key: The Primary Access Key associated with this Authorization Rule.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] secondary_access_key: The Secondary Access Key associated with this Authorization Rule.
        :param pulumi.Input[bool] send: Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_authorization_rule.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["listen"] = listen
        __props__["manage"] = manage
        __props__["name"] = name
        __props__["namespace_name"] = namespace_name
        __props__["notification_hub_name"] = notification_hub_name
        __props__["primary_access_key"] = primary_access_key
        __props__["resource_group_name"] = resource_group_name
        __props__["secondary_access_key"] = secondary_access_key
        __props__["send"] = send
        return AuthorizationRule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

