# A program written for St. John's Marina & Yacht Club

# Written By: Chris Pinto
# Date Written: Jan 31 2022

# Define program constants.
ALT_MEM_COST = 5.00
EVEN_MONTHLY = 80.00
ODD_MONTHLY = 120.00
SITE_CLEAN = 0
VID_SURV = 0
TAX = .15
STANDARD = 75.00
EXECUTIVE = 150.00

# Gather required data from the user.
SiteNum = int(input("Enter the Site number (1-100): "))
MemNam = input("Enter the Members Name: ")
StAdd = input("Enter the street address: ")
City = input("Enter the city: ")
Prov = input("Enter the province: ")
PostCode = input("Enter the Postal Code: ")
PhoneNum = int(input("Enter the phone number: "))
CellNum = int(input("Enter the cell number: "))
MemShipType = input("Enter the Membership type(S,E): ")
AltMem = int(input("Enter the number of alternate members: "))
WeeklySiteClean = input("Weekly site cleaning?(Y/N): ").upper()
VideoSur = input("Video Surveillance?(Y/N): ").upper()

# Perform required calculations.
TotAlt = AltMem * ALT_MEM_COST
EvenSiteChrg = EVEN_MONTHLY * TotAlt
OddSiteChrg = ODD_MONTHLY * TotAlt
if MemShipType == "S" or "s":
    TypeMem = "Standard"
elif MemShipType == "E" or "e":
    TypeMem = "Executive"
if WeeklySiteClean == "Y":
    WeeklyClean = "Yes"
else:
    WeeklyClean = "No"
if VideoSur == "Y":
    VidSur = "Yes"
else:
    VidSur = "No"
if SiteNum % 2 == 0:
    SiteChrg = EVEN_MONTHLY + TotAlt
elif SiteNum % 2 == 1:
    SiteChrg = ODD_MONTHLY + TotAlt
if WeeklySiteClean == "Y":
    SITE_CLEAN = 50.00
else:
    SITE_CLEAN = 0
if VideoSur == "Y":
    VID_SURV = 35.00
else:
    VID_SURV = 0
ExtraChrg = VID_SURV + SITE_CLEAN
if SiteNum % 2 == 0:
    Subtotal = SiteChrg + ExtraChrg
elif SiteNum % 2 == 1:
    Subtotal = SiteChrg + ExtraChrg
if (SiteNum % 2 == 0):
    TotalTax = (SiteChrg + ExtraChrg) * TAX
elif (SiteNum % 2 == 1):
    TotalTax = (SiteChrg + ExtraChrg) * TAX
if SiteNum % 2 == 0:
    TotMonChrg = SiteChrg + ExtraChrg + TotalTax
elif SiteNum % 2 == 1:
    TotMonChrg = SiteChrg + ExtraChrg + TotalTax
if MemShipType == "S" or "s":
    TotMonFee = STANDARD + TotMonChrg
elif MemShipType == "E" or "e":
    TotMonFee = EXECUTIVE + TotMonChrg
if MemShipType == "S" or "s":
    MonthlyDues = 75
elif MemShipType == "E" or "e":
    MonthlyDues = 150.00
YearlyFees = TotMonFee * 12
MonthlyPay = (YearlyFees + 59.99) / 12
CancelFee = YearlyFees * .60

# Display output results for the user.
print()
print()
print(" "*15,      "St. John's Marina & Yacht Club")
print(" "*18,        "Yearly Member Reciept")
print("-------------------------------------------------------")
print()
print("Client Name and Address:")
print()
print(MemNam)
print(StAdd)
print(City,",",Prov)
print(PostCode)
print()
print("Phone: {:<2}(H)".format(PhoneNum))
print("     : {:<2}(C)".format(CellNum))
print()
print("Site #: {:<21} Member Type: {:<21}".format(SiteNum, TypeMem))
print()
print("Alternate Members:                                 {:<21}".format(AltMem))
print("Weekly Site Cleaning:                              {:<21}".format(WeeklyClean))
print("Video Surveillance:                                {:<21}".format(VidSur))
print()
print("Site Charges:                                    ${:.2f}".format(SiteChrg))
print("Extra Charges:                                    ${:.2f}".format(ExtraChrg))
print("                                              ----------")
print("Subtotal:                                        ${:.2f}".format(Subtotal))
print("Sales Tax(HST):                                   ${:.2f}".format(TotalTax))
print("                                              ----------")
print("Total Monthly Charges:                           ${:.2f}".format(TotMonChrg))
print("Monthly dues:                                    ${:.2f}".format(MonthlyDues))
print("                                              ----------")
print("Total Monthly Fees:                              ${:.2f}".format(TotMonFee))
print("Total yearly fee:                               ${:.2f}".format(YearlyFees))
print("Monthly Payment:                                 ${:.2f}".format(MonthlyPay))
print("--------------------------------------------------------")
print("Issued: 2022-01-31")
print("HST Reg No: 549-33-5849-4720-9885")
print()
print("Cancellation Fee:                                ${:.2f}".format(CancelFee))