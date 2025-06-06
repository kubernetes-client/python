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


class V1beta1DeviceAllocationResult(object):
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
        'config': 'list[V1beta1DeviceAllocationConfiguration]',
        'results': 'list[V1beta1DeviceRequestAllocationResult]'
    }

    attribute_map = {
        'config': 'config',
        'results': 'results'
    }

    def __init__(self, config=None, results=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1DeviceAllocationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._results = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if results is not None:
            self.results = results

    @property
    def config(self):
        """Gets the config of this V1beta1DeviceAllocationResult.  # noqa: E501

        This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.  This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.  # noqa: E501

        :return: The config of this V1beta1DeviceAllocationResult.  # noqa: E501
        :rtype: list[V1beta1DeviceAllocationConfiguration]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this V1beta1DeviceAllocationResult.

        This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.  This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.  # noqa: E501

        :param config: The config of this V1beta1DeviceAllocationResult.  # noqa: E501
        :type: list[V1beta1DeviceAllocationConfiguration]
        """

        self._config = config

    @property
    def results(self):
        """Gets the results of this V1beta1DeviceAllocationResult.  # noqa: E501

        Results lists all allocated devices.  # noqa: E501

        :return: The results of this V1beta1DeviceAllocationResult.  # noqa: E501
        :rtype: list[V1beta1DeviceRequestAllocationResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this V1beta1DeviceAllocationResult.

        Results lists all allocated devices.  # noqa: E501

        :param results: The results of this V1beta1DeviceAllocationResult.  # noqa: E501
        :type: list[V1beta1DeviceRequestAllocationResult]
        """

        self._results = results

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
        if not isinstance(other, V1beta1DeviceAllocationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1DeviceAllocationResult):
            return True

        return self.to_dict() != other.to_dict()
