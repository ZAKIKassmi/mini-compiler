from fastapi import FastAPI
from pydantic import BaseModel
from semantic_analyzer import analyze_semantic
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



# Initialize FastAPI app
app = FastAPI()

# Request and Response models
class ProverbRequest(BaseModel):
    proverb_input: str
    is_textarea: bool


# FastAPI endpoint
@app.post("/api/py/verify_input")
async def verify_input_endpoint(proverb: ProverbRequest):
    if proverb.is_textarea:
      lines = proverb.proverb_input.split("\n")
      for line in lines:
          line = line.strip()
          if not line:
              continue
          res = analyze_semantic(line)
          if res["is_error"]:
              return JSONResponse(content=jsonable_encoder(res))
      
      # If no errors found, return success
      return JSONResponse(content=jsonable_encoder({
          "is_error": False,
          "message": "Everything is ok",
          "bayt": ""
      }))

    else:
      return  JSONResponse(content=jsonable_encoder(analyze_semantic(proverb.proverb_input)))
    
    
