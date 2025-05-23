import math
def suma(x, y):
    return x+y

def resta(x, y):
    return x-y

def divis(x, y):
    return x/y

def raiz(x):
    return math.sqrt(x)

def potn(x):
    return x**2

a = 3
b = -2
c = -3
"""
pont(b) #El cuadrado de b
4*a*c   #El producto de 4, a y c
resta(potn(b), 4*a*c)   #Resta de b^2 con 4ac
raiz(resta(potn(b), 4*a*c)) #Raiz a la resta de b^2 con 4ac
x1 = divis(suma(-b, raiz(resta(potn(b), 4*a*c))), 2*a)
x2 = divis(resta(-b, raiz(resta(potn(b), 4*a*c))), 2*a)
"""
x1 = divis(suma(-b, raiz(resta(potn(b), 4*a*c))), 2*a)
x2 = divis(resta(-b, raiz(resta(potn(b), 4*a*c))), 2*a)

print(f"Las soluciones del trinomio\n{a}x^2+{b}x+{c} son\n{x1} y {x2}")