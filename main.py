from dotenv import load_dotenv
import os
import base64
import requests
import json

load_dotenv()

Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")

print(Client_ID, Client_Secret)

def get_token():
    auth_string = Client_ID + ":" + Client_Secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token
print(get_token());
'''def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
          
    if len(json_result) == 0:
        print("No artist found")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def save_token_to_file(token, filename):
    with open(filename, 'w') as file:
        file.write(f"token={token}")

def read_token_from_file(filename):
    with open(filename, 'r') as file:
        token = file.read().replace("token=", "")
    return token

# Get a new token
token = get_token()

# Save the new token to a file
save_token_to_file(token, 'whre you should save the token')

# Read the token from a file
token = read_token_from_file('where you saved the token')

result = search_for_artist(token, "BTS")
print(result["name"])
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx+1}. {song['name']}")'''