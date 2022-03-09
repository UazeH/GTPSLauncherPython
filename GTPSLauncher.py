import time
import os

def list():
    os.system("title List Menu")
    os.system("color 0c")
    os.system('cls')
    print("""[+] Menu :
    
[1] Turn ON GTPSLauncher
[2] Turn OFF GTPSLauncher
""")

    pilih = input("[>] Select Menu: ")

    if pilih == "1":on()
    elif pilih == '2':off()
    else:
        os.system("cls")
        print("Menu Not Available!")
        print(" ")
        y = input("Back To List Menu? (y/n): ")
    if y == "y":
        list()

def on():
    f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w")
    f.write(f"youripserver growtopia1.com\nyouripserver growtopia2.com\n")
    f.close()

    print("Please wait......")
    time.sleep(5)

    os.system("cls")
    print("GTPSLauncher has been turned ON")
    y = input("Back To List Menu? (y/n): ")
    if y == "y":
        list()

def off():
    f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w")
    f.write(f"")
    f.close()

    print("Please wait......")
    time.sleep(5)

    os.system("cls")
    print("GTPSLauncher has been turned OFF")
    y = input("Back To List Menu? (y/n): ")
    if y == "y":
        list()

list()
