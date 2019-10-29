# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class DscConfiguration(pulumi.CustomResource):
    automation_account_name: pulumi.Output[str]
    """
    The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.
    """
    content_embedded: pulumi.Output[str]
    """
    The PowerShell DSC Configuration script.
    """
    description: pulumi.Output[str]
    """
    Description to go with DSC Configuration.
    """
    location: pulumi.Output[str]
    """
    Must be the same location as the Automation Account.
    """
    log_verbose: pulumi.Output[bool]
    """
    Verbose log option.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.
    """
    state: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, automation_account_name=None, content_embedded=None, description=None, location=None, log_verbose=None, name=None, resource_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Automation DSC Configuration.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] content_embedded: The PowerShell DSC Configuration script.
        :param pulumi.Input[str] description: Description to go with DSC Configuration.
        :param pulumi.Input[str] location: Must be the same location as the Automation Account.
        :param pulumi.Input[bool] log_verbose: Verbose log option.
        :param pulumi.Input[str] name: Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_dsc_configuration.html.markdown.
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

            if automation_account_name is None:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__['automation_account_name'] = automation_account_name
            if content_embedded is None:
                raise TypeError("Missing required property 'content_embedded'")
            __props__['content_embedded'] = content_embedded
            __props__['description'] = description
            __props__['location'] = location
            __props__['log_verbose'] = log_verbose
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['state'] = None
        super(DscConfiguration, __self__).__init__(
            'azure:automation/dscConfiguration:DscConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, automation_account_name=None, content_embedded=None, description=None, location=None, log_verbose=None, name=None, resource_group_name=None, state=None):
        """
        Get an existing DscConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] content_embedded: The PowerShell DSC Configuration script.
        :param pulumi.Input[str] description: Description to go with DSC Configuration.
        :param pulumi.Input[str] location: Must be the same location as the Automation Account.
        :param pulumi.Input[bool] log_verbose: Verbose log option.
        :param pulumi.Input[str] name: Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_dsc_configuration.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["automation_account_name"] = automation_account_name
        __props__["content_embedded"] = content_embedded
        __props__["description"] = description
        __props__["location"] = location
        __props__["log_verbose"] = log_verbose
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["state"] = state
        return DscConfiguration(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

