# Passwordcracker-master


# Installation:

    $ python setup.py install

# Steps:
    1) Enter the voice password what you want to use.
    2) Enter your reset code for the voice password.
    3) Now it's installing.
# Output:
    Installing... 
    Enter a voice password: password
    Enter a reset code: 123
    
    Compiling...
    
    Creating directory '.private'...
    Done creating directory '.private'...
    
    Creating 'voice_pass.txt'...
    Done creating 'voice_pass.txt'...
    
    Creating 'resetcode.txt'...
    Done creating 'resetcode.txt'...

    Installing Required Modules...
    Requirement already satisfied: colorama in /usr/lib/python3/dist-packages (from -r lib/modules.lst (line 1)) (0.4.3)
    Requirement already satisfied: SpeechRecognition in /home/bob/.local/lib/python3.8/site-packages (from -r lib/modules.lst  (line 2)) (3.8.1)
    Requirement already satisfied: pyttsx3 in /home/bob/.local/lib/python3.8/site-packages (from -r lib/modules.lst (line 3))      (2.87)
    Done installing Required Modules...


    Done installing 'passwordcracker-master'!


# PASSWORD RESETTING:

    $ python setup.py reset

# Steps:
    1) Enter your current resetcode.
    2) Enter your new voice password.
    3) Confirm your new voice password.
    4) Resetted!

# USAGE:

    $ sudo python cracker.py [username | nothing]

# COPYRIGHT:

All rights reserved.

By Skyfight
