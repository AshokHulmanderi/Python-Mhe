# Sample Message Parser to compare and validate between the input and the excel file

# Function to parse the sheet name from the message
# This function should be modified based on how the sheet name is represented in the message
def parse_sheet_name(value: str) -> str:
    """
    Parses the sheet name from the given value.
    Modify this logic based on your specific requirements.
    """
    if value:
        return value.strip()  # Example: Strip any leading/trailing whitespace
    return None


def message_Parser(fields, rows ) -> dict:

    # Initialize the response JSON array
    response_json = []

    # Validate rows where row[4] == 'M'
    for index, row in enumerate(rows):

        if len(row) > 4:  # Ensure the row has at least 5 elements
            field_name = row[0]
            required_length = row[2] if len(row) > 2 and isinstance(row[2], (int, float)) else 50
            field_required = row[4]
            received_value = fields[index].strip() if index < len(fields) and fields[index] else None

            # Add the field details to the response JSON array
            response_json.append({
                "field_name": field_name,
                "received_value": received_value,
                "field_required": field_required,
                "required_length": required_length
            })
 
            if field_required == "M":
                if not received_value:
                    raise ValueError(f"Value for '{field_name}' is not present in position '{index}' .")

            
            if received_value and len(received_value) > required_length:
                raise ValueError(f"Value for '{field_name}' is more the required length '{required_length}'.")


    # Return the response JSON array
    return response_json


"""  
    # Extract MHE_FIELDS_ALLOWED from column1 of rows
    MHE_FIELDS_ALLOWED = [row[0] for row in rows if row[0]]

    # Parse the message into a dictionary
    response = {}
    for i in range(0, len(fields), 2):
        key = fields[i].strip()
        value = fields[i + 1].strip()

        # Validate if the keyword is valid and is in the allowed list
        if key not in MHE_FIELDS_ALLOWED:
            raise ValueError(f"Invalid keyword '{key}' found in message.")

        # Add to the response dictionary
        response[key] = value
    
    string_position = 0

    for row in rows:
        string_position =string_position + 1

        if len(row) > 4 and row[4] == "M":  # Ensure row has at least 5 elements
            missing_fields = [field for field in MHE_FIELDS_REQUIRED if field not in response]


            # Check if mandatory input string is present and of length specified
            if field_length > max_length:
                max_length = field_length
                MHE_FIELDS_REQUIRED = [row[2]]  # Reset with the new max-length field
            elif field_length == max_length:
                MHE_FIELDS_REQUIRED.append(row[2])  # Add to the list if the length matches max_length

    if not MHE_FIELDS_REQUIRED:
        raise ValueError("No required fields found in rows.")


    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    return response
 """

