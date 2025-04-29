
import openpyxl
import os

from message_parser import *
from history_tracker import *
from MAWM_Connect import *


def parse_knapp_message(message: str):

    delimiter = "^"
    prefix = "STX"
    suffix = "ETX"

    message = message.strip()

    file_path = "./Mapping_Spec//Knapp_MHE.xlsx"
    # Validate prefix/suffix.
    if not (message.startswith(prefix) and message.endswith(suffix)):
        raise ValueError(f"Message must start with {prefix} and end with {suffix}: {message}")
    
    # Strip prefix/suffix.
    content = message[len(prefix):-len(suffix)].strip()
    fields = content.split(delimiter)

    # Otherwise, continue to parse message.
    response = {}

    for i in range(0, len(fields), 2):
        key = fields[i].strip()
        value = fields[i + 1].strip()

        # Validate if keyword is valid and is in the allowed list.
        if key not in MHE_FIELDS_ALLOWED:
            raise ValueError(f"Invalid keyword '{key}' found in message: {message}")

        # Add to the response dictionary.
        response[key] = value

    # Validate if all required fields are present.
    missing_fields = [field for field in MHE_FIELDS_REQUIRED if field not in response]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    return response
