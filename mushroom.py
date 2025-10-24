sizes = []
large = []
medium = []
small = []
check = False 
while check == False:
    print("1. add sizes ")
    print("2. catigorize mushrooms by sizes ")
    option = input("what option would you like ")
    if option == "1":
        size = input("what sizes are mushrooms? ")
        if size.isnumeric():
            size = int(size)
            sizes.append(size)
        else:
            print("that is not a numeric size")
    elif option == "2":
        for i in range(len(sizes)):
            if sizes[i] < 100:
                small.append(sizes[i])
            if sizes[i] >= 200:
                medium.append(sizes[i])
            if sizes[i] >= 200:
                large.append(sizes[i])
        check = True 
print(small)
print(medium)
print(large)