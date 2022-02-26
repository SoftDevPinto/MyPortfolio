import datetime

RightW = "Right Wing"
LeftW = "Left Wing"
DonaldT = "Donald Trump"
MikeP = "Mike Pence"
JoeB = "Joe Biden"
HilaryC = "Hilary Clinton"
Rep = "Rep"
Dem = "Dem"

DResult1 = 0
JResult1 = 0
MResult1 = 0
BResult1 = 0


def Vote():
    print(" Options    Canditates    Party   Wing")
    print("---------------------------------------")
    print("   1        Donald Trump   Rep    Right")
    print("   2        Joe Biden      Dem    Left")
    print("   3        Mike Pence     Rep    Right")
    print("   4        Bernie Sanders Dem    Left")

    while True:
        print()
        Choice = int(input("Enter the Number for your Presedental Vote, Please keep anonymous (1-4):  "))
        print()
        if Choice == 1:
            DResult2 = DResult1 + 1
            JResult2 = JResult1
            MResult2 = MResult1
            BResult2 = BResult1
        elif Choice == 2:
            JResult2 = JResult1 + 1
            DResult2 = DResult1
            MResult2 = MResult1
            BResult2 = BResult1
        elif Choice == 3:
            MResult2 = MResult1 + 1
            DResult2 = DResult1
            JResult2 = JResult1
            BResult2 = BResult1
        elif Choice == 4:
            BResult2 = BResult1 + 1
            DResult2 = DResult1
            JResult2 = JResult1
            MResult2 = MResult1
        else:
            break
        break

while True:
    try:
        CustFirstNam = input("Please enter your first name: ").title()
    except CustFirstNam == "":
        print("Name cannot be blank - Please enter your name. ")
        if not set(CustFirstNam).issubset(allowed_char):
            print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break

while True:
    try:
        CustLastNam = input("Please enter your last name: ").title()
    except CustLastNam == "":
        print("Name cannot be blank - Please enter your name. ")
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break

while True:
    try:
        IdNum = input("Please enter your ID Number: (1274847384)")
    except IdNum == "":
        print("ID cannot be blank - Please re-enter ")
    else:
        break

Runner1 = DonaldT
Runner2 = JoeB
Runner3 = MikeP
Runner4 = HilaryC
Choice1 = 1
Choice2 = 2
Choice3 = 3
Choice4 = 4


print(" Options    Canditates    Party   Wing")
print("----------------------------------------")
print("   1        Donald Trump   Rep    Right")
print("   2        Joe Biden      Dem    Left")
print("   3        Mike Pence     Rep    Right")
print("   4        Bernie Sanders Dem    Left")


while True:
    print()
    Choice = int(input("Enter the Number for your Presedental Vote, Please keep anonymous (1-4):  "))
    print()
    if Choice == 1:
        DResult1 = 1
        JResult1 = 0
        MResult1 = 0
        BResult1 = 0
    elif Choice == 2:
        JResult1 = 1
        DResult1 = 0
        MResult1 = 0
        BResult1 = 0
    elif Choice == 3:
        MResult1 = 1
        DResult1 = 0
        JResult1 = 0
        BResult1 = 0
    elif Choice == 4:
        BResult = 1
        DResult1 = 0
        JResult1 = 0
        MResult1 = 0
    else:
        break
    break

Choice = input("Is there another vote? (Y/N) ")
print()

if Choice == "Y":
    CustFirstNam = input("Enter your first name: ")
    CustLastNam = input("Enter your last name: ")
    IdNum = input("Enter your ID: ")
    Vote()
    Choice = input("Is there another vote? (Y/N) ")
elif Choice == "N":
    print("Thanks for using the voting system")
    print("")
    print("{:>4} {:<8} {:<12} {:<16}".format(DResult1, JResult1, MResult1, BResult1))
    AnyKey = input("Press any key to continue: ")
print()


if Choice == "Y":
    CustFirstNam = input("Enter your first name: ")
    CustLastNam = input("Enter your last name: ")
    IdNum = input("Enter your ID: ")
    Vote()
elif Choice == "N":
    print("Thanks for using the voting system")
    print("{:>4} {:<8} {:<12} {:<16}".format(DResult2, JResult2, MResult2, BResult2))






