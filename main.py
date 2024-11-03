# all packages
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


# Main function
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool=True
    rating:Optional[int]=None

my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"Favorite foods","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p


@app.get("/")
def root():
    return {"message":"Hello I am zakir"}
 

@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return {"details":post}


@app.get("/posts/{id}")
def get_posts(id:int,response:Response):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} was not Found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"Post with id:{id} was not Found!"}
    return {"Post detail":post}





# Title str, Content str