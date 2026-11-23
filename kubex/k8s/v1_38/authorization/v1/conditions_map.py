from pydantic import Field

from kubex.k8s.v1_38.authorization.v1.condition import Condition
from kubex_core.models.base import BaseK8sModel


class ConditionsMap(BaseK8sModel):
    """ConditionsMap represents a map of conditions, keyed by ID across all conditions, across all effects. The ConditionsMap must have at least one Allow condition or at least one Deny condition. It cannot contain more than 128 conditions in total. The conditions are evaluated against data available later, to determine whether the authorizer that authored the conditions allows or denies the request. If all conditions in the map evaluate to false, the final decision must be NoOpinion."""

    allow_conditions: list[Condition] | None = Field(
        default=None,
        alias="allowConditions",
        description="allowConditions contains the conditions with Allow effect. If any such condition evaluates to true, the ConditionsMap as a whole must evaluate to Allow.",
    )
    deny_conditions: list[Condition] | None = Field(
        default=None,
        alias="denyConditions",
        description="denyConditions contains the conditions with Deny effect. If any such condition evaluates to true or error, the ConditionsMap as a whole must evaluate to Deny.",
    )
    no_opinion_conditions: list[Condition] | None = Field(
        default=None,
        alias="noOpinionConditions",
        description="noOpinionConditions contains the conditions with NoOpinion effect. If any such condition evaluates to true or error, the ConditionsMap as a whole must evaluate to NoOpinion.",
    )
