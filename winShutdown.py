# shutdown windows through linux subsystem
import os
def shutdown():
    os.system("shutdown.exe -s -t 0")
shutdown()