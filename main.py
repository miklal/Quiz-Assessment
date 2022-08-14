#type witing function
import time
import sys

#end of quiz code
score = 0
quizsummary = []

#type writing function
def write(str, eol="\n"):
    for char in str:
        time.sleep(.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()

#introduction
write("Welcome to the Hip-Hop Music Quiz for Cultured Individuals!")
write("This quiz was created to be difficult and very specific. You have been warned. ")
write("This quiz is open book, e.g. You may search the answers. ")
write(
    "Answering Disclaimer: Please answer in lowercase writing and use no symbols or punctuation. "
)

write("START QUIZ: ")

#question1
#if answered correctly it adds 1 point to score, if answered incorrectly there will be no points to be added. No matter the outcome of answer the quiz will forward to next question. The code for each question is the same.
write(
    "1. What artist group created the 1999 album 'Enter the Wu-Tang 36 Chambers'? (2 words) "
)
answer = input(">")
if answer == "wutang clan":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'wutang clan', next question. ")

#question2
write(
    "2. How old was Joey Bada$$ when he realesed his album '1999'? (2 digits) "
)
answer = input(">")
if answer == "17":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was '17', next question. ")

#question3
write("3. What year did Tupac Shakur pass away? (4 digits) ")
answer = input(">")
if answer == "1996":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was '1996', next question. ")

#question4
write("4. Quasimoto is the alter ego of who? (1 word) ")
answer = input(">")
if answer == "madlib":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'madlib', next question. ")

#question5
write(
    "5. L*Roneous and Da'Versifier had success with what 2002 album? (1 word) "
)
answer = input(">")
if answer == "imaginarium":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'imaginarium', next question. ")

#question6
write(
    "6. How many volumes of 'Metal Fingers Presents: Special Herbs:' by MF DOOM were released? (1 digit) "
)
answer = input(">")
if answer == "8":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was '8', next question. ")

#question7
write(
    "Methodman released his first studio album in 1994 titled 'Tical'. What does 'Tical' stand for? (5 words) "
)
answer = input(">")
if answer == "taking into consideration all lives":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'taking into consideration all lives', next question. ")

#question8
write(
    "'Supreme Clientle' is an album released in 2000 by what member of the Wu-Tang Clan? (2 words) "
)
answer = input(">")
if answer == "ghostface killah":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'ghostface killah', next question. ")

#question9
write(
    "An album simply titled 'Bread' featuring Westside Gunn, Conway the Machine, Roc Marciano, Black Thought and Earl Sweatshirt was created and produced by who? (2 words)"
)
answer = input(">")
if answer == "the alchemist":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'the alchemist', next question. ")

#question10
write("Mos Def and Talib Kweli are? (1 word) ")
answer = input(">")
if answer == "blackstar":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'blackstar', next question. ")

#question11
write("Stones Throw is a hiphop record label. Who is founder/owner? (3 words)")
answer = input(">")
if answer == "peanut butter wolf":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'peanut butter wolf', next question. ")

#question12
write(
    "Mobb Deep is an infamous hiphop duo. What is the name of their most prominent album? (2 words) "
)
answer = input(">")
if answer == "the infamous":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'the infamous', next question. ")

#question13
write(
    "How many volumes of 'Hitler Wears Hermes:''by Westside Gunn have been released? (1 digit)/(1 digit, 1 word, 1 letter"
)
answer = input(">")
if answer == "8":
    write("Correct!")
if answer == "8 side b":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was '8'/'8 side b', next question. ")

#question14
write(
    "Madlib and Jdilla came together to form 'Jaylib'. What is the name of their 2003 album? (2 words) "
)
answer = input(">")
if answer == "champion sound":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'champion sound', next question. ")

#question15
write(
    "Before becoming a rapper Action Bronson, an american rapper had success in what profession? (1 word) "
)
answer = input(">")
if answer == "chief":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'chief', next question. ")

#question16
write(
    "The legendary collaboration between Madlib and MF DOOM brought forth what 2004 album? (1 word) "
)
answer = input(">")
if answer == "madvilliany":
    write("Correct!")
    score += 1
else:
    write("Incorrect, the correct answer was 'madvilliany', next question. ")

if score == 1:
    quizsummary.append("+ 1 score")

elif score >= 2:
    quizsummary.append("You scored {} correct! ".format(score))
    print(quizsummary)
