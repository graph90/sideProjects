import os
def rebootComputer():
    # reboot windows from wsl
    os.system("shutdown.exe -r -t 0")
rebootComputer()