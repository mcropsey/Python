import math
from typing import List, Iterator



def sen(numbers):
    mylist = []
    for x in (numbers):
        if ( x % 2 == 0):
            mylist.append(x ** 2)
    return mylist

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6]
    print("Sqare of even numbers is: ", sen(numbers))