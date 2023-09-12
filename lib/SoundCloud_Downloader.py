import requests
import typing

def Get_Trackinfo_From_SoundCloud(soundCloudURL: str, destPath: str, client_id):
    print("Start to download from SoundCloud")
    soundCloudAPI = f"https://api.soundcloud.com/resolve?url={soundCloudURL}&client_id={client_id}"
    response = requests.get(soundCloudAPI)

    if response.status_code == 200:
        data = response.json()
