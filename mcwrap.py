import download_assets
import download_client_jar
import download_libs
import run_client
import requests
import sys
import json
import os

os.makedirs("mc" + sys.argv[2].split("/")[-1].split(".json")[0], exist_ok=True)
os.chdir("mc" + sys.argv[2].split("/")[-1].split(".json")[0])

data = json.loads(requests.get(sys.argv[2]).text)

download_client_jar.download_client_jar(data["downloads"]["client"]["url"])

download_libs.download_libs(data["libraries"])

assets = json.loads(requests.get(data["assetIndex"]["url"]).content)
download_assets.download_assets(assets["objects"])

run_client.run_client(sys.argv[1], data["id"])

os.chdir("..")
