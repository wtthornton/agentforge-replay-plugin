"""Deterministic runner for replay-test-agent. Pure function, no side effects."""

from __future__ import annotations


class ReplayRunner:
    def run(self, input_text: str = "") -> str:
        return "replay:ok"
