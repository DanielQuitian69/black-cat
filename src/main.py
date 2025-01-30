from src.loaders.api_loader import ApiServerLoader

"""
Function responsible for loading all the services necessary for the operation of the API
"""
def loadApplication ():
  return ApiServerLoader.load()


app = loadApplication()