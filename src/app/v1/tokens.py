from fastapi import APIRouter
from libs.models.tokens import Tokens_get, Tokens_post, Tokens_delete
from sqlalchemy import literal, Select, Insert, Delete
from plugins.database.models import Tokens, Users
from plugins.database import Session

from uuid import uuid4
import math, datetime

router = APIRouter(
    prefix='/tokens',
    tags=['tokens']
)

@router.get('')
async def get_tokens(model:Tokens_get):
    async with Session.begin() as session:
        sql = Select(Tokens.id, Tokens.userID, Tokens.projectID, Tokens.token, Tokens.timestamp).join(Users, Users.id == Tokens.userID).where(Users.login == model.login, Users.password == model.password)
        data = await session.execute(sql)
        data = data.mappings().all()
    
    result = data[(model.page-1)*model.limit:(model.page-1)*model.limit+model.limit]
    return {
        'status':True,
        'params':{
            'limit':model.limit,
            'page':model.page,
            'count':len(result),
            'all':{
                'allPage':math.ceil(len(data)/model.limit),
                'allCount':len(data)
            }
        },
        "data":result
    }

@router.post('')
async def post_tokens(model:Tokens_post):
    token = str(uuid4())
    timestamp = datetime.datetime.now(datetime.UTC)
    async with Session.begin() as session:
        sub_sql = Select(Users.id, literal(model.projectID), literal(token), literal(timestamp)).where(Users.login == model.login, Users.password == model.password)
        sql = Insert(Tokens).from_select(['userID', 'projectID', 'token', 'timestamp'], sub_sql)
        await session.execute(sql)
        await session.commit()
    return {'status':True, 'token': token}

@router.delete('')
async def delete_tokens(model:Tokens_delete):
    async with Session.begin() as session:
        sql = Delete(Tokens).where(Tokens.token == model.token)
        await session.execute(sql)
        await session.commit()
    return {'status':True}