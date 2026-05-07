

import requests

CLIENT_ID = "Ypixa0O9MoKSrkijCbfoVVxpWEQxed5g"
CLIENT_SECRET = "T7pi3XIBnpen86ZpLWK327n162nC3BbaD945Rd76"

def get_access_token():
    url = "https://login.uber.com/oauth/v2/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": "ride_widgets"
    }
    response = requests.post(url, data=payload)
    print(response.status_code)


get_access_token()