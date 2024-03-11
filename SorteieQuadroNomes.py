#Faça um programa que sorteie quatro nomes.

import random
#nome = ["Rodrigo", "Afonso", "Mara", "Mayara", "Idelfonso", "Marluce", "Mateus", "Izabel"]

aluno1 = input("ALUNO 01 > ")
aluno2 = input("ALUNO 02 > ")
aluno3 = input("ALUNO 03 > ")
aluno4 = input("ALUNO 04 > ")

nomearmz = [aluno1, aluno2, aluno3, aluno4] #colchete forma uma lista

nomealeatorio = random.choice(nomearmz)
random.shuffle(nomearmz) #shuffle deixa aleatorio o que está na lista,
#quando exibir a lista, ela estará listada de forma aletaória.

print("Nome Aleatório", nomealeatorio)
print("Ordem  de apresentação", nomearmz)
