import os
import requests
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv("PERSONAL_DISCORD_AUTHORIZATION")

# Grab the URL for the normies channel
normies_url = "https://discord.com/api/v9/channels/1110098316479438870/messages"

# Creating our payload
payload_msg = {
    "content" : "<@261167267142696960>"
}
# Creating our header
headers = {
    "Authorization" : auth_token
}


# Send a post request to the normies url
res = requests.post(normies_url, payload_msg, headers=headers)