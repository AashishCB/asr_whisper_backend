from pydantic import BaseModel


class TextGenerationSchema(BaseModel):
    data: str
