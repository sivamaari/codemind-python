a=int(input())
b=int(input())
q=0
w=0
for i in range(1,a):
    if a%i==0:
        q=q+i
for i in range(1,b):
    if b%i==0:
        w=w+i
        
        
        
if q==b and a==w:
   print("Amicable")
else:
   print("Not Amicable")
        