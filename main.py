import os
import requests

# TODO: Custom install locations
DEFAULT_INSTALL_DIR = "C:\Program Files (x86)\Disney\Disney Online\ToontownOnline"

if not os.path.exists(DEFAULT_INSTALL_DIR):
    raise Exception("Please install Toontown Online through the installer first.")

headers = {
    "User-Agent": "TTOManager - Automated Setup Utility"
}

params_data = requests.get("https://download.sunrise.games/parameters/parameters.txt", headers=headers).text
open(os.path.join(DEFAULT_INSTALL_DIR, "parameters.txt"), "w").write(params_data)
print("Pointed launcher to Sunrise servers.")

# Setup the wrokaround for connection hang
os.makedirs(os.path.join(DEFAULT_INSTALL_DIR, "hash_data"), exist_ok=True)
print("Added workaround for connection freeze on modern versions of Windows.")

# Finally, grab cnc-ddraw
ddraw_data = requests.get("https://raw.githubusercontent.com/rocketprogrammer/TTOManager/main/libs/cnc-ddraw/ddraw.dll").content
open(os.path.join(DEFAULT_INSTALL_DIR, "ddraw.dll"), "wb").write(ddraw_data)
print("Added cnc-ddraw display wrapper.\nToontown Online should be ready to go now.")

os.system("pause")
