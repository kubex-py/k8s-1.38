from pydantic import Field

from kubex_core.models.base import BaseK8sModel


class SecurityProfileOCIBase(BaseK8sModel):
    """SecurityProfileOCIBase specifies the base profile of an OCI security profile."""

    localhost_profile: str | None = Field(
        default=None,
        alias="localhostProfile",
        description='localhostProfile indicates a base profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a non-empty descending path, relative to the kubelet\'s configured seccomp profile location, of at most 4096 characters. Must be set if type is "Localhost". Must NOT be set for any other type.',
    )
    type_: str = Field(
        ...,
        alias="type",
        description="type indicates which kind of base profile will be applied. Valid options are: Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used.",
    )
