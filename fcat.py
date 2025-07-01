import os
import sys

if len(sys.argv) == 2:
    os.system(f"figlet {sys.argv[1]} | lolcat")
