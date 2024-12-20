from ply.lex import lex
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Request and Response models
class ProverbRequest(BaseModel):
    proverb_input: str

class ProverbResponse(BaseModel):
    valid: bool
    error: str = None
    bayt: str = None

# Define tokens for the lexer
tokens = (
    'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'IDENTIFIER'
)

# Token regex patterns
t_FIRST = r'على'
t_SECOND = r'قدر'
t_THIRD = r'أهل'
t_FOURTH = r'الحلم'
t_FIFTH = r'ترتقي'
t_SIXTH = r'الآمال'
t_IDENTIFIER = r'[^\s]+'

# Ignored characters
t_ignore = ' \t\n'

# Error handling for invalid tokens
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Initialize the lexer
lexer = lex()

# Proverb verification logic
def verify_proverb(proverb_input):
    lexer.input(proverb_input)

    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    valid_order = (
        ('FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH'),
        ('FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH'),
        ('FIRST', 'SECOND', 'THIRD', 'FOURTH'),
        ('FIRST', 'SECOND', 'THIRD'),
        ('FIRST', 'SECOND'),
    )

    bayts = {
        ('على', 'قدر', 'أهل', 'الحلم', 'ترتقي', 'الآمال'): "على قدر أهل الحلم ترتقي الآمال",
        ('وتزهر', 'على', 'دروب', 'العزّ', 'الأعمال'): "وتزهر على دروب العزّ الأعمال",
        ('وتكبر', 'في', 'عين', 'الفتى', 'أحلامه'): "وتكبر في عين الفتى أحلامه",
        ('وتصغر', 'في', 'عزم', 'الحكيم', 'الأحوال'): "وتصغر في عزم الحكيم الأحوال",
    }

    response = {
        "valid": False,
        "error": None,
        "bayt": None
    }

    if any(token.type == 'IDENTIFIER' for token in tokens):
        response["error"] = "Sentence contains unknown token."
    elif tuple(token.type for token in tokens) not in valid_order:
        response["error"] = "Invalid token order."
    elif tuple(token.value for token in tokens) in bayts:
        response["valid"] = True
        response["bayt"] = bayts[tuple(token.value for token in tokens)]
    else:
        response["error"] = "The input does not match any known valid phrases."
    
    return response

# FastAPI endpoint
@app.post("/api/py/verify_input")
async def verify_input_endpoint(proverb: ProverbRequest):
    print(proverb.proverb_input)
    result = verify_proverb(proverb.proverb_input)
    return result
