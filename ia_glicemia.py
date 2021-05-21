'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 1
Alunos
Arthur de Oliveira - 89187
Gabriel Bega - 87442
'''
RED   = "\033[1;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
from sklearn import tree
features = [99, 120, 60], [80, 139, 100], [94, 60, 98], [60, 30, 80], [76, 90, 120], [94, 112, 70], [83, 121, 32], [89, 78, 135], [22, 123, 97], [54, 93, 128], [101, 141, 189], [124, 146, 104], [124, 159, 198], [120, 148, 180], [121, 186, 120], [112, 196, 160], [115, 154, 100], [107, 167, 198], [109, 187, 180], [123, 199, 120], [126, 241, 289], [127, 200, 204], [129, 259, 298], [130, 248, 280], [131, 286, 220], [142, 296, 260], [165, 254, 200], [167, 267, 298], [199, 287, 280], [143, 299, 220]


#Usamos 0 para green, 1 para yellow e 2 para red
labels = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
#j = em jejum, ps = pós-sobrecarga, gc = glicemia casual
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
j = int(input('Digite o valor da glicemia em jejum:'))
ps = int(input('Digite o valor da glicemia pós-sobrecarga:'))
gc =int(input('Digite o valor da glicemia glicemia casual:'))
x = classif.predict([[j, ps, gc]])
if x == 0:
    print(GREEN + 'O nível de glicose está normal!')
elif x == 1:
    print(YELLOW + 'O nível de tolerância a glicose está diminuído!')
else:
    print(RED + 'Diagnóstico de Diabetes Mellitus!')
print(BLUE + 'As respostas do programa precisam ser analisadas por um médico especialista e essas informações não devem ser usadas como diagnóstico definitivo!')