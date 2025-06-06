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


class V2HorizontalPodAutoscalerSpec(object):
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
        'behavior': 'V2HorizontalPodAutoscalerBehavior',
        'max_replicas': 'int',
        'metrics': 'list[V2MetricSpec]',
        'min_replicas': 'int',
        'scale_target_ref': 'V2CrossVersionObjectReference'
    }

    attribute_map = {
        'behavior': 'behavior',
        'max_replicas': 'maxReplicas',
        'metrics': 'metrics',
        'min_replicas': 'minReplicas',
        'scale_target_ref': 'scaleTargetRef'
    }

    def __init__(self, behavior=None, max_replicas=None, metrics=None, min_replicas=None, scale_target_ref=None, local_vars_configuration=None):  # noqa: E501
        """V2HorizontalPodAutoscalerSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._behavior = None
        self._max_replicas = None
        self._metrics = None
        self._min_replicas = None
        self._scale_target_ref = None
        self.discriminator = None

        if behavior is not None:
            self.behavior = behavior
        self.max_replicas = max_replicas
        if metrics is not None:
            self.metrics = metrics
        if min_replicas is not None:
            self.min_replicas = min_replicas
        self.scale_target_ref = scale_target_ref

    @property
    def behavior(self):
        """Gets the behavior of this V2HorizontalPodAutoscalerSpec.  # noqa: E501


        :return: The behavior of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: V2HorizontalPodAutoscalerBehavior
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this V2HorizontalPodAutoscalerSpec.


        :param behavior: The behavior of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: V2HorizontalPodAutoscalerBehavior
        """

        self._behavior = behavior

    @property
    def max_replicas(self):
        """Gets the max_replicas of this V2HorizontalPodAutoscalerSpec.  # noqa: E501

        maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.  # noqa: E501

        :return: The max_replicas of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this V2HorizontalPodAutoscalerSpec.

        maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.  # noqa: E501

        :param max_replicas: The max_replicas of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `max_replicas`, must not be `None`")  # noqa: E501

        self._max_replicas = max_replicas

    @property
    def metrics(self):
        """Gets the metrics of this V2HorizontalPodAutoscalerSpec.  # noqa: E501

        metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization.  # noqa: E501

        :return: The metrics of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: list[V2MetricSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this V2HorizontalPodAutoscalerSpec.

        metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization.  # noqa: E501

        :param metrics: The metrics of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: list[V2MetricSpec]
        """

        self._metrics = metrics

    @property
    def min_replicas(self):
        """Gets the min_replicas of this V2HorizontalPodAutoscalerSpec.  # noqa: E501

        minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.  # noqa: E501

        :return: The min_replicas of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this V2HorizontalPodAutoscalerSpec.

        minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.  # noqa: E501

        :param min_replicas: The min_replicas of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def scale_target_ref(self):
        """Gets the scale_target_ref of this V2HorizontalPodAutoscalerSpec.  # noqa: E501


        :return: The scale_target_ref of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :rtype: V2CrossVersionObjectReference
        """
        return self._scale_target_ref

    @scale_target_ref.setter
    def scale_target_ref(self, scale_target_ref):
        """Sets the scale_target_ref of this V2HorizontalPodAutoscalerSpec.


        :param scale_target_ref: The scale_target_ref of this V2HorizontalPodAutoscalerSpec.  # noqa: E501
        :type: V2CrossVersionObjectReference
        """
        if self.local_vars_configuration.client_side_validation and scale_target_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `scale_target_ref`, must not be `None`")  # noqa: E501

        self._scale_target_ref = scale_target_ref

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
        if not isinstance(other, V2HorizontalPodAutoscalerSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2HorizontalPodAutoscalerSpec):
            return True

        return self.to_dict() != other.to_dict()
