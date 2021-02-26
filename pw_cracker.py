#Author:SoeZayZay
#Dtae :23/2/2021
import hashlib
import pyfiglet
banner = pyfiglet.figlet_format("PW-Cracker",font="slant")
print(banner)
found  = False
hash_password = input("       Enter Your SHA-256 Password : ")
print("")
path   = input("       Enter Your Wordlist File    : ")
file   = open(path)
password_list = []
char   = file.readlines()
for word in char:
    pw = word.strip()
    password_list.append(pw)
for passwd in password_list:
    encrypt_pass=passwd.encode("utf-8")
    password    =hashlib.sha256(encrypt_pass).hexdigest()
    print(f"            [=============== Cracking ==> {passwd}")
    if password == hash_password:
       print("")
       print(f"                   Password is {passwd}")
       print("")
       found = True
       break;
      
if found==False:
   print("")
   print("                     Password not found!")
   print("")
      
    
