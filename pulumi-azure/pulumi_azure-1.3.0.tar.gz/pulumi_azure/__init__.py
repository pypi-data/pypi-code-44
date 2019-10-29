# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import importlib
# Make subpackages available:
__all__ = ['ad', 'analysisservices', 'apimanagement', 'appinsights', 'appservice', 'authorization', 'automation', 'autoscale', 'batch', 'bot', 'cdn', 'cognitive', 'compute', 'config', 'containerservice', 'core', 'cosmosdb', 'dashboard', 'databricks', 'datafactory', 'datalake', 'ddosprotection', 'devspace', 'devtest', 'dns', 'eventgrid', 'eventhub', 'frontdoor', 'hdinsight', 'iot', 'keyvault', 'kusto', 'lb', 'loganalytics', 'logicapps', 'management', 'managementgroups', 'managementresource', 'maps', 'mariadb', 'marketplace', 'mediaservices', 'monitoring', 'msi', 'mssql', 'mysql', 'network', 'notificationhub', 'operationalinsights', 'policy', 'postgresql', 'privatedns', 'proximity', 'recoveryservices', 'redis', 'relay', 'role', 'scheduler', 'search', 'securitycenter', 'servicebus', 'servicefabric', 'signalr', 'sql', 'storage', 'streamanalytics', 'trafficmanager', 'waf']
for pkg in __all__:
    if pkg != 'config':
        importlib.import_module(f'{__name__}.{pkg}')

# Export this package's modules as members:
from .provider import *
