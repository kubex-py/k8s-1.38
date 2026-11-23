from pydantic import Field

from kubex_core.models.base import BaseK8sModel
from kubex_core.models.types import NullAsEmptyList


class AuthorizationOptions(BaseK8sModel):
    """AuthorizationOptions contains options for specifying the client's authorization abilities."""

    handled_decision_types: NullAsEmptyList[str] = Field(
        ...,
        alias="handledDecisionTypes",
        description='handledDecisionTypes specifies what decision types the client can handle in the context it is in. Currently valid values are: - [Allow, Deny, NoOpinion] (for conditions-unaware clients) or - [Allow, Deny, NoOpinion, ConditionsMap, Union, ...] (for conditions-aware clients) If the authorizer would like to return conditions, but the client does not opt in to handle those here, the authorizer must fail closed to a safe unconditional decision (Deny if any Deny conditions were present, otherwise NoOpinion). Order does not matter in this slice; set semantics should be used. The server does not reject unrecognized decision types, but focuses on whether the client supports a mode that the server does. All clients must support "classic", conditions-unaware authorization.',
    )
