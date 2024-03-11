#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DiGA SE ELA COMEÇA OU NAO O NOME “SANTO”

cidade = str(input("DIGITE O NOME DA CIDADE "))
cidade = cidade.lower()

condicao = "santo" in cidade
print(condicao)

if condicao == True:
    print("A CIDADE CONTÉM SANTO ")
else:
    print("A CIDADE NAO CONTÉM SANTO ")

cidade = str(input("DIGITE O NOME DA CIDADE ")).strip()
verificador = cidade[:5].upper() == 'SANTO'
print(verificador)
if verificador == True:
    print("A CIDADE COMEÇA COM SANTO")
else:
    print("A CIDADE NAO COMEÇA COM SANTO")
