import math
#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

angulo = float(input("DIGITE UM ÂNGULO QUALQUER "))

seno = math.sin(math.radians(angulo)) #transformar em radiano para o calculo correto
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O ANGULO ESCOLHIDO FOI {}ª, "
      "SENO {:.2f}, COSSENO {:.2f}, TANGENTE {:.2f} ".format(angulo, seno,cosseno,tangente))