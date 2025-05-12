from collections import Counter
mylist = [1,1,1,8,7,8,1,2,9,2]
result = dict(Counter(mylist))
print(result)