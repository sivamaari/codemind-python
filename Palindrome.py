a=int(input())
z=a
rev=0
while a>0:
    b=a%10
    a=a//10
    rev=rev*10+b
if rev==z:
    print("True")
else:
    print("False")