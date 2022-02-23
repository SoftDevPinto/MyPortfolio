# Main Menu - Chris Pinto
import datetime
import random
def CelcFahr():
    Celc = int(input("Enter a Temperature in Celsius: "))
    Fahr = 9 / 5 * Celc + 32
    print()
    print("{} degrees Celsius is {} degrees Fahrenheit. ".format(Celc, Fahr))
    print()
    AnyKey = input("Press any key to continue. ")
def CalcThr():
    Age = int(input("Enter your age: "))
    Resting_HR = int(input("Enter your resting heart rate: "))
    # validate needed, could use range, ensure its valid digit
    Thr = float((((220 - Age)) - float(Resting_HR)) * float(0.60)) + float(Resting_HR)
    THRDsp = "{:.0f}".format(Thr)
    print("Your training heart rate is {} BPM".format(Thr))
    Anykey = input("Press any key to continue.")
def DaysToSanta():
    # CurDate = datetime.datetime.today()
    CurDate = datetime.datetime(2022, 2, 15)
    ChrDate = datetime.datetime(CurDate.year, 12, 25)
    if CurDate.month == 12 and CurDate.day > 25:
        ChrDate = datetime.datetime(CurDate.year + 1, 12, 25)
    DaysToChr = (ChrDate - CurDate).days
    print()
    print("The current date is " + CurDate.strftime("%Y/%m/%d"))
    print("The next Christmas day is on " + ChrDate.strftime("%Y/%m/%d"))
    print(str(DaysToChr) + " days to Christmas")
    print()
    Anykey = input("Press any key to continue.")
def OldInv():
    Company = input("Enter the name of the company: ")
    InvDate = input("Enter the date of the invoice (YYYY/MM/DD): ")
    InvAmt = float(input("Enter the amount of the invoice: "))
    CurDate = datetime.datetime.now()
    InvDate = datetime.datetime.strptime(InvDate, "%Y/%m/%d")
    Age = (CurDate - InvDate).days
    print()
    print("The current date is " + CurDate.strftime("%Y/%m/%d"))
    print("The Invoice Date is " + InvDate.strftime("%Y/%m/%d"))
    print("The invoice is " + str(Age) + " days old.")
    print()
    if Age <= 30:
        print("Advice: OK for now")
    elif Age >= 31 and Age <= 60:
        print("Advice: Better think about paying.")
    elif Age > 60:
        print("Advice: This one could be in trouble.")
    Anykey = input("Press any key to continue.")
def GuessGame():
    Number = random.randint(1, 101)
    GuessCtr = 0
    while True:
        Guess = int(input("Enter your guess: "))
        GuessCtr += 1
        if Guess == Number:
            print()
            print("You are correct.  The number was " + str(Number) + ".")
            break
        elif Guess < Number:
            print()
            print("The number is higher than your current guess.")
        else:
            print()
            print("The number is lower than your current guess.")
    print("You had " + str(GuessCtr) + " guesses.")
    print()
    print("Thanks for playing our little game.")
    Anykey = input("Press any key to continue.")
while True:
    print()
    print("Chris' Quick Problems - Main Menu")
    print()
    print("1. Convert Celsius to Fahrenheit")
    print("2. Determine Training Heart Rate.")
    print("3. How many days to Christmas?")
    print("4. How old is an invoice?")
    print("5. Play my guessing game.")
    print("6. Quit")
    print()
    Choice = int(input("   Enter choice (1-6): "))
    if Choice == 1:
        CelcFahr()
    elif Choice == 2:
         CalcThr()
    elif Choice == 3:
        DaysToSanta()
    elif Choice == 4:
        OldInv()
    elif Choice == 5:
        GuessGame()
    elif Choice == 6:
        print("Thanks for using the menu")
        break