# Hash Cracker
## Overview
This script is a basic password cracker that utilizes multiple threads to search for a specific hashed password within a given wordlist. It uses the MD5 hashing algorithm to compare hashed passwords and find a match for a given target hash.

## Requirements

 - Python 3.x
 - `concurrent.futures`
 - `hashlib`
 - `json`

## How to use
**Setup:**

 - Ensure Python3.x is installed
 - Create a wordlist file `wordlist.txt`, The default wordlist file consists of the top 100 most common passwords
 - Edit the `config.json` file to define the number of threads, the wordlist file path, and the target hash to crack. This is the format of the configuration file:
```
{

"threads": <threads>,

"wordlist": "wordlist.txt",

"target": <target>

}
```
The default value for target is the md5 hash of the text `password123`

**Running the script**

 - To run the script, type `python3 main.py`
 - If you recieve a `ModuleNotFoundError` error, run:
 `pip3 install -r requirements.txt`

**Usage notes**
-   Ensure the wordlist file contains a comprehensive list of passwords for effective password cracking.
-   Adjust the number of threads based on system capabilities and performance requirements.

**Disclamer**
This script is intended for educational and ethical testing purposes only. Ensure you have the legal right to use the provided password list and respect privacy and security laws when using this script. Do not use this script, without permission of the 'target'
