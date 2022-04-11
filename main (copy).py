'''
Objetivo: Desenvolver um programa que receba um arquivo txt e devolva como saida uma tabela com a analise de Pareto
'''



#<Decoracao>
print("--" * 30)
print('                ANÁLISE DE PARETO')
print("--" * 30)
print("")
#</Decoracao>



#<LeituraTxt>

dados = open('arquivo.txt', 'r')
'''
a variavel dados consiste na funcao open chamando o arquivo txt (arquivo.txt) o parametro 'r' indica que apenas faremos a leitura do arquivo (reading = leitura).
'''

#codeDesabilitado
#print(dados.read())
'''
imprime os dados na tela
'''

dados_brutos = dados.readlines()
'''
o metodo readlines retorna o arquivo em forma de lista.
'''

dados_rol = (dados_brutos)
'''
a funcao sorted constroi uma nova lista ordenada
'''

lista1 = []

for i in dados_rol:
    lista1.append(i.rstrip())
#print(f'Dados: {lista1}')
print('')
'''
A lista1 e criada e os valores de dados_rol sao inseridos nela por meio do metodo append, o metodo rstrip remove os caracteres de marcacao (o /n)
'''

dados.seek(0)
'''
Quando executamos a funcao read o arquivo todo e lido e o ponteiro de localizacao do arquivo vai pro final, de modo que se chamarmos a funcao read mais uma vez nao leremos nada, pois o arquivo ja foi lido e o ponteiro esta no final, por isso executamos o metodo seek em cima do objeto file (file = dados), para retornar ao inicio do arquivo, por isso o parametro e 0, para retornar ao comeco.
'''

#codeDesabilitado
#print(dados.readlines())
'''
imprime os dados em forma de lista, com os caracteres de controle
'''

dados.close()
'''
Fecha dados.
'''

#</LeituraTxt>

#<NOColuna>


def remove_duplicatas(lista1):
    l = []
    for i in lista1:
        if i not in l:
            l.append(i)
    #l.sort()
    return l

print('DADOS SEM DUPLICATAS')
listaSemDuplicatas = remove_duplicatas(lista1)
for c in listaSemDuplicatas:
  print(f'{c}')

print('')
'''
A funcao remove_duplicatas recebe como parametro a lista1 (lista1 = dados_rol, a lista1 consiste nos dados ordenados em ordem crescente, porem repetidos). A lista 'l' e criada e o for e usado para percorrer a lista1, se 'i' nao estiver em 'l', 'l' recebe o valor de 'i', 'l' e ordenada pelo sort, e lista esta sem duplicatas
'''

#</NOColuna>

#<FOColuna>

lenLista1 = len(lista1)
lenListaSemDuplicatas = len(listaSemDuplicatas)
'''
A funcao len conta quantas posicoes as listas possuem
'''

counter = -1
NO_string = []
NO = []
FR = []
FA = []
O_NO_string = []
l1 = []


for i in listaSemDuplicatas:
    counter += 1
    O = listaSemDuplicatas[counter]
    NO_string = lista1.count(O)
    NO.append(int(NO_string))
    #NO.sort(reverse=True)
    
    print(f'{O:^30} {NO_string}')#, end='')

  
    #O_NO.append(O[i] , NO_string[i])
    #print(f'NUMERO OCORRENCIA: {NO_string} ')

    def somar(NO):
        SNO = 0
        for c in NO:
            SNO += c
        print(f'TOTAL (SOMA NUMERO OCORRENCIA): {SNO}')
        counter = -1
        print('')
        print('FREQUENCIA RELATIVA')
        for i in NO:
            counter += 1
            FR_string = (NO[counter] / SNO) * 100
            FR.append(float(FR_string))
            print(f'{FR_string:.2f}')
            
        
        
            
            
            
           
            


somar(NO)



'''
Percorro a listaSemDuplicatas e através do contador (counter) mudo o index da lista sem duplicatas mostrando a ocorrencia (O). O numero de ocorrencias (NO_string) é procurado na lista1 através do count, converto os valores das string para int e adiciono na lista NO (Numero de Ocorrencias). Atraves da funcao somar, efetuo a Soma Numero Ocorrencia (SNO) e por meio do laco (c) aplicado na lista (NO) efetuo a soma
'''
'''
Por meio do laco for percorro o numero de ocorrencias (NO), e efetuo a frequencia relativa atraves do numero de ocorrencia e seu respectivo indice 
determinado pelo (counter) e divido pela soma numero de ocorrencia, e multiplico o valor por 100 para encontrar a porcentagem, logo em seguida adiciono os valores da variavel FR_string na lista com numeros flutuantes (FR)
'''

#</FOColuna>

#<FRColuna>


def somar_FR(FR):
    SFR = 0
    for c in FR:
        SFR += c
    print(f'TOTAL (FREQUENCIA RELATIVA): {SFR:.2f}')

somar_FR(FR)

'''
Efetuo  a soma da frequencia relativa (FR) por meio do laco que percorre a lista FR
'''

#</FRColuna>

#<FAColuna>



'''
Frequencia Relativa (FR) ordenada em ordem decrescente
'''


FA = []

FAO = FR[0]
FA.append(float(FR[0]))

c1 = 0
c2 = 1

for v in FR:
  if len(FA) < len(FR):
    FA.append(float(FA[c1] + FR[c2]))
    c1 += 1 
    c2 += 1
    


print('')
print('FREQUENCIA ACUMULADA')
for c in FA:
  print(f'{c:.2f}')
    
'''
Criacao da lista vazia de Frequencia Acumulada(FA), declaracao da variavel FA0 correspondente ao indice 0 da lista FR. Os contadores (c1 e c2) serao utilizados no laco for com a finalidade de realizar a soma entre o elemento do primeiro indice da lista FA e o segundo elemento da lista FR ate o fim da lista FR, se o tamanho da lista FA for inferior ao tamanho da lista FR.

O laco for e utilizado para apresentar a lista FA em tabela, o c e cada valor da frequencia acumulada
'''


#</FAColuna>

print('')
print(f'  NO   |   FR   |   FA  ')
for i in range(len(FA)):
  
  #O_NO_string = listaSemDuplicatas[i] + NO[i]
  
  O_NO_string.sort(reverse=True)
  NO.sort(reverse=True)
  #print(f'{listaSemDuplicatas[i]:^30} ', end='')
  print(f'{NO[i]:^7}| {FR[i]:^7.2f}|  {FA[i]:^7.2f}')

  
''' 
for i in listaSemDuplicatas:
    counter += 1
    #O = listaSemDuplicatas[counter]
    
    NO_string = lista1.count(i)
    NO.append(int(NO_string))
    NO.sort(reverse=True)
    
    print(f'OCORRENCIA: {listaSemDuplicatas} {NO_string}')



O_NO_string = sorted(matriz,key=lambda x:x [1], reverse=True)
 
''' 
