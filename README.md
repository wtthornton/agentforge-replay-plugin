# agentforge-replay-plugin

Event-store replay rig for AgentForge (TAP-770).

Provides two HTTP endpoints that exercise `EventStore.write()` and `EventStore.query()`
through the plugin system — the pre-release smoke gate for event persistence.

## Endpoints

- `POST /api/replay-test/write` — write an event to the host app's `event_store`
- `GET /api/replay-test/query` — query events, optionally filtered by namespace

## Install

```bash
pip install -e /path/to/agentforge-replay-plugin
```

Or from the AgentForge project root:

```bash
uv add --editable /path/to/agentforge-replay-plugin
```

## Plugin registration

```python
# Via PluginRegistry (preferred)
await registry.register_plugin("agentforge_replay")

# Or direct
from agentforge_replay.plugin import register
register(app)
```

## Running tests

```bash
# Plugin-internal unit tests
cd agentforge-replay-plugin
uv run pytest

# AgentForge smoke tests (requires AgentForge deps)
cd AgentForge
uv run pytest backend/tests/test_replay_smoke.py
```
