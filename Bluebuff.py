import os 
operating = os.name
os.system("clear")


print("""
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
                                                                     
                        
""")




    
if operating == "posix":
    print("System is running Linux")  
    print("Getting Date and Hostname: ") 
    os.system('date')   
    os.system("uptime")
    os.system('hostname')
    update = input("Would You Like To Update? (yes/no) (REQUIRES SUDO)")
    if update == "yes":
        os.system("sudo apt-get update && sudo apt-get upgrade")
    elif update == "no":
        input("Please Press Enter To Exit: ")
else:
    print("This Only Runs ON LINUX!")        
