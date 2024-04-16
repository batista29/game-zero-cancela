# depois ver o que fazer quando o primeiro número digitado for 0
#lucia disse para imprimir que não há número digitalizado
# Código está funcionando
# falta contabilizar os números considerados e os desconsiderados
#ler número
atual  =  0
soma  =  0
ultimo  =  penultimo  =  antepenultimo  =  pre_antepenultimo =  0
ultimo =  penultimo  =  antepenultimo  =  pre_antepenultimo =  0
aux_ultimo  =  aux_penultimo  =  aux_antepenultimo  =  aux_pre_antepenultimo  =  0
qtd_considerados  =  qtd_desconsiderados  =  qtd_numeros  =  0

# laço de repetição
while ( atual  >=  0 ):
  #atualiza as variaveis desse modo quando o nº atual não for zero
    if ( atual  !=  0 ):
        pre_antepenultimo  =  antepenultimo
        antepenultimo  =  penultimo
        penultimo  =  ultimo
        ultimo  =  atual
    # variáveis ​​que controlam os zeros que são digitados
    aux_pre_antepenultimo  =  aux_antepenultimo
    aux_antepenultimo  =  aux_penultimo
    aux_penultimo  =  aux_ultimo
    aux_ultimo  =  atual
    #recebe número atual
    atual  =  int ( input ( "Digite um número: " ))
    # condicinal para verificar se é hr de para o jogo
    if (atual < 0):
        break
    else :
        soma  =  soma  +  atual
    if (atual>0):
         qtd_considerados=qtd_considerados+1
    #condicinal para retirar os números digitados errados
    if ( atual  ==  0 ):
        qtd_desconsiderados=qtd_desconsiderados+1
        qtd_considerados=qtd_considerados-1
        #condicinal analisar se o usuário digitou mais de 3 zeros
        if ( atual ==  0  and  aux_ultimo  ==  0  and  aux_penultimo  ==  0  and  aux_antepenultimo  ==  0 ):
                qtd_desconsiderados=qtd_desconsiderados-1
                qtd_considerados=qtd_considerados+1
                print ( "Atenção: NÃO é permitido inserir mais de três 0 consecutivos!" )
        else :
         #atualiza as variaveis desse modo quando o nº atual for zero
            soma  =  soma  -  ultimo
            ultimo  =  penultimo
            penultimo  =  antepenultimo
            antepenultimo  =  pre_antepenultimo        

print ("Zero Cancelamento Finalizado!" )
print ("Soma total: ", soma )
print (f"A quantidade de números considerados é {qtd_considerados} e a quantidade de números desconsiderados é de {qtd_desconsiderados} ")