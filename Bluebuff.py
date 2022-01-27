#IMPORTS
import os 
import socket 
#SETTING HOST AND PORT SETTINGS FOR BASIC PORT SCAN
hosts = ["Localhost"]
ports = [22, 23, 80, 443, 445, 3389]
#SETTING OS VARI
operating = os.name


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
         
 version 0.1                                                                     
                        
""")


#IF STATEMENT TO DETERMINE OS  

if operating == "nt":
    print("System is running Windows")
    print("Getting Date and Hostname: ")
    os.system('echo %date%-%time%')   
    os.system('hostname')
    input("Please press enter to continue with localhost scan: ")
    
elif operating == "posix":
    os.system("clear")
    print(motd)
    print("System is running Linux")  
    print("Getting Date and Hostname: ") 
    #PRINTS DATE TIME AND HOSTNAME FROM LOCALHOST
    os.system('date')   
    os.system("uptime")
    os.system('hostname')
    #START LINUX UPDATE/UPGRADE 
    update = input("Would You Like To Update? (yes/no) (REQUIRES SUDO)")
    if update == "yes":
        os.system("sudo apt-get update && sudo apt-get upgrade")
    elif update == "no":
        input("Please Press Enter To Countinue with scanning: ")
    #BASIC SCANNER FUNCTION TO RETURN OPEN PORTS IN DEFINED VARIBLES SET EARLIER  
    for host in hosts:
     for port in ports:
        try:
            print ("[+] Connecting to " + host + ":" + str(port))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, port))
            if result == 0:
                print ("  [*] Port " + str(port) + " open!")
            s.close()
        except:
            pass
     
