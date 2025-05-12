def reverse_while_loop(s):
    i = ''
    length = len(s) - 1
    while length >= 0:
        i = i + s[length]
        length = length - 1
    return i

input_str = 'python'
obj = reverse_while_loop(input_str)
print(obj)