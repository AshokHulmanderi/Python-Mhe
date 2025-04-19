from typing import Union
from typing import List
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel

from file_processor import *
from message_parser import *

class DivertMessage(BaseModel):
    Loc: str
    MessageType: str
    WaveId: str
    OrderId: str
    ContainerId: str
    ContainerState: str
    LogicalDestination: str
    PhysicalDestination: str
    EventResult: str

#class DivertList(BaseModel):
#   Data: List[DivertMessage]

class Message(BaseModel):
    message: str

# Create a FastAPI instance
app = FastAPI(
    title="Cencora MHE TEST",
    description="This is a sample MHE Test for API",
    version="1.0.0"
)

# Endpoint to validate the divertmessages
@app.post("/mhe/Dematic/createDivertMessages")
def dematic_mawm_divert(inputDivertMessages: DivertMessage):
    try:
        return parse_dematic_divert(inputDivertMessages)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/mhe/Dematic")
def mawm_dematic_msg(message: Message):
    try:
        return parse_dematic_message(message.message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/mhe/knapp")
def mawm_knapp_msg(message: Message):
    try:
        return parse_knapp_message(message.message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/mhe/ssi")
def mawm_ssi_msg(message: Message):
    try:
        return parse_ssi_message(message.message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    