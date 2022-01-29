#!/usr/bin/python3

from os import system

print("""	     #####  Simple Mac Address Changer  #####\n
               ##    By: Abd Almoen Arafa    ##
               ##    Age: 15                 ##\n""")
system("macchanger -s eth0")
interface=input("\nEnter The Interface: ")
quit() if not interface else None
ask=input("Do you want a random Mac Address or manually change? (ran,man): ")
quit() if not ask else None
if ask.lower() == "man" or ask.lower() == "manually":
	Mac=input("Enter The Mac Address you want to change to: ").strip()
	quit() if not Mac else None
	system(f"ifconfig {interface} down"),system(f"ifconfig {interface} hw ether {Mac}"),system(f"ifconfig {interface} up"),system(f"macchanger -s {interface}")
elif ask.lower() == "ran" or ask.lower() == "random":	system(f"macchanger -r {interface}")
#By: Abd Almoen Arafa
#Age: 15

