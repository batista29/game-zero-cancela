# depois ver o que fazer quando o primeiro numero digitado é 0
#lucia disse para imprimir que não há numero digitado
#ler número
numero = 0
soma = 0
ultimo = penultimo = antepenultimo = 0
qdt_considerados = qdt_desconsiderados = qdt_numeros = 0

# laço de repetição
while(numero >= 0):
    antepenultimo = penultimo
    penultimo = ultimo
    ultimo = numero
    numero = int(input("Digite um número? "))
    soma = soma + numero
    if(soma == 0):
        print("Não há nenhum número digitado!")
    else:
        if(numero == 0):
            soma = soma - ultimo
        elif(numero == 0 and penultimo == 0):
            soma = soma - ultimo - penultimo
    print("O ultimo numero", ultimo)
    print("O penultimo numero", penultimo)
    print("O antepenultimo numero", antepenultimo)
    print("soma ", soma)