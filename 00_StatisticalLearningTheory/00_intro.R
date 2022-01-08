n = 1:1000

# we accept here an error of 0.1 for epsilon
# difference between expected risk and empirical risk?
epsilon = 0.1

# possivel ver como conforme n aumenta, temos 
# uma menor diferenca entre o Risco Empirico e o 
# Risco Verdadeiro 
# Quanto menor for este erro, maior sera o poder de generalizacao 
# do modelo 

# this here is the probability that 
# the empirical risk minus the true risk is 
# greater than epsilon
plot(2*exp(-2*n*epsilon^2))
