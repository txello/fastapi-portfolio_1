from pydantic import (
    BaseModel,
    field_validator,
    ValidationInfo
)

class Tokens_get(BaseModel):
    login:str
    password:str
    
    limit:int = 20
    page:int = 1
    
    @field_validator('limit', 'page')
    @classmethod
    def check_limit(cls, v:int, info: ValidationInfo):
        if info.field_name == 'limit' and (v < 0 or v > 100):
            raise ValueError('Ошибка: значение лимита не находится в диапозоне 0-100')
        if info.field_name == 'page' and (1 > v):
            raise ValueError('Ошибка: значение страницы не может быть меньше 1')
        return v
    
class Tokens_post(BaseModel):
    login:str
    password:str
    projectID:int
    
class Tokens_delete(BaseModel):
    token:str