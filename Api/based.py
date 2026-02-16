from fastapi import APIRouter, Response

router = APIRouter(prefix='/base')

@router.get('hello world')
async def get_hello_world():
    return Response(content='hello world', status_code=204)