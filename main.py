from typing import Annotated

from fastapi import FastAPI, UploadFile, File
from speech_to_text.schemas import TextGenerationSchema
from speech_to_text.text_generation import transcribe


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/speech-to-text", response_model=TextGenerationSchema)
async def generate_text(file: UploadFile):
    return await transcribe(file)


# @app.post("/speech-to-text", response_model=TextGenerationSchema)
# async def generate_text(file: Annotated[bytes, File()]):
#     result = base_model.transcribe(load_audio(file))
#     return {"data": result['text']}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
