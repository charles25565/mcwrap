import requests
import os
import os.path

def download_assets(objects: dict) -> None:
  session = requests.Session()
  for asset in objects:
    print(asset)
    if os.path.isfile("assets/" + asset):
      continue
    os.makedirs(os.path.dirname("assets/" + asset), exist_ok=True)
    with open("assets/" + asset, "wb") as asset_file:
      asset_file.write(session.get("https://resources.download.minecraft.net/" + objects[asset]["hash"][:2] + "/" + objects[asset]["hash"]).content)
