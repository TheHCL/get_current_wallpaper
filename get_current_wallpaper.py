import os

current=os.getcwd()
app_folder=os.getenv('APPDATA')+"\\Microsoft\\Windows\\Themes\\CachedFiles"
os.chdir(app_folder)
files=os.listdir(app_folder)

for x in files:
    os.system("copy "+app_folder+"\\"+x+" "+current)