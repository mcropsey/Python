mylist = [1,2,3]
largest = mylist[0]
second_largest = mylist[0]

for i in range(1, len(mylist)):
    if mylist[i]> largest:
        second_largest=largest
        largest=mylist[i]
    elif mylist[i]>second_largest:
        second_largest=mylist[i]

print("The Second Largest number is", second_largest)