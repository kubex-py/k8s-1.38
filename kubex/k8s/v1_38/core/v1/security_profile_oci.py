from pydantic import Field

from kubex.k8s.v1_38.core.v1.security_profile_oci_base import SecurityProfileOCIBase
from kubex_core.models.base import BaseK8sModel


class SecurityProfileOCI(BaseK8sModel):
    """SecurityProfileOCI references a security profile stored as an artifact in an OCI registry, with an optional base profile."""

    base_profile: SecurityProfileOCIBase | None = Field(
        default=None,
        alias="baseProfile",
        description="baseProfile optionally specifies the base profile that the container runtime merges with the OCI profile. The effective profile permits an operation only if both permit it. When omitted, the container runtime default profile is the base; a Localhost base profile takes its place.",
    )
    ref: str = Field(
        ...,
        alias="ref",
        description="ref is the OCI reference of the profile. It must be a digest-pinned reference in canonical form, registry/repository@<algorithm>:<digest>, with the registry spelled out (for example docker.io/library/profile, not profile or docker.io/profile). Tags are rejected. The digest algorithm must be sha256, sha384, or sha512. The maximum length is 1024 characters. Pull secrets are assembled in the same way as for the container image by looking up node credentials, service account image pull secrets, and pod spec image pull secrets.",
    )
