import operator

list1 = [[31, 60], [10, 10], [30, 20], [20, 25], [45, 30]]
dict1 = dict(list1)
sort_obj = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=False))
mylist = []

print(sorted(list1, key=lambda arg:arg[1]))