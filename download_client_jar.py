import requests
import os.path

def download_client_jar(url: str) -> None:
  print("client.jar")
  if os.path.isfile("client.jar"):
    return
  with open("client.jar", "wb") as client_file:
    client_file.write(requests.get(url).content)
