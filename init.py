import os
import termcolor as tc
import term as t
from time import sleep
import requests
import ext
import platform
os.system("cls")
t.write("█")
sleep(2)
os.system("cls")
welcome = tc.colored("Welcome to pyOS!", "blue")
tx = "(c) 2023 AzureTecDevs"
ver = tc.colored(f"Version 1.0.0 {tx}", "dark_grey")
print(f"{welcome}\n{ver}\n\n")
while True:
    i = input("$ ")
    try:
        if i.lower() == "python":
            os.system("python")
        elif i.lower() == "help":
            print("""
python  : Run Python           exit    : Exit pyOS            
reset   : Restart              clear   : Clear screen         
pkg     : Install package      pkg run : Run package          
pkg info: Get package info""")
        elif i.lower() == "reset":
            os.system("cls")
            os.system("python init.py")
        elif i.lower() == "clear":
            os.system("cls")
            print(f"{welcome}\n{ver}\n\n") 
        elif i.lower() == "pkg":
            z = input("Package Name: ").lower()
            if not os.path.exists(f'pkg/{z}'):
                os.mkdir(f'pkg/{z}')
            url = f'https://raw.githubusercontent.com/AzureTecDevs/pyOS-Windows/packages/pkg/{z}/{z}.py'
            r = requests.get(url, allow_redirects=True)
            open(f'pkg/{z}/{z}.py', 'wb').write(r.content)
            url = f'https://raw.githubusercontent.com/AzureTecDevs/pyOS-Windows/packages/pkg/{z}/about'
            r = requests.get(url, allow_redirects=True)
            open(f'pkg/{z}/about', 'wb').write(r.content)
        elif i.lower() == "pkg run":
            z = input("Package Name: ").lower()
            os.system(f'python pkg/{z}/{z}.py')
        elif i.lower() == "pkg info":
            z = input("Package Name: ").lower()
            f = ext.readFile(f'pkg/{z}/about')
            print(f'Description: {f[0]}\nAuthor: {z[1]}')
    except:
        print('Fatal Error')
