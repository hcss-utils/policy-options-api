# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field


class InputDocument(BaseModel):
    text: str


class ModelResponse(InputDocument):
    policy_option: float = Field(alias="policy-option")

    class Config:
        allow_population_by_field_name = True
