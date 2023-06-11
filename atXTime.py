import time,os
breakTime = "19:42:00"
def getTime():
    return time.strftime("%H:%M:%S")
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def f():
    
print(getTime())
iteration = 0

while True:
    print(iteration)
    if getTime() == breakTime:
        clearScreen()
        print("Time stopped at:" + getTime())
        f()
        break
    iteration += 1