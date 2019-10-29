# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class LinuxVirtualMachine(pulumi.CustomResource):
    allow_claim: pulumi.Output[bool]
    """
    Can this Virtual Machine be claimed by users? Defaults to `true`.
    """
    disallow_public_ip_address: pulumi.Output[bool]
    """
    Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.
    """
    fqdn: pulumi.Output[str]
    """
    The FQDN of the Virtual Machine.
    """
    gallery_image_reference: pulumi.Output[dict]
    """
    A `gallery_image_reference` block as defined below.
    
      * `offer` (`str`)
      * `publisher` (`str`)
      * `sku` (`str`)
      * `version` (`str`)
    """
    inbound_nat_rules: pulumi.Output[list]
    """
    One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.
    
      * `backendPort` (`float`)
      * `frontendPort` (`float`) - The frontend port associated with this Inbound NAT Rule.
      * `protocol` (`str`)
    """
    lab_name: pulumi.Output[str]
    """
    Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.
    """
    lab_subnet_name: pulumi.Output[str]
    """
    The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.
    """
    lab_virtual_network_id: pulumi.Output[str]
    """
    The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.
    """
    notes: pulumi.Output[str]
    """
    Any notes about the Virtual Machine.
    """
    password: pulumi.Output[str]
    """
    The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.
    """
    size: pulumi.Output[str]
    """
    The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.
    """
    ssh_key: pulumi.Output[str]
    """
    The SSH Key associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.
    """
    storage_type: pulumi.Output[str]
    """
    The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    unique_identifier: pulumi.Output[str]
    """
    The unique immutable identifier of the Virtual Machine.
    """
    username: pulumi.Output[str]
    """
    The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, allow_claim=None, disallow_public_ip_address=None, gallery_image_reference=None, inbound_nat_rules=None, lab_name=None, lab_subnet_name=None, lab_virtual_network_id=None, location=None, name=None, notes=None, password=None, resource_group_name=None, size=None, ssh_key=None, storage_type=None, tags=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Linux Virtual Machine within a Dev Test Lab.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_claim: Can this Virtual Machine be claimed by users? Defaults to `true`.
        :param pulumi.Input[bool] disallow_public_ip_address: Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.
        :param pulumi.Input[dict] gallery_image_reference: A `gallery_image_reference` block as defined below.
        :param pulumi.Input[list] inbound_nat_rules: One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] lab_name: Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] lab_subnet_name: The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] lab_virtual_network_id: The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[str] notes: Any notes about the Virtual Machine.
        :param pulumi.Input[str] password: The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] size: The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssh_key: The SSH Key associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_type: The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] username: The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.
        
        The **gallery_image_reference** object supports the following:
        
          * `offer` (`pulumi.Input[str]`)
          * `publisher` (`pulumi.Input[str]`)
          * `sku` (`pulumi.Input[str]`)
          * `version` (`pulumi.Input[str]`)
        
        The **inbound_nat_rules** object supports the following:
        
          * `backendPort` (`pulumi.Input[float]`)
          * `frontendPort` (`pulumi.Input[float]`) - The frontend port associated with this Inbound NAT Rule.
          * `protocol` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_linux_virtual_machine.html.markdown.
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

            __props__['allow_claim'] = allow_claim
            __props__['disallow_public_ip_address'] = disallow_public_ip_address
            if gallery_image_reference is None:
                raise TypeError("Missing required property 'gallery_image_reference'")
            __props__['gallery_image_reference'] = gallery_image_reference
            __props__['inbound_nat_rules'] = inbound_nat_rules
            if lab_name is None:
                raise TypeError("Missing required property 'lab_name'")
            __props__['lab_name'] = lab_name
            if lab_subnet_name is None:
                raise TypeError("Missing required property 'lab_subnet_name'")
            __props__['lab_subnet_name'] = lab_subnet_name
            if lab_virtual_network_id is None:
                raise TypeError("Missing required property 'lab_virtual_network_id'")
            __props__['lab_virtual_network_id'] = lab_virtual_network_id
            __props__['location'] = location
            __props__['name'] = name
            __props__['notes'] = notes
            __props__['password'] = password
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if size is None:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['ssh_key'] = ssh_key
            if storage_type is None:
                raise TypeError("Missing required property 'storage_type'")
            __props__['storage_type'] = storage_type
            __props__['tags'] = tags
            if username is None:
                raise TypeError("Missing required property 'username'")
            __props__['username'] = username
            __props__['fqdn'] = None
            __props__['unique_identifier'] = None
        super(LinuxVirtualMachine, __self__).__init__(
            'azure:devtest/linuxVirtualMachine:LinuxVirtualMachine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, allow_claim=None, disallow_public_ip_address=None, fqdn=None, gallery_image_reference=None, inbound_nat_rules=None, lab_name=None, lab_subnet_name=None, lab_virtual_network_id=None, location=None, name=None, notes=None, password=None, resource_group_name=None, size=None, ssh_key=None, storage_type=None, tags=None, unique_identifier=None, username=None):
        """
        Get an existing LinuxVirtualMachine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_claim: Can this Virtual Machine be claimed by users? Defaults to `true`.
        :param pulumi.Input[bool] disallow_public_ip_address: Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.
        :param pulumi.Input[str] fqdn: The FQDN of the Virtual Machine.
        :param pulumi.Input[dict] gallery_image_reference: A `gallery_image_reference` block as defined below.
        :param pulumi.Input[list] inbound_nat_rules: One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] lab_name: Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] lab_subnet_name: The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] lab_virtual_network_id: The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[str] notes: Any notes about the Virtual Machine.
        :param pulumi.Input[str] password: The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] size: The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssh_key: The SSH Key associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_type: The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of the Virtual Machine.
        :param pulumi.Input[str] username: The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.
        
        The **gallery_image_reference** object supports the following:
        
          * `offer` (`pulumi.Input[str]`)
          * `publisher` (`pulumi.Input[str]`)
          * `sku` (`pulumi.Input[str]`)
          * `version` (`pulumi.Input[str]`)
        
        The **inbound_nat_rules** object supports the following:
        
          * `backendPort` (`pulumi.Input[float]`)
          * `frontendPort` (`pulumi.Input[float]`) - The frontend port associated with this Inbound NAT Rule.
          * `protocol` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_linux_virtual_machine.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["allow_claim"] = allow_claim
        __props__["disallow_public_ip_address"] = disallow_public_ip_address
        __props__["fqdn"] = fqdn
        __props__["gallery_image_reference"] = gallery_image_reference
        __props__["inbound_nat_rules"] = inbound_nat_rules
        __props__["lab_name"] = lab_name
        __props__["lab_subnet_name"] = lab_subnet_name
        __props__["lab_virtual_network_id"] = lab_virtual_network_id
        __props__["location"] = location
        __props__["name"] = name
        __props__["notes"] = notes
        __props__["password"] = password
        __props__["resource_group_name"] = resource_group_name
        __props__["size"] = size
        __props__["ssh_key"] = ssh_key
        __props__["storage_type"] = storage_type
        __props__["tags"] = tags
        __props__["unique_identifier"] = unique_identifier
        __props__["username"] = username
        return LinuxVirtualMachine(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

