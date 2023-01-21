n = 1:10000000
epsilon = 0.1
a = 1

delta = 2*a*exp(2*log(n) - 2*n*epsilon^5)

plot(delta)

# plot(delta, ylim = c(0,1))

