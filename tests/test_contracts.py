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
"""Structural contract coverage for optional metric exporters."""

from orbit.diagnostics import MetricSnapshot

from orbit_metrics import MetricsExporter


class TextExporter:
    """Minimal provider-specific implementation used to exercise the public protocol."""

    def export(self, snapshots: tuple[MetricSnapshot, ...]) -> str:
        """Return a deterministic representation of the supplied detached samples."""
        return "\n".join(snapshot.name for snapshot in snapshots)


def test_exporter_protocol_is_structural_and_typed() -> None:
    exporter = TextExporter()
    snapshot = MetricSnapshot("requests_total", "counter", {}, 1)

    assert isinstance(exporter, MetricsExporter)
    assert exporter.export((snapshot,)) == "requests_total"
