option = input("enter fish type")
if option == "carnivorous":
    option = input (" do you already have this fish") 
    if option == "yes":
        print("too bad")
    elif option == "no":
        print("enjoy")
elif option == "salt water":
    print("your a fancy fish parent")
elif option == "community":
    print("you should get more than one")
else:
    print("i dont think thats a fish")
