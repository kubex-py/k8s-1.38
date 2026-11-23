from pydantic import Field

from kubex_core.models.base import BaseK8sModel


class RollingUpdateStatefulSetStrategy(BaseK8sModel):
    """RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType."""

    max_unavailable: int | str | None = Field(
        default=None,
        alias="maxUnavailable",
        description="maxUnavailable is the maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of pods in the update range (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0. Defaults to 1. This field is beta-level and is enabled by default. The field applies only to pods in the update range (ordinals greater than or equal to Partition, up to Replicas-1). Unavailable pods below Partition are not counted towards MaxUnavailable. When MaxUnavailable is a percentage, it is calculated from the number of pods in that update range (Replicas - Partition), not from all replicas. This setting might not be effective for the OrderedReady podManagementPolicy. That policy ensures pods are created and become ready one at a time.",
    )
    partition: int | None = Field(
        default=None,
        alias="partition",
        description="partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.",
    )
