sexo = input("M - Masculino, ou F - para Feminino:  ")
altura = float(input("Digite a alturaem metros: "))

peso = 0

if sexo.upper() == "M": 
    peso = ( 72.7 * altura) - 58

elif sexo.upper() == "F":
    peso = (62.1 * altura) - 44.7

if peso != 0:
    print("O peso ideal para sua altura seria %.2f" % peso)

else:
    print("Não sabemos o peso ideal para o seu gênero.")



