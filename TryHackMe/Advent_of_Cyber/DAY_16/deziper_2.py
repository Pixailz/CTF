#!/usr/bin/env python3

from os import path, chdir, listdir, getcwd, system, remove
import zipfile
import exiftool
import sys

CWD = getcwd()
FOLDER = "zipfile"
PATH = "{}/{}".format(CWD, FOLDER)

def extract_zip():

  is_finish = False

  while is_finish == False:

    list_of_file = listdir(FOLDER)
    contain_zip = False

    for file in list_of_file:

      if ".zip" in file:

        contain_zip = True

    if contain_zip == True:

      for file in list_of_file:

        file_path = "{}/{}".format(FOLDER, file)

        if zipfile.is_zipfile(file_path):

          print("Decompressing : {}".format(file_path))

          with zipfile.ZipFile(file_path, "r") as zip_ref:

            zip_ref.extractall(PATH)
            zip_ref.close()

          remove(file_path)

        else:
          print(file_path, "Not a .zip file")

    else:
      is_finish = True

def extract_metadata():

  for i in listdir(PATH):

    system(f"exiftool {PATH}/{i} >> exiftool.txt")

  with open("exiftool.txt") as etresults:

    metadata = etresults.readlines()

  system("rm exiftool.txt")

  counter = 0

  for line in metadata:

    if "Version" in line and "1.1" in line:

      counter += 1

  print("The number of files containing Version: 1.1 is: ",counter)

def check_file_for_password():
  
  chdir(PATH)

  for filename in listdir():

    try:

      with open(filename, "r") as f:

        data = f.read()
        if "password" in data:

          print("Filename is :", filename)

    except:
      
      continue

extract_zip()

extract_metadata()

check_file_for_password()