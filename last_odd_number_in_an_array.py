n=int(input())
lst=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if lst[i]%2==1:
        print(lst[i])
        break