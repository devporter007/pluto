import os
import zipfile
# TRY TO GET USERNAME OF THE RUNNING ENVIROMENT
username = os.getlogin()

#VERIFY USERNAME AND COPING MECHANISM
if os.path.exists("C:\\Users\\"+ username):
    pass
else:
    #IN CASE USERNAME DOES NOT EXIST
    i=0
    while i==0:
        username = input("Enter your username: ")
        if os.path.exists("C:\\Users\\"+ username):
            i=1
            break
        else:
            print("Username not found")
            continue
print("Hello "+username)
print("Step-1 : Turning off Windows Defender...")
print("Due to sensitive nature of command, you need to manually turn off windows defender. Press enter once done..")
print("")
print("Step-2 : Turning off firewall...")
os.system("NetSh Advfirewall set allprofiles state off")
print("")
print("Step-3 : Installing Anydesk and Sunshine...")
os.system(f"curl -L -o C:\\Users\\{username}\\Desktop\\Anydesk.exe https://download.anydesk.com/AnyDesk.exe")
os.system(f"curl -L -o C:\\Users\\{username}\\Desktop\\sunshine.zip https://github.com/loki-47-6F-64/sunshine/releases/download/v0.11.1/Sunshine-Windows.zip")
with zipfile.ZipFile(f"C:\\Users\\{username}\\Desktop\\sunshine.zip", 'r') as zip_ref:
    zip_ref.extractall(f"C:\\Users\\{username}\\Desktop\\Sunshine\\")
rgsc_input = input("Do you want to install Rockstar Games Launcher? (y/N): ")
if rgsc_input == "y" or rgsc_input == "Y" or rgsc_input == "yes" or rgsc_input == "Yes" or rgsc_input == "YES":
    print("Step-3(O) : Installing Rockstar Games Launcher")
    os.system(f"curl -L -o C:\\Users\\{username}\\Desktop\\RGL.exe https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe")
print("Step-4 : Installing CB Launcher...")
os.system(f"mkdir \"C:\\Users\\{username}\\Desktop\\CB Launcher\"")
os.system(f"curl -L -o \"C:\\Users\\{username}\\Desktop\\CB Launcher\\CB.Launcher.exe\" https://github.com/devporter007/binarybuildscb/releases/download/1.0/CB.Launcher.exe")
print("Step-5 : Starting Sunshine...")
print("Launch urself...")
if rgsc_input == "y" or rgsc_input == "Y" or rgsc_input == "yes" or rgsc_input == "Yes" or rgsc_input == "YES":
    print("Step-5(A) : Installing RGL...")
    os.system(f"C:\\Users\\{username}\\Desktop\\RGL.exe")
