#!/usr/bin/env python3

########################################
# HEADER
import requests as r
import json

IP = "10.10.117.158"
URL = "http://{}/api/site-log.php".format(IP)
WORDLIST = "wordlist"

word = []
########################################


########################################
# READING PASSWORD_FILE AND CLOSE IT
with open(WORDLIST, "r") as WORDLIST:
  for line in WORDLIST:
    word.append(line.replace("\n", ""))
########################################


########################################
# FUZZING
for options in word:
  query = {"date" : options}
  response = r.get(URL, query)
  if response.text != "":
    print("{} \\'O'/".format(options))
    break
  else:
    print("{} -_-".format(options))
########################################