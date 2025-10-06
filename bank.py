name = ["Connor , Jack , john , josh"]
balance = [39 , 47 , 90 , 100]
check = False
while check == False:
    for i in range(len(name)):
        print(f"Name:{name[1]} balance:{balance[1]}")
    print ("welcome to FFCU How can I help you ")
    print ("deposit or withdraw ")
    print ("Transpher Money")
    print ("listy acounts and balance")
    print ("add or remove acount")
option = input("")
if(option == "deposit"):
    print("how much do you want to deposit")
if(option == "withdraw"):
    print("how much do you want to withdraw")
