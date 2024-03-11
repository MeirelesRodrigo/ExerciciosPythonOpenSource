#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = float(input("DIGITE UM NÚMERO "))
dobro = num*2
triplo = num*3
raiz = num**(1/2)

print("")
print("O NÚMERO ESCOLHIDO FOI ",num)
print("O DOBRO É ",dobro)
print("O TRIPLO É ",triplo)
print("A RAIZ É {:.2f}".format(raiz))