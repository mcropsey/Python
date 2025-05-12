def reverse_for_loop(s):
    i = ''
    for c in s:
        i = c + i  # appending chars in reverse order
    return i

input_str = 'python'
obj = reverse_for_loop(input_str)
print(obj)