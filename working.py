# In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
# Note that you can format an int with leading zeroes with code like
# print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.
#example inputs: 9:00 AM to 5:00 PM returns 9:00 to 17:00
# 9 AM to 5 PM  returns 09:00 to 17:00
#program to expect AM and PM will be capitalized with no periods!



import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if re.search(r"^[0-9]{1,2}:?[0-9]?[0-9]? A?P?M to [0-9]{1,2}:?[0-9]?[0-9]? A?P?M$", s):
        pass
    else:
        raise ValueError


    left, right = s.split(" to ")
    leftnumber, lampm = left.split(" ")
    rightnumber, rampm = right.split(" ")
    if ":" in leftnumber:                                               #This section covers if the user uses a colon
        leftnumsplithour, leftnumsplitminute = leftnumber.split(":")
        leftnumsplithour = int(leftnumsplithour)
        leftnumsplitminute = int(leftnumsplitminute)
        if lampm == "PM" and leftnumsplithour < 12:
            leftnumsplithour = leftnumsplithour + 12
        elif lampm == "PM" and leftnumsplithour == 12:
            leftnumsplithour = 12
        elif lampm == "AM" and leftnumsplithour == 12:
            leftnumsplithour = 0
        else:
            leftnumsplithour = leftnumsplithour

        #This section covers no use of colon, so something like "9am" or 5pm" where there will be no minutes given
    else:
        leftnumsplithour = int(leftnumber)
        if lampm == "PM" and leftnumsplithour < 12:
            leftnumsplithour = leftnumsplithour + 12
            leftnumsplitminute = 0
        elif lampm == "PM" and leftnumsplithour == 12:
            leftnumsplithour = 12
            leftnumsplitminute = 0
        elif lampm == "AM" and leftnumsplithour == 12:
            leftnumsplithour = 0
            leftnumsplitminute = 0
        else:
            leftnumsplithour = leftnumsplithour
            leftnumsplitminute = 0
#####################################################################################################################################

    if ":" in rightnumber:                                               #This section covers if the user uses a colon
        rightnumsplithour, rightnumsplitminute = rightnumber.split(":")
        rightnumsplithour = int(rightnumsplithour)
        rightnumsplitminute = int(rightnumsplitminute)
        if rampm == "PM" and rightnumsplithour < 12:
            rightnumsplithour = rightnumsplithour + 12
        elif rampm == "PM" and rightnumsplithour == 12:
            rightnumsplithour = 12
        elif rampm == "AM" and rightnumsplithour == 12:
            rightnumsplithour = 0
        else:
            rightnumsplithour = rightnumsplithour

        #at this point leftnumsplithour and leftnumsplitminute are ready to be called with colons
    else:
        rightnumsplithour = int(rightnumber)
        if rampm == "PM" and rightnumsplithour < 12:
             rightnumsplithour = rightnumsplithour + 12
             rightnumsplitminute = 0
        elif rampm == "PM" and rightnumsplithour == 12:
             rightnumsplithour = 12
             rightnumsplitminute = 0
        elif rampm == "AM" and rightnumsplithour == 12:
            rightnumsplithour = 0
            rightnumsplitminute = 0
        else:
            rightnumsplithour = rightnumsplithour
            rightnumsplitminute = 0
#####################################################################################################################################

    if leftnumsplithour >23 or rightnumsplithour >23 or leftnumsplitminute >59 or rightnumsplitminute >59:
        raise ValueError
    else:
        pass

    return (f"{leftnumsplithour:02}:{leftnumsplitminute:02} to {rightnumsplithour:02}:{rightnumsplitminute:02}")



if __name__ == "__main__":
    main()
