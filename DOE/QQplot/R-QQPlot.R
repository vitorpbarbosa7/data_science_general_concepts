setwd('C:\\GD\\DS\\DS_Share\\DOE\\QQplot')

data = read.csv('data.csv', header = T, sep = ',')

qqnorm(data$Residuals, pch = 1, frame = FALSE)
qqline(data$Residuals, col = 'steelblue', lwd = 2)


# Anderson Darling Normality Test -----------------------------------------
#install.packages("nortest")
library(nortest)
ad.test(data$Residuals)
#DEU CERTO