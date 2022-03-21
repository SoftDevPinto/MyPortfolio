# Comment here

print("ABC Company")
print("Sales Listing")
print()
print("Inv     Customer            Item      HST     Total")
print("Num     Name                Cost              Cost")
print("="*53)

CustCtr = 0
TotalCostAcc = 0

f = open("Sales.dat", "r")

for SalesDataLine in f:
    SalesLine = SalesDataLine.split(",")

    EmpNum = SalesLine[0].strip()
    EmpName = SalesLine[1].strip()
    ItemCost = float(SalesLine[2].strip())
    HST = float(SalesLine[3].strip())
    TotalCost = float(SalesLine[4].strip())

    print("  {}  {:<20}  ${:,.2f}  ${:,.2f}   ${:,.2f}".format(EmpNum, EmpName, ItemCost, HST, TotalCost))

    CustCtr += 1
    TotalCostAcc += TotalCost
f.close()
print("="*53)
print("Customers Listed: {}                         ${:,.2f}".format(CustCtr, TotalCostAcc))
