from fastapi import FastAPI
import os
import openai
gpt = FastAPI()

@gpt.get("/")
def 홈피():
    return 'Hello'

from pydantic import BaseModel
class 질문(BaseModel):
    question : str

@gpt.post("/send")
def gpt(data : 질문):
    API_KEY = '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'
    openai.api_key = API_KEY
    response = openai.Completion.create(
    prompt = data.question, 
    model = 'text-davinci-003', 
    max_tokens=1000,
    temperature=1,
    n=1,
    stop=['---']
    )
    result_text = response.choices[0].text.strip() if response.choices else ""
    return {"answer": result_text}



    