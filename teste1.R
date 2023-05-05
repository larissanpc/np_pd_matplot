# Gráfico de barras
programas <- c('Java','Python','PHP','JavaScript','C#','C++')
popularidade <- c(22.2, 17.6, 8.8, 8, 7.7, 6.7)
colors <- c('#8FBC8F', '#FFA07A', '#ADD8E6', '#FFD700', '#B0C4DE', '#87CEEB')

barplot(popularidade, names.arg=programas, col=colors, 
        main='Popularidade das principais linguagens de programação em 2017', 
        xlab='Linguagens de programação', ylab='Popularidade', cex.main=0.9)

# Gráfico de dispersão
x <- 1:10
Notas_Matematica <- c(88, 92, 80, 89, 100, 80, 60, 100, 80, 34)
Notas_Ciencias <- c(35, 79, 79, 48, 100, 88, 32, 45, 20, 30)

plot(x, Notas_Matematica, type='o', col='#FFA07A', ylim=c(0, 110), 
     xlab='Quantidades de provas', ylab='Notas', 
     main='Gráfico de Dispersão de notas')
lines(x, Notas_Ciencias, type='o', col='#87CEEB')
legend('topright', legend=c('Notas de Matemática', 'Notas de Ciências'), 
       col=c('#FFA07A', '#87CEEB'), lty=1, cex=0.8)

