# all packages
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


# Main function
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool=True
    rating:Optional[int]=None

my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"Favorite foods","content":"I like pizza","id":2}]
@app.get("/")
def root():
    return {"message":"Hello I am zakir"}
 

@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/posts")
def create_posts(post:Post):
    print(post.rating)
    return {"data":post}


# Title str, Content str