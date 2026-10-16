# Orbit Metrics

`orbit-metrics` defines the provider-independent exporter contract for Orbit Core metric
snapshots. It does not collect metric data itself: Core owns bounded instruments and snapshots,
while adapters implement this interface to expose or transport them. The distribution requires
Python 3.11 through 3.14 and is currently alpha.

## Implementing an exporter

Install the capability and Core's snapshot models:

```bash
python -m pip install orbit-core orbit-metrics
```

An exporter accepts a tuple of detached, immutable Core `MetricSnapshot` values. It returns its
own encoded representation and must not mutate snapshots or retain application-owned mutable
state:

```python
from orbit.diagnostics import MetricSnapshot
from orbit_metrics import MetricsExporter


class TextExporter:
    def export(self, snapshots: tuple[MetricSnapshot, ...]) -> str:
        return "\n".join(f"{item.name} {item.value}" for item in snapshots)


assert isinstance(TextExporter(), MetricsExporter)
```

This example illustrates the protocol only; production exporters must correctly encode their
target format and enforce appropriate output and cardinality bounds. The separate `orbit-metrics-prometheus`
package implements Prometheus text exposition and can optionally contribute a `/metrics` route.
Neither this capability nor Core enables an exporter automatically.

The contract does not choose a telemetry vendor, network transport, scrape policy, batching,
retention, or remote-write behavior. Those belong to separately installed adapters.

## Documentation

The package-specific guides cover [architecture](docs/architecture/overview.md), [operations and security](docs/operations/README.md), and [development](docs/development/README.md), with [security guidance](docs/security/overview.md). The [documentation index](docs/README.md) links to the full package overview and project policies.

## Development

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
mypy
```

Licensed under Apache-2.0.

