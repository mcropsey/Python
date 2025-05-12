str1 = "this is new statement"

def get_reverse_string(new_string):
    reversed_string = ""
    total_count = len(new_string) - 1
    for i in range(0, len(new_string)):
        reversed_string += new_string[total_count-i]
    return reversed_string

print(get_reverse_string(str1))