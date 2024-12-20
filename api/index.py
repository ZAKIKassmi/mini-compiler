from fastapi import FastAPI


app = FastAPI()

@app.get("/api/py/helloWorld")
def hello_world_endpoint():
  return {"message": "Hello from fast api"}

