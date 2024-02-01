from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root() :
    return {"message": "/Bagath"}

@app.post("/")
async def post():
    return {"message":"Messaage back from post"}