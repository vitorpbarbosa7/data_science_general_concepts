n = 1:100

poly = n^2
expo = 2^n

plot(poly,t="l")
lines(expo, col=2)
legend(x = "top", legend=c("polynomial (n^2)","exponential (2^n)"), lty=1, col=c("black","red"))
