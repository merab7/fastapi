from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel 
from random import randrange
from fastapi import status, Response, HTTPException

 
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True #giving default value as True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content":"content of post 1", "id": 1},{"title": "title of post 2", "content":"content of post 2", "id":2}]


@app.get("/")
async def root():
    return {"message": "welcome to my asi!"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):

    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)

    return {"data":post_dict}

@app.get("/posts/{id}")#GET SPECIFIC POST WITH PATH PARAMETHER
def get_posts(id:int, response=Response):
    
    for post in my_posts:
        if post["id"] == id:
            return{"Retrieved Post": f'Here is your post{post}'} 
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id{id} does not exists')
