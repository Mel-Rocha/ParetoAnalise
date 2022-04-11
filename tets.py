NO = [54, 30, 26]
FR = [50.3, 23.5, 3.8]
FA = [50.3, 73,8, 80.3]


print(' NO  |  FR  |  FA   ')
print('____________________')
for i in range(len(NO)):
  print(f' {NO[i]:<4}| {FR[i]:<5}| {FA[i]:<5}|')



NO = [140, 125, 65, 60, 44, 30, 20, 19]
SNO = 503

counter = -1
for i in NO:
    counter += 1
    FR = (NO[counter] / SNO) * 100
    print(f'{FR:.2f}')


'''
Por meio do laco for percorro o numero de ocorrencias (NO), e efetuo a frequencia relativa atraves do numero de ocorrencia e seu respectivo indice 
determinado pelo (counter) e divido pela soma numero de ocorrencia, e multiplico o valor por 100 para encontrar a porcentagem
'''

l1 = [1, 3, 5]
l2 = [2, 4, 6]
s = []


for elem1, elem2 in zip(l1, l2):
    s.append(elem1 + elem2)
print(f'Soma Por indice {s}')
def somar_s(s):
    st = 0
    for c in s:
        st += c
    print(f'Soma Total: {st}')

somar_s(s)
'''
soma os elements das duas listas
'''

