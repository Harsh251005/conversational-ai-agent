from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

class MessageRequest(BaseModel):
    message: str

app = FastAPI()

@app.post("/chat")
def chat(response: MessageRequest):
    llm_response = client.chat.completions.create(
        messages=[{"role": "user", "content": response.message}],
        model="llama-3.3-70b-versatile",
    )

    return llm_response.choices[0].message.content
