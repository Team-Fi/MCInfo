import urllib.request, json, ssl, datetime, base64

ssl._create_default_https_context = ssl._create_unverified_context

username = input("Username: ")

print("Gathering some data...")

with urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/" + username) as url:
    nu = json.loads(url.read().decode())

uuid = nu["id"]
username = nu["name"]

with urllib.request.urlopen("https://api.mojang.com/user/profiles/" + uuid + "/names") as url:
    nh = json.loads(url.read().decode())

with urllib.request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid) as url:
    pf = json.loads(base64.b64decode(json.loads(url.read().decode())["properties"][0]["value"]))

print("Done!")
print("")

print("Username: " + username)
print("")
print("UUID: " + uuid)
print("")
print("Username History:")
for val in nh:
    if "changedToAt" in val:
        print("- " + val["name"] + " (" + str(datetime.datetime.utcfromtimestamp(val["changedToAt"] / 1000)) + ")")
    else:
        print("- " + val["name"])
print("")
if "metadata" in pf["textures"]["SKIN"]:
    print("Skin: " + pf["textures"]["SKIN"]["url"] + " (Slim)")
else:
    print("Skin: " + pf["textures"]["SKIN"]["url"])
print("")
if "CAPE" in pf["textures"]:
    print("Cape: " + pf["textures"]["CAPE"]["url"])
else:
    print("Cape: None")
