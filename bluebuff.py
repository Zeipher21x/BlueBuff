#IMPORTS
from asyncio import subprocess
import os 
import socket 
import subprocess
import getpass

#SETTING OS VARIABLE 
operating = os.name

#ASCII ART FTW
motd = ("""
            ▄▄                                            ▄▄▄▄   ▄▄▄▄
▀███▀▀▀██▄▀███                    ▀███▀▀▀██▄            ▄█▀ ▀▀ ▄█▀ ▀▀
  ██    ██  ██                      ██    ██            ██▀    ██▀   
  ██    ██  ██ ▀███  ▀███   ▄▄█▀██  ██    █████  ▀███  █████  █████  
  ██▀▀▀█▄▄  ▓█   ██    ██  ▄█▀   ██ ██▀▀▀█▄▄ ██    ██   ██     ██    
  █▓    ▀█  ▓█   ▓█    ██  ▓█▀▀▀▀▀▀ █▓    ▀█ ▓█    ██   ▓█     ▓█    
  ▓▓    ▄█  ▓█   ▓█    █▓  ▓█▄    ▄ ▓▓    ▄█ ▓█    █▓   ▓█     ▓█    
  ▓▒    ▀▓  ▓▓   ▓█    ▓▓  ▓▓▀▀▀▀▀▀ ▓▒    ▀▓ ▓█    ▓▓   ▓▒     ▓▒    
  ▓▒    ▓▓  ▒▓   ▓▓    ▓▓  ▒▓▓      ▓▒    ▓▓ ▓▓    ▓▓   ▓▒     ▓▒    
▒ ▓▒ ▒ ▒ ▒▒ ▒ ▒  ▒▒ ▓▒ ▒▓▒  ▒ ▒ ▒▒▒ ▓▒ ▒ ▒ ▒ ▒▒ ▓▒ ▒▓▒▒ ▒▒▒  ▒ ▒▒▒   
 
                                          ▄▄            ▄▄                        
▀███▀▀▀██▄              ███▀▀▀███         ██           ███                        
  ██    ██              █▀   ███                        ██                        
  ██    ████▀   ▀██▀    ▀   ███   ▄▄█▀██▀███ ▀████████▄ ███████▄   ▄▄█▀██▀███▄███ 
  ██▀▀▀█▄▄ ██   ▄█         ███   ▄█▀   ██ ██   ██   ▀██ ██    ██  ▄█▀   ██ ██▀ ▀▀ 
  █▓    ▀█  ██ ▄▓         ███   ▄▓█▀▀▀▀▀▀ ▓█   ▓█    ██ ██    █▓  ▓█▀▀▀▀▀▀ █▓     
  ▓▓    ▄█   ██▓         ▓██   ▄█▓█▄    ▄ ▓█   ▓█    ▓█ █▓    █▓  ▓█▄    ▄ █▓     
  ▓▒    ▀▓   █▓▓         ▓▓█   ▓█▓▓▀▀▀▀▀▀ ▓▓   ▓█▓   ▓▓ ▓▓    ▓▓  ▓▓▀▀▀▀▀▀ ▓▓     
  ▓▒    ▓▓   ▓▓▒        ▓▓▓   ▓▓█▒▓▓      ▓▓   ▓█   ▓▓▓ ▓▒    ▓▒  ▒▓▓      ▓▒     
▒ ▓▒ ▒ ▒ ▒   ▓▓        ▒ ▒ ▒ ▒ ▒▓ ▒ ▒ ▒▒▒ ▒ ▒  ▒▓▒ ▒ ▒ ▒ ▒   ▒ ▒ ▒ ▒ ▒ ▒▒▒ ▒▒▒    
           ▒▒▓                                 ▒▒                                 
         ▒▒▒                                 ▒ ▒ ▒▒                               
         
version 0.3                                                                                           
""")
#OS CHECK FOR PROPER OS 
def detect_os():
    print ("-"*120)
    print ("Detecting For Linux To Run Script")
    print ("-"*120)

    if operating == "posix":
       os.system("clear")
       print(motd)
       print("System is running Linux")  
       print("Getting Date and Hostname: ") 
#PRINTS DATE TIME AND HOSTNAME FROM LOCALHOST
       os.system('date')   
       os.system("uptime")
       os.system('hostname')
    else:
        print ("This Script Is Only For Linux...")   
#LINUX UPGRADE & UPDATE 
def update_upgrade():
    print ("-"*120)
    print("Starting Update/Upgrade Module")
    print ("-"*120)

    update = input("Would You Like To Update? (yes/no) (REQUIRES SUDO)")
    if update == "yes":
        os.system("sudo apt-get update && sudo apt-get upgrade")
    elif update == "no":
        print ("-"*120)
        print ("Skipping Upgrade Sequence")        
        print ("-"*120)
#BACKUP LOG DIRECTORY
def backup_logs():
    print ("-"*120)
    print("Starting Backup_logs Module")
    print ("-"*120)


    name = input("Please enter your username for this account: ")
    print("Backing up logs to /home/" +name+ "/log_backups")
    os.system("mkdir log_backups")
    os.system("sudo rsync -a /var/log/   /home/" +name+ "/log_backups/")
    print("Backup Complete To bluebuff folder")

    view_logs_in_textfile =input("Would you like to search logs for suspicious keywords and save to a text file? ")
    if view_logs_in_textfile == "yes" or "Yes" or "y":
        with open('log_keywords.txt', 'w') as f:
            out = subprocess.run('sudo find  -name  "*.log"  | sudo cat /home/'+name+'/log_backups/auth.log | grep -E -i "sudo|cron|su|ssh"', shell=True, stdout=f, text=True)
            print ("-"*120)
            print ("log_keywords.txt saved to bluebuff folder")
            print ("-"*120)
    elif view_logs_in_textfile =="no" or "No" or "n":
        print ("-"*120)
        print ("Skipping Backup Sequence")        
        print ("-"*120)
#LOCALHOST SERVICE SCAN
def Nmap_scan():
    print ("-"*120)
    print("Starting Scanner Module")
    print ("-"*120)

    ask = input("Would You Like To Save Results To A Text File? *FYI: Saying No Will Print Scan Results To Console*")

    if ask == "yes" or "Yes" or "y":
        print ("-"*120)
        print("Starting Nmap Service Scan, Please Be Patience...")
        print ("-"*120)
        with open('Nmap_output.txt', 'a') as f:
            out = subprocess.run('nmap -sV localhost', shell=True, stdout=f, text=True)
    elif ask ==  "no" or "No" or "n":
        print ("-"*120)
        print("Starting Nmap Service Scan, Please Be Patience...")
        print ("-"*120)
        os.system("sudo nmap -sV localhost")
    print ("-"*120)
    print("Saved Nmap Scan To Local Directory")
    print ("-"*120)

#MAIN FOR CALLING ALL FUNCTIONS
def main():
    detect_os()
    update_upgrade()
    backup_logs()
    Nmap_scan()
#MAIN RUN 
if __name__ == '__main__':
    main()





