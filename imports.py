import os
import sys
import time
import json
import argparse
import logging
import logging.handlers
import subprocess
import re
import signal
import socket
import struct
import ipaddress
import threading
import multiprocessing
import multiprocessing.pool
import concurrent.futures
import concurrent.futures.thread
import concurrent.futures.process
import webbrowser

from datetime import datetime
from datetime import timedelta

print("Dividing and Multiplying numbers by 8")
time.sleep(1)
print("\n\n\n\n")

# Tell the user how to make a struct
print(struct.calcsize("P") * 8)
# Make a calculator
print(struct.calcsize("P") * 8)
# Make a calculator
print(struct.calcsize("P") * 8)
# Make a calculator
print(struct.calcsize("P") * 8)
# Tell the user what 8 divides into
print(8 % struct.calcsize("P") * 8)
# Tell the user what 8 multiplies into
print(8 * struct.calcsize("P") * 8)
# Allow the user to input a number
number = int(input("Enter a number: "))
# Use the number variable and allow the user to multiply it
print(number * 8)
# Use the number variable and allow the user to divide it
print(number / 8)
# Use the number variable and allow the user to pick a number to divide it by
print(number / int(input("Enter a number to divide by: ")))
# Use the number variable and allow the user to pick a number to multiply it by
print(number * int(input("Enter a number to multiply by: ")))
# Ask the user if they would kill someone, y/n
kill = input("Would you kill someone, y/n: ")
if kill == "y":
    # send the user to google.com
    webbrowser.open("google.com")

if kill == "n":
    # end the program
    print("The program will now end")
