# depois ver o que fazer quando o primeiro numero digitado é 0
#lucia disse para imprimir que não há numero digitado
#ler número
atual = 0
soma = 0
ultimo = penultimo = antepenultimo = pre_antepenultimo= 0
qdt_considerados = qdt_desconsiderados = qdt_numeros = 0
# laço de repetição
            while(atual >= 0):
                pre_antepenultimo =antepenultimo
                antepenultimo = penultimo
                penultimo = ultimo
                ultimo = atual
                atual = int(input("Digite um número: "))
                soma = soma + atual
                if(atual == 0):
                    soma = soma - ultimo
                    ultimo = penultimo
                    penultimo = antepenultimo
                    antepenultimo = pre_antepenultimo
                print("O ultimo numero", ultimo)
                print("O penultimo numero", penultimo)
                print("O antepenultimo numero", antepenultimo)
                print("O pre antepenultimo numero", pre_antepenultimo)
                print("soma ", soma)