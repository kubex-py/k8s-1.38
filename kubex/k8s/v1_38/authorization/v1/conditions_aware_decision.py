from pydantic import Field

from kubex.k8s.v1_38.authorization.v1.conditions_map import ConditionsMap
from kubex.k8s.v1_38.authorization.v1.named_conditions_aware_decision import (
    NamedConditionsAwareDecision,
)
from kubex.k8s.v1_38.authorization.v1.unconditional_decision import (
    UnconditionalDecision,
)
from kubex_core.models.base import BaseK8sModel


class ConditionsAwareDecision(BaseK8sModel):
    """ConditionsAwareDecision represents one authorizer's decision. It is an enum type, with variants described in ConditionsAwareDecisionType, plus a reason and error."""

    allow: UnconditionalDecision | None = Field(
        default=None,
        alias="allow",
        description='allow represents an unconditional Allow decision. Must be non-null when type == "Allow", otherwise this field must be unset.',
    )
    conditions_map: ConditionsMap | None = Field(
        default=None,
        alias="conditionsMap",
        description='conditionsMap represents a conditional decision, modelled as a map of conditions. Must be non-null when type == "ConditionsMap", otherwise this field must be unset.',
    )
    deny: UnconditionalDecision | None = Field(
        default=None,
        alias="deny",
        description='deny represents an unconditional Deny decision. Must be non-null when type == "Deny", otherwise this field must be unset.',
    )
    no_opinion: UnconditionalDecision | None = Field(
        default=None,
        alias="noOpinion",
        description='noOpinion represents an unconditional NoOpinion decision. Must be non-null when type == "NoOpinion", otherwise this field must be unset.',
    )
    type_: str = Field(
        ...,
        alias="type",
        description="type describes the type of the decision, and acts as an enum discriminator.",
    )
    union: list[NamedConditionsAwareDecision] | None = Field(
        default=None,
        alias="union",
        description='union forms an ordered tree of decisions, where the union decision is represented by an internal node, and all other decision types are leaf nodes. During evaluation, the leaf decisions are evaluated in depth-first order, until an Allow or Deny decision is found. The order of the decisions should match the order of the authorizers in the union authorizer for interpretability, but the authorizerName is the map key. At least one of the leaves must be of type ConditionsMap, as otherwise the union could be trivially reduced to just a single Allow/Deny/NoOpinion. Must have at least one element when type == "Union", otherwise this field must be unset.',
    )
