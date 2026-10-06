# Orbit Metrics: architecture and boundaries

## Responsibility

`orbit-metrics` defines the provider-independent exporter contract for Orbit Core metric
snapshots. It does not collect metric data itself: Core owns bounded instruments and snapshots,
while adapters implement this interface to expose or transport them. The distribution requires
Python 3.11 through 3.14 and is currently pre-alpha.

## Declared dependencies

The following dependency declarations come from the checked-in manifests. Optional groups and development dependencies are called out separately.

### `pyproject.toml`
- `orbit-core>=0.1.0a1,<0.2`
- Optional `dev` group: `pytest>=8,<10`, `ruff>=0.8,<1`, `mypy>=1.13,<2`.

Declared dependencies do not mean that optional providers or services are bundled with this package.

## Implementation layout

Representative implementation files in this checkout:

- `src/orbit_metrics/__init__.py`
- `src/orbit_metrics/contracts.py`

## Public contract and scope

The README does not contain a separately headed architecture section. Its responsibility statement above and the public source files define the implemented scope; this guide adds no behavior beyond that description.

## Boundary rules

Keep provider SDKs, credentials, transports, and provider-specific error translation in provider adapters. Keep reusable capability contracts in the matching capability package and lifecycle orchestration in Core. Apply the relevant layer for this repository and preserve the dependency direction shown above.
