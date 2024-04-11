# Código está funcionando 
#falta contabilizar os numeros considerados e os desconsiderados
#ler número
atual = 0
soma = 0
ultimo= penultimo = antepenultimo = pre_antepenultimo= 0
aux_ultimo = aux_penultimo = aux_antepenultimo = aux_pre_antepenultimo = 0
qdt_considerados = qdt_desconsiderados = qdt_numeros = 0

# laço de repetição
while(atual >= 0):
  #atualiza as variavéis desse modo quando o nº atual não for zero
    if(atual != 0):
        pre_antepenultimo = antepenultimo
        antepenultimo = penultimo
        penultimo = ultimo
        ultimo = atual
    # variáveis que controlam os zeros que são digitados
    aux_pre_antepenultimo = aux_antepenultimo
    aux_antepenultimo = aux_penultimo
    aux_penultimo = aux_ultimo
    aux_ultimo = atual
    #recebe nummero atual
    atual = int(input("Digite um número? "))
    # condicinal para verificar se é hr de para o jogo
    if(atual <0):
        break
    else:
        soma = soma + atual
    # condicinal para retirar os numeros digitados errados
    if(atual == 0):
        #condicinal analizar se o usuario digitou mais de 3 zeros
        if(atual== 0 and aux_ultimo == 0 and aux_penultimo == 0 and aux_antepenultimo == 0):
                print("Atenção: NÃO é permitido inserir mais de três 0 consecutivos!")
        else:
         #atualiza as variavéis desse modo quando o nº atual  for zero
            soma = soma - ultimo
            ultimo = penultimo
            penultimo = antepenultimo
            antepenultimo = pre_antepenultimo        

print("Zero Cancela Finalizado!")
print("Soma total: ", soma)
