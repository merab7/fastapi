from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to my asi!"}

@app.get("/posts")
def get_posts():
    return {"data":"content"}