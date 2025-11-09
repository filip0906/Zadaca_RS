a=0
b=1

print("3. Fibonacci niz do 1000 (WHILE):")
while a<=1000:
    print(a)
    a,b=b,a+b

print("3. Fibonacci niz do 1000 (FOR):")
c=0
d=1
for _ in range(0,1000):
    if c>1000:
        break
    print(c)
    c,d=d,c+d