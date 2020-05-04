from sys import argv

# FUNCTIONS #

def resetVoicePassword():
    import hashlib
    code = raw_input("Reset Code: ")
    hashedcode = hashlib.sha256(code.encode()).hexdigest()
    hashedcode = hashedcode
    with open(".private/resetcode.txt") as rc:
        trueHashedCode = rc.read()
        if (hashedcode == trueHashedCode):
            print("OK!")
            vptrt = raw_input("New Voice Password: ")
            vptrtc = raw_input("Confirm Password: ")
            if (vptrt == vptrtc):
                print("Reseting password...")
                with open(".private/voice_pass.txt","wb") as f:
                    f.write(hashlib.sha256(vptrt.encode()).hexdigest())
            else:
                print("Your password does not match!\nTry again!")
                exit()
        else:
            print("Your reset code was invalid!")
            exit()


def install():
    import os
    import hashlib
    print("Installing... ")
    voice_password = raw_input("Enter a voice password: ")
    reset_code = raw_input("Enter a reset code: ")
    print("Creating directory '.private'...")
    os.mkdir(".private")
    print("Done creating directory '.private'...\n")
    print("Creating 'voice_pass.txt'...")
    with open(".private/voice_pass.txt","wb") as f:
        f.write(hashlib.sha256(voice_password.encode()).hexdigest())
    print("Done creating 'voice_pass.txt'...\n")
    print("Creating 'resetcode.txt'...")
    with open(".private/resetcode.txt","wb") as f:
        f.write(hashlib.sha256(reset_code.encode()).hexdigest())
    print("Done creating 'resetcode.txt'...\n")
    print("Installing Required Modules...")
    os.system("python3 -m pip install -r Lib/modules.lst")
    print("Done installing Required Modules...")
    print("\n")
    print("Done installing 'passwordcracker-master'!")
    exit()

if ( len(argv) <= 1):
    print("You must enter an option! [ install | reset ]")
    print("Illegal option!")
    print("Exited!")
    exit()
else:
    option = argv[1]
    if (option == "install"):
        install()
    elif (option == "reset"):
        resetVoicePassword()
    else:
        print("Options: [ install | reset ]")
        print("Illegal option!")
        print("Exited!")
        exit()