from random import *
from os import system
from time import sleep



def write_pwd_in_file(pwd, place):
    with open("results.txt", "a") as file:
      file.write(place+':\n')
      file.writelines(pwd)
      file.write('\n')
def sc():
    sleep(0.5)
    system('clear')
def farewell():
    system('clear')
    print('''█████░
 █   ▒█
 █    █ █░  █   ███
 █   ▒█ ▓▒ ▒▓  ▓▓ ▒█
 █████░ ▒█ █▒  █   █
 █   ▒█  █ █   █████
 █    █  █▓▓   █
 █   ▒█  ▓█▒   ▓▓  █
 █████░  ▒█     ███▒
         ▒█
         █▒
        ██''')
    sleep(1.5)
    system('clear')
    exit()
try:
    
    print(''''█████░   ██    ▓███▒        █    █ ██████ █
 █   ▓█   ██   █▓  ░█        █    █ █      █
 █    █  ▒██▒  █             █    █ █      █
 █   ▓█  ▓▒▒▓  █▓░           █    █ █      █
 █████░  █░░█   ▓██▓         ██████ ██████ █
 █       █  █      ▓█  ███   █    █ █      █
 █      ▒████▒      █        █    █ █      █
 █      ▓▒  ▒▓ █░  ▓█        █    █ █      █
 █      █░  ░█ ▒████░        █    █ ██████ ██████''')
    print('~~~This programm will generate password for you ;)~~~')
    print('~'*35)
    while True:
            cntn = input('Start the programm? [ y / n ]  ').lower()
            if cntn != 'y':
                farewell()
            pwd = []
            place = input('Enter the site or app where you want to make a password:  ')
            print('~'*35)
            pwd_length = int(input('Enter the length of password:   '))
            print('~'*35)
            numbers = input('Include  numbers? [ y / n ]   ')
            print('~'*30)
            lletters = input('Include lower register of letters? [ y / n ]   ')
            print('~'*30)
            hletters = input('Include high register of letters? [ y / n ]    ')
            print('~'*30)
            symbol = input('Include  symbols? [ y / n ]   ')
            print('~'*30)
            sc()
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            symbols = ['.', ',', '~', '@', '#', '$', '%', '^', '&', '*', '-', "'", '"', '!', '?', ':', '+', '/']
            integer = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            for i in range(201):
                if numbers == 'y':
                    pwd.append(str(choice(integer)))
                if lletters == 'y':
                    pwd.append(str(choice(alphabet)))
                if hletters == 'y':
                    pwd.append(str(choice(alphabet).upper()))
                if symbol == 'y':
                    pwd.append(str(choice(symbols)))
            sh = input('shuffle list? [ y / n ]  ')
            while sh == 'y':
                pwd = sample(pwd, k=len(pwd))
                print('•'*23)
                sh = input('Once again? [ y / n ]  ')
            sc()
            pwd = pwd[:pwd_length]
            write_pwd_in_file(pwd, place)
            print('|'*124)
            print()
            print('~~~~~~~~~>  YOUR PASSWORD IS', ''.join(pwd),  '<~~~~~~~')
            print()
            print('|'*124)
            print()
            print("Password and password's place were saved in file - results.txt\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\niF You want to see your passwords, just stop the programm and enter this command -  cat results.txt\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nIf you want to delete some passwords stop the programm and enter this command -    nano results.txt")
            print()
            cntn = input('Continue? [ y / n ]  ')
            if cntn != 'y':
                farewell()
except KeyboardInterrupt:

    system('clear')
    print('You entered Ctrl + c (or Ctrl + z)')
    farewell()
