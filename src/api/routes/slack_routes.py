from fastapi import APIRouter, Request, Response
from src.api.middlewares.slack_middlewares import slack_events_middleware

slack_router = APIRouter()

@slack_router.post("/events")
async def slack_events_middleware(request: Request, response: Response):
  body = await request.json()  
  if body.get("type") == "url_verification":
    return {"challenge": body.get("challenge")}
  return Response(status_code=200)
