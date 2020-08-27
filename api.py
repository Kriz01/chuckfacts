import requests
import json
import config

def apicall():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        'x-rapidapi-key': config.api_key,
        'accept': "application/json"
        }

    response = requests.request("GET", url, headers=headers)
    json_obj = json.loads(response.text)

    for json_key in json_obj:
        if(json_key=="value"):
         return json_obj[json_key]
