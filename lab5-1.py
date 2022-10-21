numList = []

if len(numList) != 9:
    while len(numList) <= 9:
        number = int(input("enter ten unique number:"))
        if number in numList:
            print("please enter unqie number:")
        else:
            numList.append(number)

print(numList)
