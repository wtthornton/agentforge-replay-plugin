"""Unit tests for ReplayRunner."""

from agentforge_replay.agents.replay_test_agent.runner import ReplayRunner


def test_run_returns_replay_ok():
    runner = ReplayRunner()
    assert runner.run() == "replay:ok"


def test_run_ignores_input():
    runner = ReplayRunner()
    assert runner.run("anything") == "replay:ok"
    assert runner.run("") == "replay:ok"
