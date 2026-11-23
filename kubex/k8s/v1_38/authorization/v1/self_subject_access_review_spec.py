from pydantic import Field

from kubex.k8s.v1_38.authorization.v1.authorization_options import AuthorizationOptions
from kubex.k8s.v1_38.authorization.v1.non_resource_attributes import (
    NonResourceAttributes,
)
from kubex.k8s.v1_38.authorization.v1.resource_attributes import ResourceAttributes
from kubex_core.models.base import BaseK8sModel


class SelfSubjectAccessReviewSpec(BaseK8sModel):
    """SelfSubjectAccessReviewSpec is a description of the access request. Exactly one of resourceAttributes and nonResourceAttributes must be set"""

    authorization_options: AuthorizationOptions | None = Field(
        default=None,
        alias="authorizationOptions",
        description="authorizationOptions contains options for specifying the client's authorization abilities. If unset, only unconditional authorization is supported, for backwards-compatibility. Requires the ConditionalAuthorization feature to be enabled.",
    )
    non_resource_attributes: NonResourceAttributes | None = Field(
        default=None,
        alias="nonResourceAttributes",
        description="nonResourceAttributes describes information for a non-resource access request",
    )
    resource_attributes: ResourceAttributes | None = Field(
        default=None,
        alias="resourceAttributes",
        description="resourceAttributes describes information for a resource access request",
    )
