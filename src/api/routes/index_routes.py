from fastapi import APIRouter
from src.env import env
from src.api.routes.slack_routes import slack_router

router = APIRouter()

@router.get("/", tags=['health'])
def root():
  return {
    "message": "Black Cat API is running",
    "status": "OK"
  }

@router.get("/health", tags=['health'])
def health_check():
  return {
    "status": "healthy",
    "version": env['GENERAL_CONFIG']['version']
  }

router.include_router(slack_router, prefix='/slack', tags=['slack'])
