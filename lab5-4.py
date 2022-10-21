values = [1,2,3,4,5]
newValues = values[:]

for i in range(len(values)):
    print("old value at index {} is: {}".format(i,values[i]))
    newValues[i] +=1
    print("new value at index {} is: {}\n".format(i,newValues[i]))
