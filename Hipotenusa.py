import math
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.


'''
cat1 = float(input("DIGITE CATETO 1 "))
cat2 = float(input("DIGITE CATETO 2 "))

hipotenusa = (cat1**2 + cat2**2) ** (1/2)

print("{:.2f2}".format(hipotenusa))'''

from math import hypot
co = float(input("Digite o cateto oposto "))
ca = float(input("Digite o cateto adjacente "))
hi = hypot(co,ca)
print("A hipotenusa é {:.2f}".format(hi))
print("Fim")