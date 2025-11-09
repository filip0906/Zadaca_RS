suma=0

for broj in range(2,101,2):
    suma+=broj
print("Zbroj parnih brojeva (FOR):", suma)

suma2=0
broj2=2

while broj2<=100:
    suma2+=broj2
    broj2+=2
print("Zbroj parnih brojeva (WHILE):", suma2)