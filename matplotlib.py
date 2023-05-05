import numpy as np
import matplotlib.pyplot as plt 
labels = 'Alemanha', 'China', 'Russia', 'Estados Unidos', 'Grã-Bretanha'
medalhas = [17, 26, 19, 46, 27]
explode = (0, 0, 0, 0.1, 0) 

fig1, ax1 = plt.subplots()
ax1.pie(medalhas, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
fig1.suptitle('Conquistas de medalhas de ouro dos cinco países\n mais bem sucedidos nas olimpíadas de verão de 2016.',fontsize=12)
plt.show()

fig = plt.figure()
fig.suptitle("Popularidade das principais linguagens de programação em 2017 ",fontsize=12)
sub1 = fig.add_subplot(1,1,1)
programas=['Java','Python','PHP','JavaScript','C#','C++',]
popularidade=[22.2,17.6,8.8,8,7.7,6.7]
sub1.bar(programas,popularidade)
sub1.set_ylabel("Popularidade",fontsize=12)
sub1.set_xlabel("Linguagens de programação",fontsize=12)
plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
Notas_Matematica = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
Notas_Ciencias = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
plt.figure(figsize=(13,5))
plt.xlim([0,11])
plt.ylim([0,110])
plt.xlabel('Quantidades de provas')
plt.ylabel('Notas')
plt.title('Gráfico de Dispersão de notas')
plt.scatter(x,Notas_Ciencias,edgecolors= 'black',label = "Notas de Ciências")
plt.scatter(x,Notas_Matematica,edgecolors= 'black',label = "Notas de Matemática")
plt.legend()
plt.show()

