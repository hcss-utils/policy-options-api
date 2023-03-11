# -*- coding: utf-8 -*-
import typing
from pathlib import Path

import spacy

Prediction = typing.Dict[str, typing.Union[str, float]]
DEFAULT_MODEL: typing.Final = Path(__file__).resolve().parent / "models" / "model-best"


class PolicyOptionsClassifier:
    """Policy options text classification model.

    Usage
    -----
    >>> nlp = spacy.load("path/to/model")
    >>> snippet = '''The EU appears to have been able to put the new sanctions
    into effect through an agreement that member states
    will review implementation of the Ukraine peace plan by end-September'''
    >>> classifier = SentenceClassifier(nlp=nlp)
    >>> classifier.predict(snippet)
    {"sentence": ..., "policy option suggestion": 0.54}
    """

    def __init__(
        self, model: typing.Union[spacy.language.Language, None] = None
    ) -> None:
        self.nlp = model if model is not None else spacy.load(DEFAULT_MODEL)

    @classmethod
    def load(
        cls, model: typing.Union[spacy.language.Language, None] = None
    ) -> "PolicyOptionsClassifier":
        return PolicyOptionsClassifier(model=model)

    def predict(self, text: str) -> Prediction:
        doc = self.nlp(text)
        return {"text": text, **doc.cats}
