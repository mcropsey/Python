from functools import cmp_to_key

def get_key(first, sec):
  if str(first) + str(sec) > str(sec) + str(first):
    return -1
  return 1

num_list = [99, 89, 992, 743, 9]
latest_largest_num = "0"
new_list = sorted(num_list, key=cmp_to_key(get_key))
latest_largest_num = "".join(str(num1) for num1 in new_list)
print(latest_largest_num)