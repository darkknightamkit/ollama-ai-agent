import os

START = "\033[91m]"
END = "\033[0m"

def log(text):
    if os.getenv("DEBUG") == True:
     print(f"  {START}{text}{END}")
 