---
name: replay-test-agent
namespace: project.replay-test.replay-test-agent
description: Test agent for AgentForge event-store replay rig.
keywords: [replay, events, store, test]
runner: agentforge_replay.agents.replay_test_agent.runner:ReplayRunner
---

# Replay Test Agent

Deterministic test fixture for the event-store replay rig (TAP-770).

Returns `"replay:ok"` on every run. Exists to exercise `AgentLoader.load_external()`,
namespace registration under `project.replay-test`, and the plugin agent surface
without pulling in any LLM provider or external service.
