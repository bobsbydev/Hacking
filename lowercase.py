'''wapp to count lowercase and upper case'''

lc,uc=0,0
s1=input("Enter a string")
for c in s1:
    if c.isalpha():
        if c.islower():
            lc=lc+1
        else:
            uc=uc+1
print(lc,uc)        
