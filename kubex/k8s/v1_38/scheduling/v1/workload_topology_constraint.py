from pydantic import Field

from kubex_core.models.base import BaseK8sModel


class WorkloadTopologyConstraint(BaseK8sModel):
    """WorkloadTopologyConstraint defines a topology constraint for a group of pods managed by a workload controller."""

    key: str = Field(
        ...,
        alias="key",
        description='key specifies the key of the node label representing the topology domain. All pods within the PodGroup (or CompositePodGroup) must be colocated within the same domain instance. Different groups can land on different domain instances even if they derive from the same template. Nodes where this label is missing or has an empty value do not belong to any domain instance, so pods within the PodGroup/CompositePodGroup cannot be scheduled onto them. Examples: "topology.kubernetes.io/rack"',
    )
