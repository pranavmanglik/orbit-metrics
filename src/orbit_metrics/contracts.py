# Copyright 2026-present Orbit Contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Stable capability contracts shared by metrics exporter adapters."""

from typing import Protocol, runtime_checkable

from orbit.diagnostics import MetricSnapshot


@runtime_checkable
class MetricsExporter(Protocol):
    """Convert detached Core metric snapshots into one adapter-defined text representation.

    Implementations choose their exposition format and own escaping, aggregation, cardinality,
    transport, and output-size policies. The input tuple and snapshots are read-only contract
    values; an exporter should not retain them or mutate any nested data.
    """

    def export(self, snapshots: tuple[MetricSnapshot, ...]) -> str:
        """Return encoded samples without mutating or retaining the supplied snapshots.

        Raise an adapter-specific, sanitized error when a snapshot cannot be represented. Do not
        silently change metric type, labels, units, or counter/gauge semantics while encoding.
        """


__all__ = ["MetricsExporter"]
