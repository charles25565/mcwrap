import os
import subprocess
import glob

def run_client(username: str, id: str) -> None:
  classpath = ""
  for jar in glob.glob("*.jar"):
    classpath += jar + ":"
  classpath = classpath.rstrip(":")
  subprocess.call(("java", "-cp", classpath, "net.minecraft.client.main.Main", "-accessToken", "0", "-version", id, "-assetDir", "assets", "-username", username, "-demo"))
