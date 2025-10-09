accounts = ["connor","john", "Mike", "jack"] #list of all the accounts
balances = [200, 500, 1000, 700] #list of the balances for the accounts
check = False 
while check == False:#this makes program continue running until "check = True"
    x = input("would you like to open the menu? ") #program will continue to ask "would you like to open the menu" until it is told something other than "yes"
    if x == ("yes"):
        print("1.deposit")
        print("2.withdraw")
        print("3.view accounts and balances")
        print("4.transfer money")
        print("5.add account")
        print("6.remove account")
        #these print out the functions of the system for the user to view
        x = input("what # action would you like to do? ") 
        if x == ("3"):
            #takes in existing account name, links the account to its balance, and prints the value of the balance to the user
            accountname4 = input("what is your account name? ")
            index = accounts.index(accountname4)
            print(balances[index]) 
        elif x == ("5"):
            #takes in name of new account, creates the account
            accountname = input("what is your account name? ") 
            accounts.append(accountname) 
            balances.append(0) 
            index = accounts.index(accountname) 
            print("your account has been added")
        elif x == ("6"):
            #takes in the account name, links it to balance
            accountname2 = input("what is your account name? ") 
            index = accounts.index(accountname2) 
            accounts.pop(index) 
            balances.pop(index) 
            print("your account and balance has been removed. ")
        elif x == ("1"):
            #takes in the account name links it to balance
            accountname3 = input("what is your account name? ") 
            index = accounts.index(accountname3) 
            x = input("how much would you like to add? ") 
            x = int(x) 
            balances[index] = balances[index] + x 
            print(f"your new balance is {balances[index]} ")
        elif x ==("2"):
             #takes in the account name,and subtracts the value being withdrawn from the balance
            accountname5 = input("what is your account name? ") 
            index = accounts.index(accountname5) 
            x = input("how much would you like to withdraw? ") 
            x = int(x) 
            balances[index] = balances[index] - x #
            print(f"your new balance is {balances[index]} ") 
        elif x == ("4"):
            #subtracts value of money from the transferring account's balance and adds it to the recieving accounts balance
            accountname6 = input("what is your account name? ") 
            index = accounts.index(accountname6)
            accountname7 = input("what is the transfer account name? ") 
            i = accounts.index(accountname7) 
            transfer = input("how much would you like to transfer? ") 
            transfer = int(transfer) 
            balances[i] = balances[i] + transfer 
            balances[index] = balances[index] - transfer 
            print(f"{accountname7}'s balance is {balances[i]} ") 
            print(f"your account balance is {balances[index]} ")    
    else:
        check = True #stops program from looping
        print("thanks for using the bank system ")

            
            