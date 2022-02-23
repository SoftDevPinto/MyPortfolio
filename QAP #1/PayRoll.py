# A Program written for a PayRoll System
# Written By: Chris Pinto
# Date: Jan 16th 2022

# Define program constants.
PayPerHr = 17.50
Widget = .35


# Gather required data from the user.
EmplNam = input("Enter The Employees Name: ")
HrWork = float(input("Enter The Hours Worked: "))
Monday = float(input("Enter The Number of Widgets produced Monday: "))
Tuesday = float(input("Enter The Number of Widgets produced Tuesday: "))
Wednesday = float(input("Enter The Number of Widgets produced Wednesday: "))
Thursday = float(input("Enter The Number of Widgets produced Thursday: "))
Friday = float(input("Enter The Number of Widgets produced Friday: "))


# Perform required calculations.
print()
RegPay = HrWork * PayPerHr
TotalWid = Monday + Tuesday + Wednesday + Thursday + Friday
Comm = Widget * TotalWid
GrossPay = RegPay + Comm
IncomTax = GrossPay * .21
CPP = GrossPay * .0495
Ei = GrossPay * .016
UnionDue = 15
TotalDet = IncomTax + CPP + Ei + UnionDue
NetPay = GrossPay - TotalDet


# Display output results for the user.
print()
print("Employee Name: ", EmplNam)
print("Hours Worked: ", HrWork)
print("Commission Earned: {:.2f}".format(Comm))
print("Gross Pay: {:.2f}".format(GrossPay))
print("Income Tax: {:.2f}".format(IncomTax))
print("CPP: {:.2f}".format(CPP))
print("UnionDues: {:.2f}".format(UnionDue))
print("Net Pay: {:.2f}".format(NetPay))