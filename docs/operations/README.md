# Operations

This package contains no exporter or runtime endpoint. Install and configure a separate adapter,
then pass its exporter the detached snapshots defined by Core. The adapter owns initialization,
flush and shutdown behavior, network calls, retries, and operational health reporting.

## Prometheus exposition

For Prometheus, use `orbit-metrics-prometheus` and follow its endpoint guide. Exposition and an
ASGI `/metrics` route are opt-in. Decide whether the scrape endpoint is reachable only from the
trusted monitoring network, whether it needs authentication at the ingress, and how it behaves
during application startup and shutdown. Scrape endpoints can reveal application and infrastructure
details even when they expose no credentials.

## Metric correctness

Before enabling an exporter, verify how it maps each Core metric kind, names, labels, units, and
numeric values. Avoid label values derived from user IDs, request paths, exception messages, or
other unbounded input. High cardinality increases memory and backend cost and can make metrics
unavailable. Prefer bounded dimensions and put event-level detail in an appropriately protected
logs or traces system.

For pull exporters, test scrape concurrency, response limits, timeout behavior, and collection
overlap. For push exporters, test batching, bounded queues, backpressure, retries, duplicate sends,
flush deadlines, shutdown, and behavior while the backend is unavailable. This protocol does not
define delivery guarantees or a global timeout.

## Release checks

Test representative counter, gauge, and other supported sample forms; escaping and invalid text;
empty snapshots; large snapshots; repeated export; and concurrent export. Use a dedicated
non-production collector for integration checks. Protocol conformance and unit tests do not prove
that a remote backend received or interpreted samples correctly.
