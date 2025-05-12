a = 10
b = 20
print("Before swapping value of a is", a , "and b is", b)

#code to swap a & b
a = a ^ b
b = b ^ a
a = b ^ a
print("After swapping value of a is", a , "and b is", b)