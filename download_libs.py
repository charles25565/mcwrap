import requests
import os.path

def download_libs(libs: list) -> None:
  session = requests.Session()
  for library in libs:
    print(library["name"])
    if os.path.isfile(library["downloads"]["artifact"]["url"].split("/")[-1]):
      continue
    with open(library["downloads"]["artifact"]["url"].split("/")[-1], "wb") as library_file:
      library_file.write(session.get(library["downloads"]["artifact"]["url"]).content)
