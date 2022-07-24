import time
import sys
score = 0 
quizsummary = []
def write(str, eol = "\n"):
    for char in str:
        time.sleep(.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()


write("Welcome to the Hip-Hop Music Quiz for Cultured Individuals!")
write("This quiz is open book, e.g. You may search the answers. ")
write("Answering Disclaimer: Please answer in lowercase writing and use no symbols")

write("START QUIZ: ")

#question1
write("1. What artist group created the 1999 album 'Enter the Wu-Tang 36 Chambers'? (2 words) ")
answer = input(">")
if answer == "wutang clan":
 write("Correct!")
 score += 1 
else:
  write("Incorrect, next question. ")

#question2
write("2. How old was Joey Bada$$ when he realesed his album '1999'? (2 digits) ")
answer = input(">")
if answer == "17":
 write("Correct!")

 



