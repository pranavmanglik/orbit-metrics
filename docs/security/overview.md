# Security

## Metric data

Metric names and labels can disclose internal architecture, tenant identifiers, user activity, or
business operations. Use bounded, reviewed labels and avoid credentials, access tokens, personal
data, request bodies, raw exception messages, and user-controlled values. Do not assume that a
metric is harmless because it is numeric; labels and names often carry the sensitive context.

This capability does not inspect or sanitize samples. An exporter must escape text according to
its output format and apply any destination-specific restrictions. Treat snapshot names, kinds,
labels, and values according to the Core contract and do not build unsafe exposition by string
concatenation.

## Endpoint and backend access

This package opens no network listener and defines no authentication or transport. The selected
adapter and deployment own authorization, TLS, credential storage, endpoint exposure, retention,
and network restrictions. Keep scrape or push endpoints on trusted paths, use least-privilege
credentials, verify TLS certificates, and avoid logging complete exported payloads.

## Vulnerability reporting

Report suspected vulnerabilities through the private process described in the repository
[security policy](../../SECURITY.md). Avoid posting exploit details publicly before maintainers can
assess the issue.
