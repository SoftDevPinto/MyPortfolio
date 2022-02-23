# Honest Harry's Used Cars - Sales Program QAP - 3

# Written By: Chris Pinto
# Date: Feb 15 2022
# Edited: Feb 23 2022 - Chris Pinto

from datetime import date
import datetime
# Constants.
LIC_FEE75 = 75.00
LIC_FEE165 = 165.00
HST = .15
TRANS_FEE_STD = 0.01
TRANS_FEE_LUX = 0.016
FIN_FEE1 = 39.99
FIN_FEE2 = 78.98
FIN_FEE3 = 119.97
FIN_FEE4 = 159.96

FIN_OPT1 = "1"
FIN_OPT2 = "2"
FIN_OPT3 = "3"
FIN_OPT4 = "4"
FIN_MON12 = 12
FIN_MON24 = 24
FIN_MON36 = 36
FIN_MON48 = 48

PAYMENT1 = 12
PAYMENT2 = 24
PAYMENT3 = 36
PAYMENT4 = 48

YEAR1 = 1
YEAR2 = 2
YEAR3 = 3
YEAR4 = 4

# Gather input from the user.
while True:
    while True:
        try:
            allowed_char = set("1234567890-")
            InvoiceDate = input("Please enter the date:  (YYYY-MM-DD): ")
            InvoiceDate = datetime.datetime.strptime(InvoiceDate, "%Y-%m-%d")
        except:
            print("Date format is not a valid format - Please re-enter. ")
        else:
            break

    while True:
        try:
           allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ_ abcdefghijklmnopqrstuvwxyz-' ")
           CustFirstNam = input("Please enter your first name: ").title()
        except CustFirstNam == "":
            print("Name cannot be blank - Please enter your name. ")
        if not set(CustFirstNam).issubset(allowed_char):
            print("Customers name cannot contain invalid characters - Please re-enter your name. ")
        else:
            break

    while True:
        try:
           allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
           CustLastNam = input("Please enter your last name: ").title()
        except CustLastNam == "":
            print("Name cannot be blank - Please enter your name. ")
        if not set(CustLastNam).issubset(allowed_char):
            print("Customers name cannot contain invalid characters - Please re-enter your name. ")
        else:
            break

    while True:
        HomePhoneNum = input("Please enter your home phone number (___-___-____): ")
        if HomePhoneNum.isdigit() == False:
             print("")
        if len(HomePhoneNum) != 10:
             print("Home Phone number must include area code and should be 10 digits - please try again: ")
        else:
            break

    while True:
        CellPhoneNum = input("Please enter your Cell phone number (___-___-____): ")
        if not CellPhoneNum.isdigit():
            print("")
        elif len(CellPhoneNum) != 10:
            print("Cell Phone number must include area code and should be 10 digits - please try again: ")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXWYZ abcdefghijklmnopqrstuvwxyz,0123456789-.'")
        StAdd = input("Enter your street address: ").title()
        if StAdd == "":
            print("Street address cannot be blank - Please try again. ")
        elif not set(StAdd).issubset(allowed_char):
            print("Street address contains invalid characters - Please try again. ")
        else:
            break

    while True:
        try:
            allowed_char = set(("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'"))
            City = input("Enter the City: ").title()
        except:
            print("City name contains invalid characters - Please re-enter ")
        if City == "":
            print("City name cannot be blank. Please re-enter.")
        elif not set(City).issubset(allowed_char):
            print("City name contains invalid characters - Please re-enter ")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
        Prov =  input("Please enter name of province: ")
        if not set(Prov).issubset(allowed_char):
            print("Province name contains invalid characters - Please try again. ")
        elif Prov == "":
            print("Province name cannot be blank - Please enter Province name. ")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890")
        PostalCode = input("Please enter your postal code  (A1A1A1): ").capitalize()
        if not set(PostalCode).issubset(allowed_char):
            print("Postal Code contains invalid characters - Please Re-enter.")
        elif PostalCode == "":
            print("Postal code cannot be blank - Please enter postal code. ")
        else:
            break

    while True:
       allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890")
       LicPlate = input("Enter the licence plate number (LLL000): ").capitalize()
       if not set(LicPlate).issubset(allowed_char):
          print("Licence plate number Contains invalid characters - Please re-enter: ")
       elif LicPlate == "":
          print("Licence plate number cannot be blank - Please re-enter.")
       elif len(LicPlate) != 6:
          print("Licence plate must be 6 characters - Please re-enter.")
       elif not LicPlate[0:3].isalpha():
          print("Licence plate number must start with 3 letters - Please re-enter.")
       elif not LicPlate[3:6].isdigit():
          print("Licence plate number must end with 3 numbers - Please re-enter.")
       else:
           break

    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.,-")
            VehicleMake = input("Enter the make of the vehicle.  Examples (Chevy, Dodge, Ford, etc.): ")
        except:
            print("Vehicle make contains invalid characters - Please re-enter vehicle year:")
        if set(VehicleMake).issubset(allowed_char) == False:
            print("Vehicle make contains invalid characters - Please re-enter vehicle year:")
        if VehicleMake == "":
            print("Vehicle make cannot be empty - Please enter the vehicle make.")
        else:
            break

    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,'.-")
            VehicleModel = input("Enter the vehicle model: ").title()
        except:
            print("Vehicle make contains invalid characters - Please re-enter: ")
        if VehicleModel == "":
            print("Vehicle model cannot be blank - Please re-enter:")
        elif set(VehicleMake).issubset(allowed_char) == False:
            print("Vehicle make contains invalid characters - Please re-enter:")
        else:
            break

    while True:
        allowed_char = set("1234567890")
        VehicleYear = input("Enter the year of the vehicle   (YYYY): ")
        if int(VehicleYear) == "":
            print("Vehicle year cannot be blank - Please enter the vehicle year: ")
        elif VehicleYear < "1990" or VehicleYear > "2023":
            print("Please enter a valid year: ")
        elif not set(VehicleYear).issubset(allowed_char):
            print("Vehicle year contains invalid characters - Please re-enter vehicle year:")
        else:
            break

    while True:
         allowed_char = set("1234567890.")
         SellPrice = float(input("Enter the sell price of the vehicle   ($99999.99): "))
         if SellPrice == "":
             print("Sell price cannot be blank - Please re-enter the sell price: ")
         elif SellPrice == "":
             print("Sell price contains invalid characters - Please re-enter: ")
         else:
             break

    while True:
         allowed_char = set("1234567890.")
         TradeIn = float(input("Enter the trade-in value of the vehicle   ($99999.99): "))
         if (TradeIn) == "":
             print("Trade-in value cannot be blank - Please re-enter the trade-in value: ")
         else:
             break

    while True:
        try:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,-.'")
            SalesPerson = input("Enter the salespersons name: ").title()
        except:
            print("Salespersons name cannot contain invalid characters - Please re-enter your name. ")
        if SalesPerson == "":
            print("Salespersons name cannot be blank - Please enter your name. ")
        elif set(SalesPerson).issubset(allowed_char) == False:
            print("Salespersons name cannot contain invalid characters - Please re-enter your name. ")
        else:
            break

    while True:
        allowed_char = set("1234567890")
        CreditNum = input("Please enter the credit card number  (9999-9999-9999-9999): ")
        if len(CreditNum) > 16 or len(CreditNum) < 16:
            print("Credit card number must be 16 digits long - Please re-enter:")
        elif not set(CreditNum).issubset(allowed_char):
            print("Credit card number contains invalid characters - Please re-enter:")
        else:
            break

    if float(SellPrice) >= 5000:
          LicenceFee = LIC_FEE165
    elif float(SellPrice) < 5000:
          LicenceFee = LIC_FEE75

    # Perform required calculations.
    TransferFee = float(0)

    PriceAftTrade = float(SellPrice) - float(TradeIn)
    TotSalePrice = PriceAftTrade + TransferFee + LicenceFee
    MonthlyPay = TotSalePrice + FIN_FEE1

    TotSalePrice1 = TotSalePrice + FIN_FEE1
    TotSalePrice2 = TotSalePrice + FIN_FEE2
    TotSalePrice3 = TotSalePrice + FIN_FEE3
    TotSalePrice4 = TotSalePrice + FIN_FEE4
    MonthlyPay1 = MonthlyPay / FIN_MON12
    MonthlyPay2 = MonthlyPay / FIN_MON24
    MonthlyPay3 = MonthlyPay / FIN_MON36
    MonthlyPay4 = MonthlyPay / FIN_MON48

    # Display output results for the user.
    print("# Years         # Payments          Financing Fee               Total Price          Monthly Payment")
    print("----------------------------------------------------------------------------------------------------")
    print("{:>4} {:>18}                ${:<24}  ${:.2f}                  ${:>5.2f}".format(YEAR1, PAYMENT1, FIN_FEE1, TotSalePrice1, MonthlyPay1))
    print("{:>4} {:>18}                ${:<24}  ${:.2f}                  ${:>5.2f}".format(YEAR2, PAYMENT2, FIN_FEE2, TotSalePrice2, MonthlyPay2))
    print("{:>4} {:>18}                ${:<24}  ${:.2f}                  ${:>5.2f}".format(YEAR3, PAYMENT3, FIN_FEE3, TotSalePrice3, MonthlyPay3))
    print("{:>4} {:>18}                ${:<24}  ${:.2f}                  ${:>5.2f}".format(YEAR4, PAYMENT4, FIN_FEE4, TotSalePrice4, MonthlyPay4))

    print()
    # Perform required calculations.
    while True:
        print()
        Choice = int(input("Enter the payment schedule you want to follow (1-4):  "))
        print()
        if Choice == Choice:
            Years = Choice
            New_Price = SellPrice - TradeIn
            Payments = 12 * Choice
            FinanceFee = Years * TransferFee
            New_Price += FinanceFee
            Mon_Pay = New_Price / Payments
            Fin_FeeDsp = "${:,.2f}".format(TransferFee * Choice)
            New_PriceDsp = "${:,.2f}".format(New_Price)
            Mon_PayDsp = "${:,.2f}".format(Mon_Pay)
        if SellPrice <= 5000.00:
            LicFee = LIC_FEE75
        elif SellPrice > 5000.00:
            LicFee = LIC_FEE165
        if SellPrice <= 20000.00:
            Trans_Fee = TRANS_FEE_STD * SellPrice
        elif SellPrice > 20000.00:
            Trans_Fee = TRANS_FEE_LUX * SellPrice
        else:
            break
        # Perform required calculations.
        Mon_PayDsp = New_Price / Payments
        PaymentsDsp = 12 * Choice
        Taxes = SellPrice * HST
        Trans_FeeDsp = "${:,.2f}".format(Trans_Fee)
        LicFeeDsp = "${:,.2f}".format(LicFee)
        PriceAfterTradeDsp = "${:,.2f}".format(SellPrice - TradeIn)
        Mon_PayDsp = "${:,.2f}".format(New_Price / Payments)
        SalesPriceDsp = "${:,.2f}".format(SellPrice)
        ReceiptDsp = f"{CustFirstNam.upper()[0]}{CustLastNam.upper()[0]}-{LicPlate.upper()[3:6]}-{HomePhoneNum[6:10]}"
        TaxesDsp = "${:.2f}".format(SellPrice * HST)
        Tot_Sales_Cost = SellPrice - TradeIn + LicFee + Taxes + Trans_Fee
        Tot_Sales_CostDsp = "${:,.2f}".format(Tot_Sales_Cost)
        Today = datetime

        # Display receipt results for the user.
        print()
        print("        Honest Harry Car Sales  ")
        print("       Used Car Sale and Receipt ")
        print()
        print("Invoice Date: ", InvoiceDate.strftime("%B %d, %Y "))
        print("Receipt No:", ReceiptDsp.upper())
        print()
        print("Sold to: ")
        print("    "f"{CustFirstNam.upper()[0]}.", CustLastNam.title())
        print("   ", StAdd.title())
        print("   ", City.title(),"," "", Prov.title(),"," "", PostalCode.upper())
        print()
        print("Car Details: ")
        print("          ", VehicleYear, VehicleMake.upper(), VehicleModel.upper())
        print("-----------------------------------------")
        print("Sale Price: ", "{:>28}".format(SalesPriceDsp))
        print("Trade Allowance: ", "{:>23}".format(PriceAfterTradeDsp))
        print("Price after Trade: ", "{:>21}".format(PriceAfterTradeDsp))
        print("                              -----------")
        print("HST:", "{:>36}".format(TaxesDsp))
        print("Licence Fee: {:>28}".format(LicFeeDsp))
        print("Transfer Fee: {:>27}".format(Trans_FeeDsp))
        print("                              -----------")
        print("Total Sales Cost: {:>23}".format(Tot_Sales_CostDsp))
        print("-----------------------------------------")
        print("Terms: {:>2}              Total Payments:{:>3}".format(Choice, PaymentsDsp))
        print("Monthly Payment: {:>24}".format(Mon_PayDsp))
        print("First Payment Date:   {:>1} ".format(str(InvoiceDate + datetime.timedelta(days=30))))
        print()
        print("         Honest Harry Car Sales  ")
        print("   Best Used cars at the best price! ")
        print()

        Cont = input("Do you wish to continue or end? (CON,END): ")
        if Cont == "CON":
            break
        elif Cont == "END" or "end":
            print()
            print("Thank you for shopping with Honest Harry's car sales")
            exit()
        else:
            print("Invalid Answer - Please Re-Enter")



