# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NetworkPacketCapture(pulumi.CustomResource):
    filters: pulumi.Output[list]
    """
    One or more `filter` blocks as defined below. Changing this forces a new resource to be created.
    
      * `localIpAddress` (`str`)
      * `localPort` (`str`)
      * `protocol` (`str`)
      * `remoteIpAddress` (`str`)
      * `remotePort` (`str`)
    """
    maximum_bytes_per_packet: pulumi.Output[float]
    """
    The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.
    """
    maximum_bytes_per_session: pulumi.Output[float]
    """
    Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.
    """
    maximum_capture_duration: pulumi.Output[float]
    """
    The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name to use for this Network Packet Capture. Changing this forces a new resource to be created.
    """
    network_watcher_name: pulumi.Output[str]
    """
    The name of the Network Watcher. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.
    """
    storage_location: pulumi.Output[dict]
    """
    A `storage_location` block as defined below. Changing this forces a new resource to be created.
    
      * `filePath` (`str`)
      * `storage_account_id` (`str`)
      * `storagePath` (`str`) - The URI of the storage path to save the packet capture.
    """
    target_resource_id: pulumi.Output[str]
    """
    The ID of the Resource to capture packets from. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, filters=None, maximum_bytes_per_packet=None, maximum_bytes_per_session=None, maximum_capture_duration=None, name=None, network_watcher_name=None, resource_group_name=None, storage_location=None, target_resource_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Configures Network Packet Capturing against a Virtual Machine using a Network Watcher.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] filters: One or more `filter` blocks as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[float] maximum_bytes_per_packet: The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.
        :param pulumi.Input[float] maximum_bytes_per_session: Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.
        :param pulumi.Input[float] maximum_capture_duration: The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name to use for this Network Packet Capture. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] storage_location: A `storage_location` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the Resource to capture packets from. Changing this forces a new resource to be created.
        
        The **filters** object supports the following:
        
          * `localIpAddress` (`pulumi.Input[str]`)
          * `localPort` (`pulumi.Input[str]`)
          * `protocol` (`pulumi.Input[str]`)
          * `remoteIpAddress` (`pulumi.Input[str]`)
          * `remotePort` (`pulumi.Input[str]`)
        
        The **storage_location** object supports the following:
        
          * `filePath` (`pulumi.Input[str]`)
          * `storage_account_id` (`pulumi.Input[str]`)
          * `storagePath` (`pulumi.Input[str]`) - The URI of the storage path to save the packet capture.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_packet_capture.html.markdown.
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

            __props__['filters'] = filters
            __props__['maximum_bytes_per_packet'] = maximum_bytes_per_packet
            __props__['maximum_bytes_per_session'] = maximum_bytes_per_session
            __props__['maximum_capture_duration'] = maximum_capture_duration
            __props__['name'] = name
            if network_watcher_name is None:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__['network_watcher_name'] = network_watcher_name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if storage_location is None:
                raise TypeError("Missing required property 'storage_location'")
            __props__['storage_location'] = storage_location
            if target_resource_id is None:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__['target_resource_id'] = target_resource_id
        super(NetworkPacketCapture, __self__).__init__(
            'azure:network/networkPacketCapture:NetworkPacketCapture',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, filters=None, maximum_bytes_per_packet=None, maximum_bytes_per_session=None, maximum_capture_duration=None, name=None, network_watcher_name=None, resource_group_name=None, storage_location=None, target_resource_id=None):
        """
        Get an existing NetworkPacketCapture resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] filters: One or more `filter` blocks as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[float] maximum_bytes_per_packet: The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.
        :param pulumi.Input[float] maximum_bytes_per_session: Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.
        :param pulumi.Input[float] maximum_capture_duration: The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name to use for this Network Packet Capture. Changing this forces a new resource to be created.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] storage_location: A `storage_location` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the Resource to capture packets from. Changing this forces a new resource to be created.
        
        The **filters** object supports the following:
        
          * `localIpAddress` (`pulumi.Input[str]`)
          * `localPort` (`pulumi.Input[str]`)
          * `protocol` (`pulumi.Input[str]`)
          * `remoteIpAddress` (`pulumi.Input[str]`)
          * `remotePort` (`pulumi.Input[str]`)
        
        The **storage_location** object supports the following:
        
          * `filePath` (`pulumi.Input[str]`)
          * `storage_account_id` (`pulumi.Input[str]`)
          * `storagePath` (`pulumi.Input[str]`) - The URI of the storage path to save the packet capture.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_packet_capture.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["filters"] = filters
        __props__["maximum_bytes_per_packet"] = maximum_bytes_per_packet
        __props__["maximum_bytes_per_session"] = maximum_bytes_per_session
        __props__["maximum_capture_duration"] = maximum_capture_duration
        __props__["name"] = name
        __props__["network_watcher_name"] = network_watcher_name
        __props__["resource_group_name"] = resource_group_name
        __props__["storage_location"] = storage_location
        __props__["target_resource_id"] = target_resource_id
        return NetworkPacketCapture(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

