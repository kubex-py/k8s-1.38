from pydantic import Field

from kubex.k8s.v1_38.authorization.v1.conditions_aware_decision import (
    ConditionsAwareDecision,
)
from kubex_core.models.base import BaseK8sModel


class SubjectAccessReviewStatus(BaseK8sModel):
    """SubjectAccessReviewStatus"""

    allowed: bool | None = Field(
        default=None,
        alias="allowed",
        description="allowed is true if the action would be allowed, false otherwise. allowed=true is mutually exclusive with denied=true and conditionalDecision != nil.",
    )
    conditional_decision: ConditionsAwareDecision | None = Field(
        default=None,
        alias="conditionalDecision",
        description="conditionalDecision represents a conditional decision returned by the authorizer. When conditionalDecision is set, allowed, denied, reason and evaluationError must have their zero values. The top-level decision type should be ConditionsAwareDecisionTypeConditionsMap or ConditionsAwareDecisionTypeUnion, as Allow/Deny/NoOpinion decisions can be represented with SubjectAccessReviewStatus.Allowed and SubjectAccessReviewStatus.Denied alone. May only be set if spec.authorizationOptions.handledDecisionTypes includes `ConditionsMap` and `Union`. Requires the ConditionalAuthorization feature to be enabled.",
    )
    denied: bool | None = Field(
        default=None,
        alias="denied",
        description="denied is optional. True if the action would be denied, otherwise false If allowed is false, denied is false, and conditionalDecision is unset, then the authorizer has no opinion on whether to authorize the action. denied=true is mutually exclusive with allowed=true and conditionalDecision != nil.",
    )
    evaluation_error: str | None = Field(
        default=None,
        alias="evaluationError",
        description="evaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.",
    )
    reason: str | None = Field(
        default=None,
        alias="reason",
        description="reason is optional. It indicates why a request was allowed or denied.",
    )
