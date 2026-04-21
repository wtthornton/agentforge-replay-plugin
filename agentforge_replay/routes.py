from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(prefix="/api/replay-test", tags=["replay-test"])


class WriteRequest(BaseModel):
    namespace: str
    event_type: str
    payload: dict = {}


@router.post("/write")
async def write_event(body: WriteRequest, request: Request) -> dict:
    store = getattr(request.app.state, "event_store", None)
    if store is None:
        return {"written": False, "reason": "no event_store on app.state"}
    event_id = await store.write(
        namespace=body.namespace,
        event_type=body.event_type,
        payload=body.payload,
    )
    return {"written": True, "event_id": event_id}


@router.get("/query")
async def query_events(
    namespace: str | None = None, limit: int = 100, request: Request = None
) -> dict:
    store = getattr(request.app.state, "event_store", None)
    if store is None:
        return {"events": [], "reason": "no event_store"}
    events = await store.query(namespace=namespace, limit=limit)
    return {"events": events, "count": len(events)}
