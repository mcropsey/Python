mylist = [12,45,78,60,98,95]
new_list = set(mylist)
new_list.remove(max(new_list))
print("The Second Largest number is", max(new_list))