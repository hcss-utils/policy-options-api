# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field


class InputDocument(BaseModel):
    text: str


class ModelResponse(InputDocument):
    policy_options: float = Field(alias="policy options")

    class Config:
        allow_population_by_field_name = True
