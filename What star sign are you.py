#imports time so i can use the sleep delay command
import time

#Welocmes the user to the game and asks if they want to find out there star sign
def welcome():
    print ("Lets find out what your star sign is. Tap y to continue or press any key to exit:")
    answer = input(">")
    if answer == "y":
        print ("Let't get started")
        print ("LOADING...")
        time.sleep(3)
        questions()
    else:
        exit()

#Asks the user what month they are born
def questions():
    print ("What month were you born?")
    month = input(">")
    if month == "january":
        one()
    if month == "february":
        two()
    if month == "march":
        three()
    if month == "april":
        four()
    if month == "may":
        five()
    if month == "june":
        six()
    if month == "july":
        seven()
    if month == "august":
        eight()
    if month == "september":
        nine()
    if month == "october":
        ten()
    if month == "november":
        eleven()
    if month == "december":
        twelve()
    else:
        questions()


#Asks the user which of the 2 date options they are born between
def one():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 19th")
    print ("B: 20th - 31st")
    date = input(">")
    if date == "A":
        print ("Your star sign is Capricorn")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Aquarius")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        one()

def two():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 18th")
    print ("B: 19th - 28th")
    date = input(">")
    if date == "A":
        print ("Your star sign is Aquarius")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Pisces")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        two()
        
def three():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 20th")
    print ("B: 21st - 31st")
    date = input(">")
    if date == "A":
        print ("Your star sign is Pisces")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Aries")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        three()

def four():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 19th")
    print ("B: 20th - 30th")
    date = input(">")
    if date == "A":
        print ("Your star sign is Aries")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Taurus")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        four()

def five():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 20th")
    print ("B: 21st - 31tst")
    date = input(">")
    if date == "A":
        print ("Your star sign is Taurus")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Gemini")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        five()

def six():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 20th")
    print ("B: 21st - 30th")
    date = input(">")
    if date == "A":
        print ("Your star sign is Gemini")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Cancer")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        six()

def seven():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 22nd")
    print ("B: 23rd - 31st")
    date = input(">")
    if date == "A":
        print ("Your star sign is Cancer")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Leo")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        seven()

def eight():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 22nd")
    print ("B: 23rd - 31st")
    date = input(">")
    if date == "A":
        print ("Your star sign is Leo")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Virgo")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        eight()

def nine():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 22nd")
    print ("B: 23rd - 30th")
    date = input(">")
    if date == "A":
        print ("Your star sign is Virgo")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Libra")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        nine()

def ten():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 22nd")
    print ("B: 23rd - 31st")
    date = input(">")
    if date == "A":
        print ("Your star sign is Libra")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Scorpio")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        ten()

def eleven():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 21st")
    print ("B: 22nd - 30th")
    date = input(">")
    if date == "A":
        print ("Your star sign is Scorpio")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Sagittarius")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        eleven()

def twelve():
    print ("Does option A or option B contain your birth date?")
    print ("A: 1st - 21st")
    print ("B: 22nd - 31st")
    date = input(">")
    if date == "A":
        print ("Your star sign is Sagittarius")
        time.sleep(2)
        exit()
    if date == "B":
        print ("Your star sign is Capricorn")
        time.sleep(2)
        exit()
    else:
        print ("Invalid input")
        twelve()

welcome()



#Notes to keep track of what star signs link to what months/dates
# Capricorn == December 22 - January 19
# Aquarius == jan 20 - feb 18
# Pisces == feb 19 - march 20
# Aries == march 21 - april 19
# Taurus == april 20 - may 20
# Gemini == may 21 - june 20
# Cancer == june 21 - july 22
# Leo == july 23 - aug 22
# Virgo == aug 23 - sept 22
# Libra == sept 23 - oct 22
# Scorpio == oct 23 - nov 21
# Sagittarius == nov 22 - dec 21

#Notes to show what the last date is of each month
# Jan = 31
# Feb = 28
# Mar = 31
# Apr = 30
# May = 31
# June = 30
# July = 31
# Aug = 31
# Sept = 30
# Oct = 31
# Nov = 30
# Dec = 31

