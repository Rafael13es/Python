import os 
  
shutdown = input("Do you wish to shutdown your computer? (yes / no): ") 
  
if shutdown == 'no': 
    exit() 
else:
    t = input("In how many hours do you want it to shutdonw?: ")
    print(t)
    t = str(int(t) * 3600)
    print("shutdown /s /t " + t)
    os.system("shutdown /s /t " + t)