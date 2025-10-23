sizes = []
large = []
medium = []
small = []
check = False 
while check == False:
    mushroom = input("what is the size of your mushroom?(type stop to end program) ").strip()
    if mushroom == "stop":
        check = True
        print(f"your large mushrooms are {large}")
        print(f"your medium mushrooms are {medium}")
        print(f"your small mushrooms are {small}")
    if mushroom.isnumeric():
        mushroom = int(mushroom)
        if mushroom < 100:
            small.append(mushroom)
        elif mushroom > 100 and mushroom < 200 or mushroom == 100:
            medium.append(mushroom)
        elif mushroom > 200 or mushroom == 200:
            large.append(mushroom)
    else:
        print("that is not a size for a mushroom")