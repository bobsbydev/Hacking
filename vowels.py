vc,cc=0,0
s1=input("Enter a string")
for c in s1:
    if c.isalpha():
        if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
          vc=vc+1
        else:
            cc=cc+1
print(vc,cc)
