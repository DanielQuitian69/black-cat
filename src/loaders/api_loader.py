from fastapi import FastAPI
from src.api.index_routes import router

class ApiServerLoader:

  """
  It's responsible for configure the server

  Returns:
    FastApi server object
  """
  @staticmethod
  def load():
    app = FastAPI(
      title="Black Cat API",
      description="Automation-focused API for ITools"
    )
    app.include_router(router)
    return app
