# depois ver o que fazer quando o primeiro numero digitado é 0
#lucia disse para imprimir que não há numero digitado
#ler número
atual = 0
soma = 0
ultimo = penultimo = antepenultimo = 0
qdt_considerados = qdt_desconsiderados = qdt_numeros = 0

# laço de repetição
while(atual >= 0):
        if(atual != 0):
             antepenultimo = penultimo
             penultimo = ultimo
             ultimo = atual
        elif(atual == 0):
            
            soma = soma - ultimo
            ultimo = penultimo
            penultimo = antepenultimo
            antepenultimo = 0
        atual = int(input("Digite um número? "))
        soma = soma + atual
        if(soma == 0):
            print("Não há nenhum número digitado!")
        print("O ultimo numero", ultimo)
        print("O penultimo numero", penultimo)
        print("O antepenultimo numero", antepenultimo)
        print("soma ", soma)
       