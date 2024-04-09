# depois ver o que fazer quando o primeiro numero digitado é 0
#lucia disse para imprimir que não há numero digitado
#ler número
numero = 0
soma = 0
ultimo = penultimo = antepenultimo = pre_antepenultima = pre_pre_antepenultima = 0
qdt_considerados = qdt_desconsiderados = qdt_numeros = 0

# laço de repetição
while(numero >= 0):
    pre_pre_antepenultima = pre_antepenultima
    pre_antepenultima = antepenultimo
    antepenultimo = penultimo
    penultimo = ultimo

    ultimo = int(input("Digite um número? "))
    soma = soma + ultimo

    print(ultimo)
    print(penultimo)
    print(antepenultimo)
    print(pre_antepenultima)
    print(pre_pre_antepenultima)

    if(soma == 0):
        print("Não há nenhum número digitado!")
    else:
        if(ultimo == 0):
            soma = soma - penultimo
            if(penultimo == 0 and antepenultimo != 0):
                print("teste")
                soma = soma - pre_antepenultima
                pre_antepenultima = pre_pre_antepenultima
            else:
                soma = soma - pre_pre_antepenultima

            
        # print(soma)
        # print("O ultimo numero", ultimo)
        # print("O penultimo numero", penultimo)
        # print("O antepenultimo numero", antepenultimo)
        print("soma ", soma)