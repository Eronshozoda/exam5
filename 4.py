import random
a=int(input())
code=[1234567890]
d=random.choices(code)
for i in d:
        if a==len(i):
            print(i)