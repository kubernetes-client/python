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


class V1alpha3DeviceAllocationConfiguration(object):
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
        'opaque': 'V1alpha3OpaqueDeviceConfiguration',
        'requests': 'list[str]',
        'source': 'str'
    }

    attribute_map = {
        'opaque': 'opaque',
        'requests': 'requests',
        'source': 'source'
    }

    def __init__(self, opaque=None, requests=None, source=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha3DeviceAllocationConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opaque = None
        self._requests = None
        self._source = None
        self.discriminator = None

        if opaque is not None:
            self.opaque = opaque
        if requests is not None:
            self.requests = requests
        self.source = source

    @property
    def opaque(self):
        """Gets the opaque of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501


        :return: The opaque of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501
        :rtype: V1alpha3OpaqueDeviceConfiguration
        """
        return self._opaque

    @opaque.setter
    def opaque(self, opaque):
        """Sets the opaque of this V1alpha3DeviceAllocationConfiguration.


        :param opaque: The opaque of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501
        :type: V1alpha3OpaqueDeviceConfiguration
        """

        self._opaque = opaque

    @property
    def requests(self):
        """Gets the requests of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501

        Requests lists the names of requests where the configuration applies. If empty, its applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the configuration applies to all subrequests.  # noqa: E501

        :return: The requests of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this V1alpha3DeviceAllocationConfiguration.

        Requests lists the names of requests where the configuration applies. If empty, its applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the configuration applies to all subrequests.  # noqa: E501

        :param requests: The requests of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._requests = requests

    @property
    def source(self):
        """Gets the source of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501

        Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim.  # noqa: E501

        :return: The source of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1alpha3DeviceAllocationConfiguration.

        Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim.  # noqa: E501

        :param source: The source of this V1alpha3DeviceAllocationConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

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
        if not isinstance(other, V1alpha3DeviceAllocationConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha3DeviceAllocationConfiguration):
            return True

        return self.to_dict() != other.to_dict()
