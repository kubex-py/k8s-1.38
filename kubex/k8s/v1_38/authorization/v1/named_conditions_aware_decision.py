from pydantic import Field

from kubex.k8s.v1_38.authorization.v1.conditions_aware_decision import (
    ConditionsAwareDecision,
)
from kubex_core.models.base import BaseK8sModel


class NamedConditionsAwareDecision(BaseK8sModel):
    """NamedConditionsAwareDecision is a named ConditionsAwareDecision, returned by a unioned authorizer."""

    authorizer_name: str = Field(
        ...,
        alias="authorizerName",
        description="authorizerName details the name of the authorizer that authored the condition, such that the right Decision can be paired with the right authorizer when evaluating the conditions, even across API server replicas. The name must be stable over time. This name must be unique within a given union authorizer, not necessarily globally.",
    )
    decision: ConditionsAwareDecision = Field(
        ...,
        alias="decision",
        description="decision carries the inner decision returned from the authorizer.",
    )
