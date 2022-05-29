import time
import sys
numberlist = []
def write(str, eol = "\n"):
    for char in str:
        time.sleep(.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()

write("Welcome to the Hip-Hop Music Quiz for Cultured Individuals!")

q1 = input("")
q2 = input("")
q3 = input("")