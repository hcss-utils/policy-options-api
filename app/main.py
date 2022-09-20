# -*- coding: utf-8 -*-
import json
from fastapi import FastAPI, Body, HTTPException
from starlette.responses import RedirectResponse

from app.models import InputDocument, ModelResponse
from app.classifier import PolicyOptionsClassifier

SECRET_TOKEN = "policy-options-2022"

app = FastAPI(title="Policy Options classifier", version="1.0")

text = "I may as well admit that I have a preference for democracy over rival systems"
example_request = json.dumps({"text": text})


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")


@app.post("/entities", response_model=ModelResponse)
def predict(token: str, sentence: InputDocument = Body(..., example=example_request)):
    """Predicts if sentnece contains policy options / suggestions."""
    if token != SECRET_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
        )
    classifier = PolicyOptionsClassifier.load(model=None)
    return classifier.predict(sentence)
