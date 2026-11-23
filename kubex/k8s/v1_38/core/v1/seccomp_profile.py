from pydantic import Field

from kubex.k8s.v1_38.core.v1.security_profile_oci import SecurityProfileOCI
from kubex_core.models.base import BaseK8sModel


class SeccompProfile(BaseK8sModel):
    """SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set."""

    localhost_profile: str | None = Field(
        default=None,
        alias="localhostProfile",
        description='localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet\'s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.',
    )
    oci: SecurityProfileOCI | None = Field(
        default=None,
        alias="oci",
        description='oci specifies a seccomp profile stored as an artifact in an OCI registry. The container runtime merges the profile with a base profile, so the effective profile permits an operation only if both permit it. Must be set if type is "OCI". Must NOT be set for any other type. This is an alpha field and requires enabling the SecurityProfileOCI feature gate.',
    )
    type_: str = Field(
        ...,
        alias="type",
        description="type indicates which kind of seccomp profile will be applied. Valid options are: Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied. OCI - a profile pulled from an OCI registry should be used, merged with a base profile (see oci.baseProfile). Privileged containers cannot use it, whether it is set on the container or inherited from the pod. This is an alpha value and requires enabling the SecurityProfileOCI feature gate.",
    )
