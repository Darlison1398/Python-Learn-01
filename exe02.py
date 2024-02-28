Npares = 0
Nimpares = 0

somaPares = 0
somaImpares = 0

while(True): 
    numero = int(input("Digite um número: "))

    if (numero == 0): break

    elif (numero < 0): continue

    elif (numero % 2 == 0):
        Npares += 1

        somaPares += numero
    
    else:
        Nimpares += 1
        somaImpares += numero

nTotal = Nimpares + Npares

somaTotal = somaImpares + somaPares

mediaGeral = somaTotal / nTotal

mediaPares = somaPares / Npares

mediaImpares = somaImpares / Nimpares

print("O total de números digitados é %d e a média é %.2f" % (nTotal, mediaGeral))

print("\nO total de números pares digitados é %d e a média é %.2f" % (Npares, mediaPares))

print("\nO total de números impare digitados é %d e a média é %.2f" % (Nimpares, mediaImpares))
