# policy-options-api

Welcome to the Policy Options Suggestion Predictor!

This repository contains a FastAPI backend application that can predict whether a given piece of text contains suggestions for policy options. 
It uses a machine learning model trained on a dataset of policy documents to make these predictions.

To use this app, you will need to have `docker` and `docker-compose` installed on your machine.

Once everything is set up, you can start the app by running `docker-compose up`. This will start the FastAPI server, which you can access at the default address (http://127.0.0.1:8000).

The app has a single endpoint, `/api/policy-options/predict`, which you can send a POST request to with a JSON payload containing the text you want to predict on.
The endpoint will return a JSON response with two keys:

- `text`: the input text that was sent in the request
- `policy options`: a float value indicating the model's confidence that the input text contains policy options suggestions. The higher the value, the higher the confidence.

An example of how you might use this endpoint is shown below:

```python
import requests


def predict(s: str) -> float:
    """Make a prediction on whether the input text contains policy options suggestions.

    Parameters
    ----------
    s : str
        The input text to make a prediction on.

    Returns
    -------
    float
        A float value indicating the model's confidence that the input text contains policy options suggestions. 
        The higher the value, the higher the confidence. If an error occurs, returns 0.0."""

    response = requests.post(
        "http://127.0.0.1:8000/api/policy-options/predict?token=policy-options-2022",
        json={"text": s}
    if response.status == 200:
        return response.json()["policy options"]
    else:
        return 0.0


if __name__ == "__main__":
    sentences = [
        "China and Russia can either tailor messaging in combined...", 
        "Rather than wait for a miracle, policymakers should create a strategy..."
    ]
    for sent in sentences:
        score = predict(sent)
        ...
```
