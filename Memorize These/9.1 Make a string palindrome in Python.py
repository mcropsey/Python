def isPalindrome(s):
    if s.lower() == s[::-1].lower():
        print("Yes")
    else:
        print ("No")

s = "Nitin"
result = isPalindrome(s)