from fastapi import FastAPI
from pydantic import BaseModel
from semantic_analyzer import analyze_semantic
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from translation import Translation


# Initialize FastAPI app
app = FastAPI()


class ProverbRequest(BaseModel):
    proverb_input: str
    is_textarea: bool

class TranslationRequest(BaseModel):
    input: str
    is_textarea: bool
    translate_to: str

class TranslationResponse(BaseModel):
    translation: str


def translation_based_on_language(lang:str, input:str):
    translator = Translation()
    if lang == "en":
        english_translation = translator.translate_english(input)
        return english_translation
    else:
        french_translation = translator.translate_frensh(input)
        return french_translation
    

# FastAPI endpoint
@app.post("/api/py/verify_input")
async def verify_input_endpoint(proverb: ProverbRequest):
    if len(proverb.proverb_input) == 0:
        return JSONResponse(content=jsonable_encoder({
          "is_error": True,
          "message": "Please enter a sentence",
          "bayt": "input length must be bigger than 0"
      }))
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
          "message": "Verification Result: Valid phrase.",
          "bayt": "All sentences are correct"
      }))
    else:
      return  JSONResponse(content=jsonable_encoder(analyze_semantic(proverb.proverb_input)))
    
    
@app.post("/api/py/translation")
async def translate_input(req: TranslationRequest) -> TranslationResponse:
    if req.is_textarea:
        fulltext: str = ""
        lines = req.input.split("\n")
        for line in lines:
            line = line.strip()
            print(line)
            if not line:
                continue
            res = translation_based_on_language(req.translate_to, line)
            fulltext += res
        
        fulltext = fulltext.replace("?", "\n")
        print(fulltext)
        return JSONResponse(content=jsonable_encoder(fulltext))
    else:
        return JSONResponse(content=jsonable_encoder(translation_based_on_language(req.translate_to, req.input)))


