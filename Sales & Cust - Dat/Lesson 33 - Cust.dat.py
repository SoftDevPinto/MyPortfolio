print("               RICKS COMPANY")
print("     ACCOUNTS RECEIVABLE CUSTOMER LISTING")
print("===============================================")
print("   Account        Customers             Phone")
print("   Number         Name                  Number")
print("="*47)

CustCtr = 0


f = open("Customer.dat", "r")

for CustomersDataLine in f:
    CustLine = CustomersDataLine.split(",")

    EmpNum = CustLine[0].strip()
    EmpName = CustLine[1].strip()
    PhoneNum = CustLine[4].strip()

    print("  {}        {:<23} {:<25}".format(EmpNum, EmpName, PhoneNum,))

    CustCtr += 1

f.close()
print("="*47)
print("Customers Listed: {}".format(CustCtr))
