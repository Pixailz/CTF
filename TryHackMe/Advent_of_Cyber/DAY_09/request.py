#!/usr/bin/env python3

import requests
import json

path = ""
host = "http://10.10.169.100:3000/"
response_value = []

while host != "":

  response = requests.get(host + path)
  value = json.loads(response.text)
    
  if value["next"] == "end" and value["value"] == "end":

    host = ""
    finalvalue = ""

    for value in response_value:
      finalvalue = str(finalvalue) + str(value)
        
      print (finalvalue)

  else:
    response_value.append(value["value"])
    path = value["next"]

