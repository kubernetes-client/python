# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.33
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1ServiceCIDRSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cidrs': 'list[str]'
    }

    attribute_map = {
        'cidrs': 'cidrs'
    }

    def __init__(self, cidrs=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1ServiceCIDRSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cidrs = None
        self.discriminator = None

        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def cidrs(self):
        """Gets the cidrs of this V1beta1ServiceCIDRSpec.  # noqa: E501

        CIDRs defines the IP blocks in CIDR notation (e.g. \"192.168.0.0/24\" or \"2001:db8::/64\") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.  # noqa: E501

        :return: The cidrs of this V1beta1ServiceCIDRSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this V1beta1ServiceCIDRSpec.

        CIDRs defines the IP blocks in CIDR notation (e.g. \"192.168.0.0/24\" or \"2001:db8::/64\") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.  # noqa: E501

        :param cidrs: The cidrs of this V1beta1ServiceCIDRSpec.  # noqa: E501
        :type: list[str]
        """

        self._cidrs = cidrs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1ServiceCIDRSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1ServiceCIDRSpec):
            return True

        return self.to_dict() != other.to_dict()
