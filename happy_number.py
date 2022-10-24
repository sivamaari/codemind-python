def num(n):
    c=0
    while n>0:
        r=n%10
        c+=r**2
        n=n//10
    return c
n=int(input())
while n>9:
    n=num(n)
if n==1 or n==7:
    print(True)
else:
    print(False)