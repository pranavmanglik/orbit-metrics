# Architecture and contracts

## Responsibility

`orbit-metrics` defines a structural exporter protocol over Core's detached `MetricSnapshot`
values. Core owns instrument registration and snapshot creation. This package defines no metric
instruments, global provider, transport, registry, or exporter implementation.

```text
application instruments → orbit-core snapshot → MetricsExporter → optional adapter/transport
                                                    └─ e.g. orbit-metrics-prometheus
```

The application explicitly selects and wires an exporter. The `orbit-metrics-prometheus` package
implements Prometheus exposition and can optionally provide an ASGI `/metrics` endpoint; this
capability does not enable it automatically.

## Protocol behavior

`MetricsExporter.export()` receives a tuple of `MetricSnapshot` values and returns text in the
adapter's documented format. Implementations must not mutate snapshots, retain request-owned
state, or silently change metric names, kinds, values, units, or labels. They own serialization,
escaping, type mapping, output bounds, and any transport or registry lifecycle.

The protocol intentionally does not promise Prometheus text, OpenTelemetry semantics, batching,
remote write, pull versus push, retries, or persistent storage. An adapter should report unsupported
metric forms explicitly and sanitize failures before returning them to application code.

## Dependency direction

Applications depend on the capability and a chosen exporter adapter. The capability depends on
Core's snapshot contract; Core does not depend on this optional exporter interface. Keep vendor
SDKs, endpoint configuration, credentials, transport behavior, and exporter errors in the adapter
that owns them.
