a=input()
for i in range(len(a)):
    if type(a[i])==int:
        print('int :',a[i])
    if type(a[i])==str:
        print('str :',a[i])
    if type(a[i])==bool:
        print('bool :',a[i])
