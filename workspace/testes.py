# depois ver o que fazer quando o primeiro numero digitado é 0
#lucia disse para imprimir que não há numero digitado
#ler número

ultimo = penultimo = antepenultimo = soma = numero = 0
qdt_considerados = qdt_desconsiderados = qdt_numeros = 0

# laço de repetição
while(numero >= 0):
    antepenultimo = penultimo
    penultimo = ultimo

    ultimo = int(input("Digite um número? "))
    soma = soma + ultimo

    if(soma == 0):
        print("Não há nenhum número digitado!")
    else:
        if(ultimo == 0):
            soma = soma - ultimo
            ultimo = penultimo
            penultimo = antepenultimo
            antepenultimo = -1
            
    print(ultimo)
    print(penultimo)
    print(antepenultimo)
    print(soma)