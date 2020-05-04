from colorama import Fore as colors
from os import getuid
from crypt import crypt
from sys import argv
from spwd import getspnam
import time
import speech_recognition as sr
import pyttsx3
import os

def main():

    if ( getuid() != 0 ):
        print(colors.RED + "You must be root to run this utility.")
        exit(1)

    if ( len(argv) <= 1 ):
        username = input( colors.YELLOW + "What user should we try and crack the password? : ")
    else:
        username = argv[1]
    
    print(colors.CYAN + "Cracking UNIX password for user... " + username)

    dict_file = open("dictionary.txt")
    encrypted_password = getspnam(username)[1]

    print(colors.CYAN + "Encrypted password looks to be: " + colors.YELLOW + encrypted_password)
    print(colors.GREEN + "Presueing in 3 seconds!")
    time.sleep(3)
    count = 0

    for password in dict_file.readlines():
        password = password.rstrip()
        new_password = crypt(password,encrypted_password)

        print(colors.YELLOW + "Trying password " + colors.MAGENTA + password + colors.YELLOW + "...")

        if ( encrypted_password == new_password ):
            print(colors.GREEN + "Password found!\n")
            print(colors.YELLOW + "Password found in " + colors.CYAN + str(count) + colors.CYAN + " Attempts!\n")
            print(colors.RESET + "The" + colors.LIGHTMAGENTA_EX +  " cracked " + colors.RESET + "password is: " + colors.LIGHTGREEN_EX +  password)
            exit(0)
        else:
            print(colors.RESET + "Password failed! " + colors.RED + password)
            count += 1
    
    print(colors.RESET + "No password crack was found... ")
    exit(1)


def checkVoice():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system("clear")
        print("PASSWORD");
        audio = r.listen(source)
        gp = (r.recognize_google(audio));
        print("Given password is: " + gp)
        import hashlib
        gphashed = hashlib.sha256(gp.encode()).hexdigest()
        try:
            with open(".private/voice_pass.txt") as f:
                code = f.read()
                if (gphashed == code):
                    main()
                else:
                    print(colors.RED + "PASSWORD DENIED!")
                    exit()
        except KeyboardInterrupt:
            print("Interrupt!")
            exit()


checkVoice()
