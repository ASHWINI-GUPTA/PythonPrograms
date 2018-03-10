#!/usr/bin/python3

# To Create New Account
def create_new_account():
    print ("Your Account Number :", account_number)
    if ((len(account_number)) == max_account_number_length):
            if (account_number not in account_holders):
                account_holders[account_number] = 0.0
                print ("Your Account is successfully opened!\nAccount Balance is: ",account_holders[account_number])
                return
                
            else:
                print ("\nAccount Number '{0}' Already Exist!!".format(account_number))
                return

    else:
        print("\nYou New Account Number is not valid!!\nPlease try again!")
        return

# Deposit into Account
def deposit():
    print ("\n** Deposit **\n")
    print ("\nYou Account Number is: ", account_number)
    try:
        deposit_amount = float(input("\nEnter the Amount to deposit: "))
        account_holders[account_number] += deposit_amount
        print ("\nYour New Account Balance: ", account_holders[account_number])
        return
    except:
        print ("Your Transaction is Failed!!\nTry again after some time.")
        print ("\nYour New Account Balance: ", account_holders[account_number])
        return     

# Withdraw from Account
def withdraw():
    print ("\n\n** Withdraw **\n")
    print ("You Account Number is: ", account_number)
    
    try:
        withdraw_amount = float(input("\nEnter the Amount to withdraw: "))

        if (withdraw_amount > account_holders[account_number]):
            print("\nSorry, You are out of limit!!")
            return
        else:
            account_holders[account_number] -= withdraw_amount
            print ("\nYour New Account Balance: ", account_holders[account_number])
            return

    except ValueError:
        print ("Your Transaction is Failed!!\nTry again after some time.")
        print ("\nYour New Account Balance: ", account_holders[account_number])
        return

# ****** Main Function ******

account_holders = {'0001' : 10.0, '0002' : 20.0, '0003' : 30.0} # Account Number : Account Balance

max_account_number_length = 4 # Change to increase the length of account number

while True: # condition is always true

    #print ("\n** For testing purpose **\n")
    #print ("\nExisting Account Numbers : ", account_holders.keys())
    #print ("\nAccount Balance : ", account_holders.values())

    choose = int(input("\nEnter the Choice:\n1. Deposit \n2. Withdraw \n3. To Create New Account \n4. Exit \n")) # Make Choice

    if (choose == 1):

        account_number = (input("\nEnter {0} digit Account Number: ".format(max_account_number_length)))

        if ((len(account_number)) == max_account_number_length):
            if (account_number in account_holders):
                print ("\nYour Current Account Balance: ", account_holders[account_number])
                deposit() #call function deposit
            else:
                print("\nYou Account Number is not valid!!\nPlease check and retry!")
                new_option = int(input("\n** Sub Menu **\nEnter the Choice:\n1. Open New Account \n2. Exit to Main Menu and Retry\n"))
                if (new_option == 1):
                    create_new_account()
                else:
                    break
        else:
            print("\nYou Account Number is not valid!!\nPlease check and retry!")
            continue

    elif (choose == 2):

        account_number = (input("Enter {0} digit Account Number: ".format(max_account_number_length)))

        if ((len(account_number)) == max_account_number_length):

            if (account_number in account_holders):
                print ("\nYour Current Account Balance: ", account_holders[account_number])
                withdraw() #call function withdraw

            else:
                print("\nYou Account Number is not valid!!\nPlease check and retry!")
                break

        else:
            print("\nYou Account Number is not valid!!\nPlease check and retry!")
            continue

    elif (choose == 3):

        account_number = (input("\nEnter {0} digit New Account Number: ".format(max_account_number_length)))

        if ((len(account_number)) == max_account_number_length):
            create_new_account()
                
        else:
            print("\nYou New Account Number is not valid!!\nPlease try again!")
            continue

    else:
        print("Thank you for Banking with us!\nHave a Nice Day!!")
        input()
        break