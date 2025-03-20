from fastapi import FastAPI
from pydantic import BaseModel
from humanize_engine import humanize_text_advanced

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/humanize/")
async def humanize_text(input_data: TextInput):
    """
    API endpoint that receives text and returns a humanized version.
    """
    humanized_text = humanize_text_advanced(input_data.text)
    return {"humanized_text": humanized_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
