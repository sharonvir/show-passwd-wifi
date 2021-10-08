# Creator : MRD3F417
# BlackGuard Team - Discord : discord.gg/4DbuQRg6YX
# Python 3 - Windows / Linux
# Show All Password Wifi Any Sys

import subprocess
import re
from colorama import Fore
import platform , os
import time
def wifi():
    netsh_output = subprocess.run(
        ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

    profile_names = (re.findall("All User Profile     : (.*)\r", netsh_output))

    wifi_list = []
    
    if len(profile_names) != 0:
        for name in profile_names:

            wifi_profile = {}

            profile_info = subprocess.run(
                ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                password = re.search(
                    "Key Content            : (.*)\r", profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]

                wifi_list.append(wifi_profile)
        
    for x in range(len(wifi_list)):
       
        print(wifi_list[x])
    input('')
def passwords():
    data0 = platform.uname()[0]
    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    p = input("Sir ! Enter the Password:")
    if p == 'blackguard':
        print(Fore.GREEN + '[+]' + Fore.WHITE + 'Wellcome Back ...')
        print("")
        print("")
        print("[!] Dont Copy Kid - I See You - Discord : MƦ.Ɗ3Ƒ417#8277")
        print("""
    
███╗░░░███╗██████╗░░░░██████╗░██████╗░███████╗░░██╗██╗░░███╗░░███████╗
████╗░████║██╔══██╗░░░██╔══██╗╚════██╗██╔════╝░██╔╝██║░████║░░╚════██║
██╔████╔██║██████╔╝░░░██║░░██║░█████╔╝█████╗░░██╔╝░██║██╔██║░░░░░░██╔╝
██║╚██╔╝██║██╔══██╗░░░██║░░██║░╚═══██╗██╔══╝░░███████║╚═╝██║░░░░░██╔╝░
██║░╚═╝░██║██║░░██║██╗██████╔╝██████╔╝██║░░░░░╚════██║███████╗░░██╔╝░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚═╝░░░░░░░░░░╚═╝╚══════╝░░╚═╝░░░  """)
        print("")
        print("")
        time.sleep(2)
        wifi()
    else:
        print()
        print('This is not password')
        print()
        time.sleep(1)
        passwords()

passwords()
