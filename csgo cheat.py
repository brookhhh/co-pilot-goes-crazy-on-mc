import pymem
import pymem.process
import os
from pywinauto import Desktop

# Welcome user to the cheating client
print("Welcome to the Cheating Client!")
print("This client is designed to help you cheat in the game.")
print("Please make sure you have the latest version of the game.")
print("If you have any questions, please contact me at: brook@skidders.wtf")
print("")


# Check if csgo is running in background using pywinauto
if Desktop(backend="win32").windows(title="Counter-Strike: Global Offensive"):
    print("CSGO is running in background!")
     # Ask user if its okay to run the cheat
    print("")
    print("Are you sure you want to run the cheat?")
    print("If you are not sure, please enter (n) in the next input")
    print("If you are sure, please enter (y) in the next input")
    print("")
    option = input("Are you sure? (y/n): ")
    if option == "y":
        print("")
        print("Starting the cheat...")
        print("")
        # Start the cheat
        os.system("start \\Users\\brook\\Desktop\\Cheat\\main.exe")

    elif option == "n":
        print("")
        print("Exiting...")
        print("")
        # Exit the program
        exit()
elif (Desktop(backend="win32").windows(title="Counter-Strike: Global Offensive" != True)):
    print("CSGO is not running in background!")
    print("")
    print("Exiting...")
    print("")
    # Exit the program
    exit()
