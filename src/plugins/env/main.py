from envserv import EnvBase

class DockerEnv(EnvBase):
    __envfile__ = '.env'
    
    HOST:str
    PORT:int
    DEBUG:bool
    VERSION:str
    
env_docker = DockerEnv()