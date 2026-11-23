from pydantic import Field

from kubex.k8s.v1_38.core.v1.resource_claim import ResourceClaim
from kubex_core.models.base import BaseK8sModel
from kubex_core.models.types import Quantity


class ResourceRequirements(BaseK8sModel):
    """ResourceRequirements describes the compute resource requirements."""

    claims: list[ResourceClaim] | None = Field(
        default=None,
        alias="claims",
        description="claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. This field is immutable. It can only be set for containers.",
    )
    limits: dict[str, Quantity] | None = Field(
        default=None,
        alias="limits",
        description="limits describes the maximum amount of compute resources allowed. For kubelet cgroup enforcement: - cpu and memory: a limit of 0 is treated the same as an unspecified limit. If neither the container nor the pod specifies a limit, the resource is not limited. - hugepages: an unspecified limit is treated the same as a limit of 0. More details: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/",
    )
    requests: dict[str, Quantity] | None = Field(
        default=None,
        alias="requests",
        description="requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/",
    )
