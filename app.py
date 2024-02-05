from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import torch
import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

class prompt_creation(BaseModel):
    prompt: str

@app.post("/predict")
async def predict(prompt_data: prompt_creation):

    input_text = prompt_data.prompt

    llm=CTransformers(model='./models/llama-2-7b-chat.ggmlv3.q4_K_S.bin',
                      model_type='llama',
                      n_gqa=8,
                      n_gpu_layers=32,
                      n_threads=6,
                      config={'max_new_tokens':256,
                              'temperature':0.1})
    prompt=PromptTemplate(input_variables=["input_text"],
                          template=input_text)
    response_text=llm(prompt.format(input_text=input_text))
    return response_text


if __name__ == "__main__":
   uvicorn.run("app:app",port=8080,reload=True)