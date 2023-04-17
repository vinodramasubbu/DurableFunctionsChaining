# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

"""
import logging


def main(name: str) -> str:
    logging.info(f"Python HTTP trigger function processed a request. Name={name}")
    return f"Hello {name}!"
"""

import azure.functions as func
import logging
import uuid
import json

#def main(name: str) -> str:
def main(name: str, outputDocument: func.Out[func.Document]) -> str:
    logging.info(f"Python HTTP trigger function processed a request. Name={name}")
    #outputDocument.set(func.Document.from_dict({"id": id, "activity": name}))
    outputDocument.set(func.Document.from_dict(json.loads(name)))
    return f"{json.loads(name)}!"
