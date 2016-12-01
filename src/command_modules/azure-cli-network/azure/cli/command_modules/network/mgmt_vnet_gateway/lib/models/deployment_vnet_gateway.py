# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
#pylint: skip-file

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentVnetGateway(Model):
    """Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateVnetGateway_2016-11-29/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :param enable_bgp: Enable BGP (Border Gateway Protocol). Default value:
     False .
    :type enable_bgp: bool
    :param gateway_type: Gateway type. Possible values include: 'Vpn',
     'ExpressRoute'. Default value: "Vpn" .
    :type gateway_type: str or :class:`gatewayType
     <Default.models.gatewayType>`
    :param location: Location for resources.
    :type location: str
    :param public_ip_address: Name or ID of public IP address to use.
    :type public_ip_address: str
    :param public_ip_address_type: Type of Public IP Address to associate
     with the VPN gateway. Possible values include: 'existingName',
     'existingId'. Default value: "existingId" .
    :type public_ip_address_type: str or :class:`publicIpAddressType
     <Default.models.publicIpAddressType>`
    :param sku: VPN Gateway SKU. Possible values include: 'Basic',
     'Standard', 'HighPerformance'. Default value: "Basic" .
    :type sku: str or :class:`sku <Default.models.sku>`
    :param tags: Tags object.
    :type tags: object
    :param virtual_network: Name or ID of a virtual network that contains a
     subnet named 'GatewaySubnet'.
    :type virtual_network: str
    :param virtual_network_gateway_name: Gateway name.
    :type virtual_network_gateway_name: str
    :param virtual_network_type: Type of virtual network to supply to the VPN
     gateway. Possible values include: 'existingId', 'existingName'. Default
     value: "existingId" .
    :type virtual_network_type: str or :class:`virtualNetworkType
     <Default.models.virtualNetworkType>`
    :param vpn_type: VPN gateway type. Possible values include: 'RouteBased',
     'PolicyBased'. Default value: "RouteBased" .
    :type vpn_type: str or :class:`vpnType <Default.models.vpnType>`
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        'enable_bgp': {'required': True},
        'public_ip_address': {'required': True},
        'virtual_network': {'required': True},
        'virtual_network_gateway_name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'enable_bgp': {'key': 'properties.parameters.enableBgp.value', 'type': 'bool'},
        'gateway_type': {'key': 'properties.parameters.gatewayType.value', 'type': 'gatewayType'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'public_ip_address': {'key': 'properties.parameters.publicIpAddress.value', 'type': 'str'},
        'public_ip_address_type': {'key': 'properties.parameters.publicIpAddressType.value', 'type': 'publicIpAddressType'},
        'sku': {'key': 'properties.parameters.sku.value', 'type': 'sku'},
        'tags': {'key': 'properties.parameters.tags.value', 'type': 'object'},
        'virtual_network': {'key': 'properties.parameters.virtualNetwork.value', 'type': 'str'},
        'virtual_network_gateway_name': {'key': 'properties.parameters.virtualNetworkGatewayName.value', 'type': 'str'},
        'virtual_network_type': {'key': 'properties.parameters.virtualNetworkType.value', 'type': 'virtualNetworkType'},
        'vpn_type': {'key': 'properties.parameters.vpnType.value', 'type': 'vpnType'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateVnetGateway_2016-11-29/azuredeploy.json"

    mode = "Incremental"

    def __init__(self, public_ip_address, virtual_network, virtual_network_gateway_name, content_version=None, enable_bgp=False, gateway_type="Vpn", location=None, public_ip_address_type="existingId", sku="Basic", tags=None, virtual_network_type="existingId", vpn_type="RouteBased"):
        self.content_version = content_version
        self.enable_bgp = enable_bgp
        self.gateway_type = gateway_type
        self.location = location
        self.public_ip_address = public_ip_address
        self.public_ip_address_type = public_ip_address_type
        self.sku = sku
        self.tags = tags
        self.virtual_network = virtual_network
        self.virtual_network_gateway_name = virtual_network_gateway_name
        self.virtual_network_type = virtual_network_type
        self.vpn_type = vpn_type
