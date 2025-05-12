from itertools import permutations
num_list = [99, 89, 992, 743, 9]
latest_largest_num = "0"
new_list = []
for per in permutations(str(number) for number in num_list):
  new_list.append(''.join(per))
latest_largest_num = max(new_list, key=int)
print(latest_largest_num)