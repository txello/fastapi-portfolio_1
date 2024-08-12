from plugins.env import env_docker

HOST = env_docker.HOST
PORT = env_docker.PORT

FASTAPI_SETTINGS = {
    'debug':env_docker.DEBUG,
    'title':'FastAPI',
    'docs_url':'/docs'
}

VERSION = env_docker.VERSION

APPS = [
    'tokens'
]