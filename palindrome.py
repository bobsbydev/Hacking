"""TO CHeck palindrome"""

s1=input("Enter a string")
s1=s1.lower()
r1=s1[::-1]
if (s1==r1):
    print("YES")
else:
    print("NO")

