"""Kvadriraj"""
kvadrat = lambda x: x**2

print(kvadrat(5))

"""Zbroji pa kvadriraj"""

zbroji_pa_kvadriraj = lambda x,y: (x+y)**2
print(zbroji_pa_kvadriraj(2,5))

"""kvadriraj duljinu niz brojeva"""
kvadriraj_duljinu = lambda lista: [x**2 for x in lista]
print(kvadriraj_duljinu([1,2,3,4]))

"""pomnozi i potenciraj"""
pomnozi_i_potenciraj = lambda x,y: (y*5)**x
print(pomnozi_i_potenciraj(2,3))

"""parni brojevi"""
paran_broj = lambda x: True if x%2==0 else None
print(paran_broj(5))