import os
import shutil
print(os.getcwd())
os.mkdir("source")
file=open("source/new.txt",'x')
file.close()
os.mkdir("destination")
try:
    shutil.copy("source/new.txt", "destination/new.txt")
except FileNotFoundError:
    print("no file found in source")
except FileExistsError:
    print("File with same name already exists")
except :
    print("An error occured")     