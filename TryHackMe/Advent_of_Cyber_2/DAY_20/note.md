# Command

## `Get-ChildItem`
	- `-Hidden`			
	- `-Recurse`
	- `-File`
	- `-Directory`
	- `-Filter '<REGEX>'`

## `Get-Content`
	- `-Path`

## `Measure-Object`
	- `-Word`
	
## 1st (Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?)
```
PS C:\Users\mceager\Documents> Get-ChildItem -Hidden -File


    Directory: C:\Users\mceager\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        12/7/2020  10:29 AM            402 desktop.ini
-arh--       11/18/2020   5:05 PM             35 e1fone.txt
```

## 2nd (Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?)
```
PS C:\Users\mceager\Desktop> Get-ChildItem -Directory -Hidden


    Directory: C:\Users\mceager\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--h--        12/7/2020  11:26 AM                elf2wo
```

## 3rd (Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while))
```
PS C:\Windows> Get-ChildItem -Hidden -Directory -Filter '*3*' -Recurse -ErrorAction SilentlyContinue
 

    Directory: C:\Windows\System32


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--h--       11/23/2020   3:26 PM                3lfthr3e

```

## 4th (How many words does the first file contain?)
```
PS C:\Windows\System32\3lfthr3e> Get-ChildItem -Hidden


    Directory: C:\Windows\System32\3lfthr3e


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-arh--       11/17/2020  10:58 AM          85887 1.txt
-arh--       11/23/2020   3:26 PM       12061168 2.txt

PS C:\Windows\System32\3lfthr3e> Get-Content .\1.txt | Measure-Object -Word

Lines Words Characters Property 
----- ----- ---------- --------
       9999
```

## 5th (What 2 words are at index 551 and 6991 in the first file?)
```
PS C:\Windows\System32\3lfthr3e> Get-Content .\1.txt | Select -Index 551,6991
Red 
Ryder
```

## 6th (This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer))
```
PS C:\Windows\System32\3lfthr3e> Select-String .\2.txt -Pattern 'redryder' 

2.txt:558704:redryderbbgun
```