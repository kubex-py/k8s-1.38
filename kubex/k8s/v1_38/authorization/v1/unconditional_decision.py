from pydantic import Field

from kubex_core.models.base import BaseK8sModel


class UnconditionalDecision(BaseK8sModel):
    """UnconditionalDecision represents the data associated with an unconditional decision."""

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
