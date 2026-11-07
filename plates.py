# REQUIREMENTS: 
# “All vanity plates must start with at least two letters.”
#  “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#  “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
#  vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#  “No periods, spaces, or punctuation marks are allowed.”



import re
import sys

plate = input("Plate: ").strip().upper()

if len(plate) < 2 or len(plate) > 6:
    print("exited after len")
    print("Bad input!")
else:
    pass

#THE PLATE CAN ONLY BE LETTER, LETTER, THEN OPTIONALLY ONLY LETTERS AND NO ZERO, THEN IT CAN BE ANY LETTER AND ANY ZERO

if test1 := re.search(r"^[A-Z]{2}[A-Z1-9]?[A-Z0-9]*$", plate):
    pass
else:
    print("Bad input!")
    sys.exit()

#CHECK EACH CHARACTER, IF THE FIRST NUMBER IT COMES TO IS A ZERO, THEN FAIL
  #this should flip to 1 when a non-zero digit has occurred. then zeros are allowed
zerochecker = 0
letterchecker = False
# if the next character is a letter, move to the next.
# if the next chacater is a number other than zero, add 1 to the zerochecker variable and go to the next character
# the only thing else it could be is zero, so check if zerochecker has already flipped to 1. If so, continue
# if it hasn't already flipped, the zero must be the first digit which is not allowed. end program.

for l in plate:
    if l.isalpha() == True:
        if letterchecker == False:
            pass
        else:
            print("Bad input!")
            sys.exit()
        pass
    elif l != "0":
        zerochecker = zerochecker + 1
        letterchecker = True
        pass
    elif zerochecker >= 1:
        letterchecker = True
        pass
    else:
        print("Bad input!")
        sys.exit()

print("Successful plate number!")