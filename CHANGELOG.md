# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Until 0.1.0-alpha.2 the package was developed in the [kubex](https://github.com/kubex-py/kubex)
repository and released together with kubex; the notes for those releases are this package's
part of kubex's changelog.

## [Unreleased]

## [0.1.0-alpha.3] - 2026-11-23

### Added

- The `Programming Language :: Python :: Free Threading :: 2 - Beta` classifier: the models work on
  free-threaded Python 3.14t and 3.15t.
- New models from the 1.38 beta spec: `CompositePodGroup` (`scheduling.k8s.io/v1beta1`) with its
  list, spec and status; `WorkloadTopologyConstraint` (`scheduling.k8s.io/v1`); the authorization
  condition types `AuthorizationOptions`, `Condition`, `ConditionsAwareDecision`, `ConditionsMap`,
  `NamedConditionsAwareDecision` and `UnconditionalDecision`; `SecurityProfileOCI` and
  `SecurityProfileOCIBase`.

### Changed

- Regenerated from the Kubernetes v1.38.0-beta.0 spec with
  [kubex-codegen](https://github.com/kubex-py/kubex-codegen) v0.2.0; 0.1.0-alpha.2 came from an
  earlier 1.38 pre-release. 58 models change, most in `core/v1`, `autoscaling/v2` and `resource`.
- **Breaking:** The `WorkloadPodGroup*` models moved from `scheduling.k8s.io/v1alpha3` to
  `scheduling.k8s.io/v1` (`kubex.k8s.v1_38.scheduling.v1`).
- The package moved to its own repository, [kubex-py/k8s-1.38](https://github.com/kubex-py/k8s-1.38),
  with its history. `pyproject.toml` and `LICENSE` are maintained by hand; `pyproject.toml` has
  project URLs for the new repository.

## [0.1.0-alpha.2] - 2026-10-28

### Added

- The distribution includes the MIT `LICENSE` file.
- The `Framework :: Pydantic :: 2` and `Typing :: Typed` classifiers.

### Fixed

- Spec-required list, map and timestamp fields accept `null` (EndpointSlice, CSINode and
  events.k8s.io Event lists).
- `CustomResourceDefinition` schema fields (`default`, `enum`, `items`, `additionalProperties`).
- `Quantity` fields accept numbers.
- The package requires `kubex-core>=0.1.0b4,<0.2` (it accepted any `kubex-core` before).

### Changed

- **Breaking:** Timestamp fields are typed `Time`/`MicroTime` and resource quantities `Quantity`
  (from `kubex_core.models.types`) instead of `datetime` and `str`.
- **Breaking:** Spec-required `Time`/`MicroTime`/byte fields are typed `T | None`. The `JSON`,
  `JSONSchemaPropsOr*`, `ManagedFieldsEntry` and `ShardInfo` modules are removed;
  `ManagedFieldsEntry` and `ShardInfo` live in `kubex_core.models.metadata`.

## [0.1.0-alpha.1] - 2026-10-23

First release, together with kubex 0.1.0-beta.3: preliminary models for Kubernetes 1.38,
generated from a pre-release spec.

[unreleased]: https://github.com/kubex-py/k8s-1.38/compare/v0.1.0-alpha.3...HEAD
[0.1.0-alpha.3]: https://github.com/kubex-py/k8s-1.38/compare/v0.1.0-alpha.2...v0.1.0-alpha.3
[0.1.0-alpha.2]: https://github.com/kubex-py/k8s-1.38/compare/v0.1.0-alpha.1...v0.1.0-alpha.2
[0.1.0-alpha.1]: https://github.com/kubex-py/k8s-1.38/releases/tag/v0.1.0-alpha.1
