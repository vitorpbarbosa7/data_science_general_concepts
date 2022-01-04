hw <- data.frame(Height_cm=c(164, 167, 168, 169, 169, 170, 170, 170, 171, 172, 172, 173, 173, 175, 176, 178),
                 Weight_kg=c( 54,  57,  58,  60,  61,  60,  61,  62,  62,  64,  62,  62,  64,  56,  66,  70))

#Dado que dados escalonados, padronizados são múltiplos do desvio padrão, então > 2 estou dizendo que aquele que for 
#2x o desvio padrão será retirado. 
height_outlier = abs(scale(hw$Height_cm)) > 2
weight_outlier = abs(scale(hw$Weight_kg)) > 2

#16 é um código para um dos plot characters
pch = (height_outlier | weight_outlier) * 16

plot(hw, 
     pch = pch)

#Distância estatística para cada observação
maha = as.data.frame(mahalanobis(hw, colMeans(hw), cov(hw)))

#Ordenando esta lista 