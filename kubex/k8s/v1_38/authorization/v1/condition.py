from pydantic import Field

from kubex_core.models.base import BaseK8sModel


class Condition(BaseK8sModel):
    """Condition represents a single authorization condition to be evaluated against data available later in the request chain, e.g. objects available in admission."""

    condition: str | None = Field(
        default=None,
        alias="condition",
        description="condition returns a string encoding of the condition to be evaluated. It is a pure, deterministic function from ConditionsData to a boolean (or error). Might or might not be human-readable. Optional, if the ID alone is enough for the authorizer to know how to evaluate the condition.",
    )
    description: str | None = Field(
        default=None,
        alias="description",
        description="description is an optional human-friendly description that can be shown as an error message or for debugging. Optional.",
    )
    id: str = Field(
        ...,
        alias="id",
        description="id uniquely identifies this condition within the scope of the authorizer that authored it and ConditionsMap it is part of. Validated as a Kubernetes label key. Any domain of form *.k8s.io or *.kubernetes.io is reserved for Kubernetes use.",
    )
    type_: str | None = Field(
        default=None,
        alias="type",
        description="type describes the type of the condition, if there are multiple possibilities. Should be formatted as a Kubernetes label key. Any domain of form *.k8s.io or *.kubernetes.io is reserved for Kubernetes use. authorizer.kubernetes.io/cel is a conditions type for CEL, handled by kube-apiserver. Optional. Can be omitted if the authorizer already knows how to evaluate the condition.",
    )
