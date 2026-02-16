from fastapi import APIRouter, Response, status
from schemas.post import Post
router = APIRouter()


@router.get('/hello world')
async def get_hello_world():
    return Response(content='hello world', status_code=status.HTTP_200_OK)


@router.post('/test_json', status_code=status.HTTP_201_CREATED)
async def test_json(post: Post) -> dict:
    response = {
        "post_text": post.text,
        "author_name": post.author_name
    }

    return response
