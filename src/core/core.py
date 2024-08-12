from fastapi import FastAPI, APIRouter
from importlib import import_module
import settings

app = FastAPI(**settings.FASTAPI_SETTINGS)

if hasattr(settings, 'VERSION'):
    route = APIRouter(
        prefix=f'/{settings.VERSION}',
        tags=[settings.VERSION]
    )
else:
    route = APIRouter()

for apps in settings.APPS:
    if hasattr(settings, 'VERSION'):
        module = import_module(f'app.{settings.VERSION}.{apps}')
    else:
        module = import_module(f'app.{apps}')
    route.include_router(getattr(module,'router'))
    
app.include_router(route)