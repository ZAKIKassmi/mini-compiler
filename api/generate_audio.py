import edge_tts
import uuid  

async def generate_speech(input: str):
    random_name = f"{uuid.uuid4()}.mp3" 
    file_path = f"../public/audio/{random_name}"  
    
    tts = edge_tts.Communicate(input, voice='ar-DZ-IsmaelNeural')
    
    await tts.save(file_path)
    return file_path

