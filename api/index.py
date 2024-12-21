from fastapi import FastAPI
from pydantic import BaseModel
from semantic_analyzer import analyze_semantic
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from translation import Translation
from suggestions import Suggestion

# Initialize FastAPI app
app = FastAPI()


class ProverbRequest(BaseModel):
    proverb_input: str

class TranslationRequest(BaseModel):
    input: str
    translate_to: str

class TranslationResponse(BaseModel):
    translation: str
    is_error: bool
    bayt: str
    closest_match: str




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
    lines = proverb.proverb_input.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        res = analyze_semantic(line)
        if res["is_error"]:
            return JSONResponse(content=jsonable_encoder({
                "is_error": True,
                "message": res["message"],
                "bayt": line
            }))
    
    # If no errors found, return success
    return JSONResponse(content=jsonable_encoder({
        "is_error": False,
        "message": "Verification Result: Valid phrase.",
        "bayt": "All sentences are correct"
    }))
    
    
@app.post("/api/py/translation")
async def translate_input(req: TranslationRequest) -> TranslationResponse:
        fulltext: str = ""
        lines = req.input.split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
            compiler_verification = analyze_semantic(line)
            if compiler_verification["is_error"]:
                suggestion = Suggestion()
                suggestion_result = suggestion.suggest(line)
                print(suggestion_result["accuracy"])
                if suggestion_result["is_found"] and suggestion_result["accuracy"] > 0:
                    return JSONResponse(content=jsonable_encoder({
                        "is_error": True,
                        "translation": compiler_verification["message"],
                        "bayt": line,
                        "closest_match": suggestion_result["message"]
                    }))
                else:
                    return JSONResponse(content=jsonable_encoder({
                        "is_error": True,
                        "translation": compiler_verification["message"],
                        "bayt": line,
                        "closest_match": ""
                    }))
            res = translation_based_on_language(req.translate_to, line)
            fulltext += res + "\n"
        return JSONResponse(content=jsonable_encoder({
            "is_error": False,
            "translation": fulltext,
            "bayt": ""
        }))



