print("-------------------")
print(" CALCULADORA TINTA")
print("-------------------")

altura = float(input("INFORME A ALTURA DA PAREDE: "))
largura = float(input("INFORME A LARGURA DA PAREDE: "))

area = altura*largura
tinta = area/2

print("SUA PAREDE MEDE {} X {}, CONTÉM UMA ÁREA DE {} M²".format(altura,largura,area))
print("SERÁ NECESSÁRIO {} L DE TINTA PARA PINTAR ESSA PAREDE".format(tinta))