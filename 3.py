c=int(input())
with open("darexs.txt","r") as file:
    a=file.readlines()    
    print(a[c])
    