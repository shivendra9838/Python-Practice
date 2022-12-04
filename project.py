import datetime
import time as t
import random
acc_list=[74185296300,96385274100,78945612300,32165498700]
pin_list=[887253,987214,628389,740011]
bal_list=[7000,4000,3000,1000]
account_holder=["Ishaan Khullar","Abhinas","Shivendra","Pranav"]
pass_book=[]

#def1
def check_balance(a):
    print("Your Current Account Balance is :  ",bal_list[a])

#def2
def change_pin(a):
    check_old_pin=int(input("Enter Old PIN         :  "))
    if check_old_pin==pin_list[a]:
        a1=random.randint(1,100)
        b1=random.randint(1,100)
        print("--- Enter a Number Between\033[91m",a1,"\033[0m and \033[91m",b1,"\033[0m---")
        print("\t\tOR","--- Press \033[91m 0 \033[0m to Cancel Change PIN ---",sep="\n")
        Authentication=int(input("Please Enter a Number Between the Given Range: "))
        if(a1<b1):
            if(Authentication>a1 and Authentication<b1):
                t.sleep(0.5)
                print("\tPlease Wait....")
                user_pin=int(input("Enter 6-Digit NEW PIN :  "))
                if user_pin!=pin_list[a] and len(str(user_pin))==6:
                    pin_list[a]=user_pin
                    print("Initiating Your Request","Please Wait........")
                    t.sleep(1)
                    print("Your New PIN for Your Account is :  ",user_pin)
                    t.sleep(1)
                else:
                    print("Please Wait......")
                    t.sleep(1)
                    print("You Have Entered Wrong PIN Format")
                    t.sleep(1)
            else:
                t.sleep(1)
                print("\tYou Are Not Authorized !!")
                t.sleep(0.5)
                print("---   Exiting From Current Window   ----")
                t.sleep(0.5)
        elif(a1>b1):
            if(Authentication<a1 and Authentication>b1):
                t.sleep(0.5)
                print("\tPlease Wait....")
                user_pin=int(input("Enter 6-Digit NEW PIN :  "))
                if user_pin!=pin_list[a] and len(str(user_pin))==6:
                    pin_list[a]=user_pin
                    print("Your New PIN for Your Account is :  ",user_pin)
                else:
                    print("Please Wait......")
                    t.sleep(1)
                    print("---You Have Entered Wrong PIN Format---")
                    t.sleep(1)
            else:
                t.sleep(1)
                print("\tYou Are Not Authorized!!!")
                t.sleep(0.5)
                print("---- Exiting From Current Window ----")
                t.sleep(0.5)
    else:
        print("Please Wait......")
        t.sleep(1)
        print("The Old PIN Entered is INCORRECT !!")
        t.sleep(1)
        print("You are Unauthorized !!")
        t.sleep(0.5)
        print("Try Again With a Valid PIN")
        t.sleep(0.5)

