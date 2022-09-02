#First name validation
def first_name_validation():
    while True:
        allowedchar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,-")
        try:
            fname = input("Please enter your first name: ")
        except:
            print("Invalid customer name - please re-enter.")
        else:
            if fname == "":
                print("Invalid first name - cannot be blank - please re enter")
            elif set(fname).issubset(allowedchar) == False:
                print("Invalid first name - characters entered not valid - please re-enter")
            #else:
                #fname = fname
            break
    print(fname)
#validation for the last name
def last_name_validation():
    while True:
        allowedchar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,-")
        try:
            lname = input("Please enter your last name: ")
        except:
            print("Invalid customer name - please re-enter.")
        else:
            if lname == "":
                print("Invalid last name - cannot be blank - please re enter")
            elif set(lname).issubset(allowedchar) == False:
                print("Invalid last name - characters entered not valid - please re-enter")
            else:
                lname = lname.title()
                break
    #validation for phone number
def phone_number_validation():
    while True:
        try:
            PhoneNum = input("Enter the phone number (9999999999): ")
        except:
            print("Invalid phone number - please re-enter: ")
        else:
            if PhoneNum == "" or len(PhoneNum) != 10 or PhoneNum.isdigit() == False:
                print("Invalid phone number - please re-enter.")
            else:
                PhoneNum = "(" + PhoneNum[0:3] + ")" + PhoneNum[3:6] + "-" + PhoneNum[6:]
                break
    # Set up a validation for the plate number
def license_plate_number_validation():
    while True:
        Lplate = input("Please enter a lisence plate number (XXX999): ")
        if Lplate == "":
            print("Please enter a lisence plate number - cannot be blank - please re-enter")
        elif len(Lplate) != 6:
            print("Please enter a 6 character lisence plate - please re-enter")
        elif not (Lplate[0:2].isalpha() and Lplate[3:5].isdigit()):
            print("Missformatted lisence plate number")
        else:
            break
        #validation for the Credit Card number
def credit_card_number_validation():
    while True:
        try:
            CreditCardNum = input("Enter your credit card number (999999999999): ")
        except:
            print("Invalid credit card number - please re-enter: ")
        else:
            if CreditCardNum == "" or len(CreditCardNum) != 12 or CreditCardNum.isdigit() == False:
                print("Invalid credit card number - please re-enter.")
            else:
                CreditCardNum = CreditCardNum[0:4] + " " + CreditCardNum[4:8] + " " + CreditCardNum[8:]
                break