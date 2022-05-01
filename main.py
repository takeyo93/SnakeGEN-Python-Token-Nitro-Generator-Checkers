import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

from pystyle import Colorate, Colors, Write, Add, Center

CountNitro             = 0
num                    = 0
InvalidNitro           = 0
ValidNitro             = 0

os.system("title SnakeGEN, the fastest Generator/Checker on the world in 2022.")


banner = r"""
                                            

                         _        
                        | |                 //   ) )  //   / /  /|    / /                             _,.--. 
         ___ _ __   __ _| | _____          //        //____    //|   / /         --..,_           .'`__ o  `;__,
        / __| '_ \ / _` | |/ / _ \        //  ____  / ____    // |  / /             `'.'.       .'.'`  '---'`  '
        \__ \ | | | (_| |   <  __/       //    / / //        //  | / /                '.`-...-'.'
        |___/_| |_|\__,_|_|\_\___|      ((____/ / //____/ / //   |/ /                    `-...-'                                 

                                                
                                                                    
"""[1:]

os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.GREEN + (banner))
print(Fore.WHITE +Fore.GREEN +"                         ["+Fore.GREEN +Fore.GREEN +"+"+Fore.GREEN +Fore.GREEN +"]"+ Fore.GREEN +Fore.GREEN +"-------------------------------------------------------"+ Fore.GREEN +Fore.GREEN +"["+ Fore.GREEN +Fore.GREEN +"+"+ Fore.GREEN +Fore.GREEN +"]")
print(Fore.WHITE +Fore.GREEN +"                                    Hello !"+Fore.WHITE+" What Do You Want? ")
print(Fore.WHITE +Fore.GREEN +"                             [1] "+Fore.WHITE+"Token Generator (without Checker)")
print(Fore.WHITE +Fore.GREEN +"                             [2] "+Fore.WHITE+"Nitro Generator (without Checker)")
print(Fore.WHITE +Fore.GREEN +"                             [3] "+Fore.WHITE+"Checker (Checks all nitros or tokens you generated)")
print(Fore.WHITE +Fore.GREEN +"                         ["+Fore.GREEN +Fore.GREEN +"+"+Fore.GREEN +Fore.GREEN +"]"+ Fore.GREEN +Fore.GREEN +"-------------------------------------------------------"+ Fore.GREEN +Fore.GREEN +"["+ Fore.GREEN +Fore.GREEN +"+"+ Fore.GREEN +Fore.GREEN +"]")
opcion = input("\n[+] Choice >> ")
if opcion=='1':
	os.system("cls")
	print(banner)
	cantidad = Write.Input("\n[?] How many Token(s) you want to generate? -> ", Colors.green_to_white, interval=000.001)
	while int(count)<int(cantidad):
		Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		f= open(current_path +"/"+str("Tokens")+str("")+".txt","a")
		f.write(Generated+"\n")
		print(Fore.GREEN +f"[i] Sended {count} Token >> "+ Fore.RESET + Generated)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.GREEN +Fore.GREEN +"[!] Tokens Generated Successfully and Saved in Tokens.txt!")
			input(Fore.GREEN +Fore.GREEN +"\n[+] Press Enter to Exit.")
			os.system("cls")
			print(Fore.WHITE +Fore.GREEN +"                         ["+Fore.WHITE +Fore.GREEN +"+"+Fore.WHITE +Fore.GREEN +"]"+ Fore.WHITE +Fore.GREEN +"-------------------------------------------------------"+ Fore.WHITE +Fore.GREEN +"["+ Fore.WHITE +Fore.GREEN +"+"+ Fore.WHITE +Fore.GREEN +"]")
			print(Fore.GREEN +Fore.GREEN +"                                                 [...] Closing SnakeGEN..")
			print(Fore.WHITE +Fore.GREEN +"                         ["+Fore.WHITE +Fore.GREEN +"+"+Fore.WHITE +Fore.GREEN +"]"+ Fore.WHITE +Fore.GREEN +"-------------------------------------------------------"+ Fore.WHITE +Fore.GREEN +"["+ Fore.WHITE +Fore.GREEN +"+"+ Fore.WHITE +Fore.GREEN +"]")
			time.sleep(2)
			sys.exit()
pass
if opcion=='2':
  os.system("cls")
  print("")
  print(Fore.GREEN + (banner))
  time.sleep(0.1)
  print(Fore.GREEN + "[>..] SnakeGEN, the fastest Nitro Generator on the world in 2022.")
  print("")
  time.sleep(0.1)

  print("")
  num = int(Write.Input('[?] How many Nitro(s) you want to generate? -> ', Colors.green_to_white, interval=000.001))

  with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
     print("")
     print("")
     print("")


     start = time.time()
    

     for i in range(num):
         code = "".join(random.choices(
             string.ascii_uppercase + string.digits + string.ascii_lowercase,
             k = 16
         ))

         file.write(f"https://discord.gift/{code}\n")

     print(Fore.GREEN + "[...] Your Nitro(s) are being generated..")
     print("")
     print("")


     with open("Nitro Codes.txt") as file:
       for line in file.readlines():
         nitro = line.strip("\n")

         count +=1
         print(Fore.GREEN + f" [i] Sended {count} Nitro >> "+ Fore.RESET + f'  {nitro}')

  print("")
  print("")

  input(Fore.GREEN + "[!] All Nitro(s) is generated ! For quit SnakeGEN Press Enter.")

  keep_alive.keep_alive()

pass
if opcion=='3':
	os.system("cls")
	print("\n" + banner + "\n")
tokenornitro = Write.Input("[?] Check Nitro or Token? (n/t) -> ", Colors.green_to_white, interval=000.001)
print("")
print("")
if tokenornitro=='t':
 with open('Tokens.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.RED}[x] Invalid Token Found! >>{Fore.RESET} ' + token)
	            else:
	                print(f'{Fore.LIGHTGREEN_EX}[v] Valid Token Found! >>{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.CYAN}[404] ERROR 404..{Fore.RESET}")

pass
if tokenornitro=='n':   
    with open("Nitro Codes.txt") as f:
        number_line=0
        for line in f:
            nitro = line.strip("\n")
            number_line += 1
            os.system(f'title {number_line}')
 
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
 
            r = requests.get(url)
 
            if r.status_code == 200:
                print(Fore.GREEN+" Valid | {} ".format(line.strip("\n"))+Fore.RESET)
                with open('Valid Nitro Codes.txt' + 'w+') as f:
                    f.write(nitro)
                break
            else:
                pass
                
                print(Fore.RED+" Invalid | {} ".format(line.strip("\n"))+Fore.RED)
    print('tout à étais check ')
    time.sleep(2.8)
pass
