# all packages
from fastapi import FastAPI




# Main function
app=FastAPI()


@app.get("/")
def root():
    return {"message":"Hello I am zakir"}
 

@app.get("/posts")
def get_posts():
    return {"data":"This is your posts"}
