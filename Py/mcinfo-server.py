import urllib.request, json, ssl
ssl._create_default_https_context = ssl._create_unverified_context

address = input("Address: ")

print("Gathering some data...")

with urllib.request.urlopen("https://api.mcsrvstat.us/2/"+address) as url:
	info = json.loads(url.read().decode())

print("Done!")

if info["online"]:
	print("")
	print("Address: "+address)
	print("")
	print("MOTD: "+info["motd"]["clean"][0])
	print("")
	if "list" in info["players"]:
		print("Players: "+", ".join(info["players"]["list"])+" ("+str(info["players"]["online"])+"/"+str(info["players"]["max"])+")")
	elif info["players"]["online"]:
		print("Players: "+str(info["players"]["online"])+"/"+str
		(info["players"]["max"]))
	else:
		print("Players: None")
	print("")
	print("Version: "+info["version"])
	print("")
	if "hostname" in info:
		print("Hostname: "+info["hostname"])
	else:
		print("Hostname: None")
	print("")
	if "software" in info:
		print("Software: "+info["software"])
	else:
		print("Software: None")
	print("")
	if "plugins" in info:
		print("Plugins: "+", ".join(info["plugins"]["names"]))
	elif "mods" in info:
		print("Mods: "+", ".join(info["mods"]["names"]))
	else:
		print("Plugins/Mods: None")
else:
	print("Server Offline")