empirical_risk = 0.01

n_samples = 1000000

#Maior margem para numero de amostras
margin = seq(0.1, 0.2, length=n_samples)

#Maior raio para maior numero de amostras
radius = seq(0.9, 1, length=n_samples)

nivel_confianca = 0.05
c = 1

n=1:n_samples

expected_risk = empirical_risk + sqrt((c/n)*((radius^2/margin^2)*log(n)^2 + log(1/nivel_confianca)))


plot(expected_risk,t="l",ylim=c(0,1))