#def 3
def transfer(a):
    print("Select one of these option to transfer!!!")
    print("\t\t\033[92m 1. \033[0mTo UPI")
    print("\t\t\033[92m 2. \033[0mTo Bank Account")
    print("\t\t\033[92m 3. \033[0mTo Mobile Number")
    a1 = int(input("\n\t\tEnter Method: "))
    if a1==1 or a1==2 or a1==3:
        if a1==1:
            UPI=input("Enter UPI id:")
            if "@" in UPI:
                UPI_id=["oksbi","okhdfc","ybl","paytm","fampay","okaxis","okicici"]
                Index=UPI.index("@")
                if UPI[Index+1:] in UPI_id and UPI[:Index].isalnum:
                    Amount=int(input("Enter amount to be transferred:"))
                    if Amount<=int(bal_list[a]) :
                        bal_list[a]=bal_list[a]-Amount
                        t.sleep(1.5)
                        print("Amount Rs.",Amount,"sent to UPI id:",UPI)
                        History="Amount Rs",Amount,"sent to","UPI id:",UPI,"Closing balance:",bal_list[a]
                        pass_book.append(History)
                        print("Current Balance is",bal_list[a])
                    elif Amount>bal_list[a]:
                        print("---Insufficient Balance!!!---")
                else:
                    print("--- Wrong UPI id!!! ---")
            else:
                print("--- Wrong UPI id!!! ---")
        if a1==2:
            Bank_Account=int(input("Enter Account Number:"))
            if len(str(Bank_Account))==11:
                Amount=int(input("Enter amount to be transferred:"))
                if Amount<=int(bal_list[a]):
                    bal_list[a]=bal_list[a]-Amount
                    t.sleep(1.5)
                    print("Amount Rs.",Amount,"sent to Account Number:",Bank_Account)
                    print("Current Balance is",bal_list[a])
                    History="Amount Rs",Amount,"sent to","Account Number:",Bank_Account,"Closing balance:",bal_list[a]
                    pass_book.append(History)
                elif Amount>bal_list[a]:
                    print("---Insufficient Balance!!!---")
            else:
                print("---Wrong Account Number!!!---")
        if a1==3:
            Mobile_Number=int(input("Enter Mobile Number:"))
            rejected_list=[0,1,2,3,4,5]
            if len(str(Mobile_Number))==10 and int(str(Mobile_Number)[0]) not in rejected_list:
                Amount=int(input("Enter amount to be transferred:"))
                if Amount<=int(bal_list[a]):
                    bal_list[a]=bal_list[a]-Amount
                    t.sleep(1.5)
                    print("Amount Rs.",Amount,"sent to Mobile Number:",Mobile_Number)
                    print("Current Balance is",bal_list[a])
                    History="Amount Rs",Amount,"sent to"," number:",Mobile_Number,"Closing balance:",bal_list[a]
                    pass_book.append(History)
                elif Amount>bal_list[a]:
                    print("---Insufficient Balance!!!---")
            else:
                print("---Wrong Mobile Number!!!---")


    else:
        print("---You have selected wrong option!!!---")

#def 4
def passbook(a):
    print(pass_book)

num_of_tries = 3
while (num_of_tries!=0):
    check_acc_num=int(input("Please 11-Digit Account Number:  "))
    check_pin=int(input("Please Enter Your 6 Digit UPI PIN:  "))
    if(check_acc_num in acc_list and check_pin in pin_list):
        #ACCOUNT 1
        a = acc_list.index(check_acc_num)
        print("ACCOUNT AUTHORISED!!\n")
        print("Hello" ,account_holder[a] ,"!!!","Welcome to SBI Bank of India")
        while True:
            print("\t\t  \033[91m 1.\033[0m BALANCE ENQUIRY")
            print("\t\t  \033[91m 2.\033[0m CHANGE PIN")
            print("\t\t  \033[91m 3.\033[0m TRANSFER")
            print("\t\t  \033[91m 4.\033[0m PASSBOOK")
            Facility=int(input("Select Any Facility to Avail:  "))
            if(Facility==1):
                print("--- You Have Selected BALANCE ENQUIRY ---")
                check_balance(a)
            elif(Facility==2):
                print("--- You Have Selected PIN CHANGE ENQUIRY ---")
                change_pin(a)
            elif(Facility==3):
                print("--- You Have Selected TRANSFER ENQUIRY ---")
                transfer(a)
            elif(Facility==4):
                print("--- You Have Selected PASSBOOK ENQUIRY ---")
                passbook(a)
            else:
                print("---You Have Selected Wrong Option!!!---")
                

    else:
        num_of_tries-=1 
        print("PIN incorrect! Number of tries left -", num_of_tries,end="\n\n")
        if(num_of_tries==0):
            print("ACESS DENIED !!!",sep="\n")   
            print(".....Exiting from SYSTEM.....")
            t.sleep(2)
            print("....YOU ARE UNAUTHORISED....")