import os
import shutil
print(os.getcwd())
os.mkdir("NEW")
file=open("NEW/new.txt",'x')
file.close()
os.mkdir("NEW_folder")
shutil.copy("NEW/new.txt", "NEW_folder/new.txt")
