from uvicorn import run
from core import app
from settings import HOST, PORT

run(app, host=HOST, port=PORT)
