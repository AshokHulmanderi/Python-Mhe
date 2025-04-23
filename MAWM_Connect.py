import json
import requests

CLIENT_AUTH = "b21uaWNvbXBvbmVudC4xLjAuMDpiNHM4cmdUeWc1NVhZTnVu"
URL_AUTH = "https://amscd-auth.sce.manh.com/oauth/token"
URL_HOST = "https://amscd.sce.manh.com/"

USR = "cencoraserviceuser"
PWD = "Zkc123sg7p$"
LOC = "200"
ORG = "200"


# Function - Access Token
def access_token(token_url, username, password):
    headers = {
        "Authorization": "Basic " + CLIENT_AUTH,
        "Accept": "application/json"
    }

    response = requests.post(
        url=token_url,
        headers=headers,
        data={
            "grant_type": "password",
            "username": username,
            "password": password
        }
    )

    response.raise_for_status()
    return response.json()["access_token"]


# Function - API Request (POST)
def restfulPOST(token, location, organization, host, component, subcomponent, requestUrl, payload):
    url = host + component + "/api/" + subcomponent + requestUrl
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "selectedLocation": location,
        "selectedOrganization": organization
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=payload
    )

    response.raise_for_status()
    return response.json()


# Function to process the appropriate vendor-specific file
def invoke_mawm_dei(endpointId, message_string):
    # Get Access Token
    token = access_token(URL_AUTH, USR, PWD)

    # Payload Creation
    payload = json.dumps({
        "EndpointId": endpointId,
        "Message": [
             message_string
        ]
    })

    # Invoke API Request
    response = restfulPOST(
        token,
        LOC,
        ORG,
        URL_HOST,
        "device-integration",
        "deviceintegration",
        "/process",
        payload
    )

    return response