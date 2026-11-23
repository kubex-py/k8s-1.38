from pydantic import Field

from kubex.k8s.v1_38.scheduling.v1.workload_topology_constraint import (
    WorkloadTopologyConstraint,
)
from kubex_core.models.base import BaseK8sModel


class WorkloadPodGroupSchedulingConstraints(BaseK8sModel):
    """WorkloadPodGroupSchedulingConstraints defines leaf-level scheduling constraints, such as topology."""

    topology: list[WorkloadTopologyConstraint] | None = Field(
        default=None,
        alias="topology",
        description="topology specifies desired topological placements for all pods within the pod group. If unset, no topology placement is requested.",
    )
