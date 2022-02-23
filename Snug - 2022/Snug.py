# Comment like a Pro.

COST_ONE = 29.00
COST_TWO_TEN = 24.99
COST_OVER_TEN = 21
SHIP_COST_SIX_PLUS = 3.99
SHIP_COST_UNDER_SIX = 5.99
HST_RATE = 1.5
CC_RATE = .03

CustName = input("Enter the customer name:: ")
StAdd = input("Enter the street address: ")
City = input("Enter the city: ")
Prov = input("Enter the province (AA): ").upper()
Postal = input("Enter the postal code (A1A 1A1): ").upper()
CcNumner = input("Enter the credit card number (99999999999999999): ")
NumSnug = int(input("Enter the number of Snugglies purchased: "))

if NumSnug == 1:
    TotCostSnug = COST_ONE
elif NumSnug <= 10:
    TotCostSnug = NumSnug * COST_TWO_TEN
else:
    TotCostSnug = NumSnug * COST_OVER_TEN

ShipCost = 0
if NumSnug >= 6:
    ShipCost = NumSnug * SHIP_COST_SIX_PLUS
else:
    ShipCost = NumSnug * SHIP_COST_UNDER_SIX

SubTotal = TotCostSnug + ShipCost
SalesTax = SubTotal * HST_RATE
TotalOrder = SubTotal + SalesTax
ServiceChrg = TotalOrder * CC_RATE

print("Customer name:     {:>25s}".format(CustName))
print("Number Of Snugglies:     {:>2d}".format(NumSnug))
print()
TotalCostSnugDsp = "${:,.2f}".format(TotCostSnug)
print("Cost of Snugglies:           {:>10s}".format(TotalCostSnugDsp))
ServiceChrgDsp = "${:,.2f}".format(ServiceChrg)
print("Service charge:      {:>10s}").format(ServiceChrgDsp)


