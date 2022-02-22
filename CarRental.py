# A Program written to find the total the customer owes for a car rental.

# Written by: Chris Pinto
# Date Written: Jan 15th 2022


# Define program constants.
Tax = .15
Kilo = .10
DailyCost = 35.00

# Gather required data from the user.
CustNam = input("Enter Your Name: ")
PhoneNum = input("Enter You Phone Number: ")
NumOfDays = int(input("Enter the number of days: "))
OrgMile = int(input("Enter the original miles: "))
RetMile = int(input("Enter the Returned miles: "))
print()
RentCost = DailyCost * NumOfDays
SalesTax = RentCost * Tax
TotalKilo = RetMile - OrgMile
TotalKiloCost = TotalKilo * Kilo
TotalCost = RentCost + SalesTax + TotalKiloCost

# Perform required calculations.
print()
print("Rental Costs: ",   RentCost)
print("Sales Tax: ",      SalesTax)
print("Total Mile Cost: ", TotalKiloCost)
print("Total Cost: ",     TotalCost)