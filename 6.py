summa=0
cnt=1
n=int(input())
for i in range (1,n+1):
    cnt*=i
    summa+=1//cnt
print(1+summa)