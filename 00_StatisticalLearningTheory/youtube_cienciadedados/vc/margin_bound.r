shatt = function(n,R,rho) {
	shatt_values = ((R^2)/(rho^2))*(log(n)^2)
	return(shatt_values)
}


R = 1
n=1:100000


rho = 0.999
rho2 = 0.95
rho3 = 0.02

print(paste("m",rho))

plot(shatt(n,R,rho), t="l", col=1)
lines(shatt(n,R,rho2),  col=2)
lines(shatt(n,R,rho3), col=3)
legend(x="bottomright", legend=c(paste(rho),paste(rho2),paste(rho3)), lty=1,col = c(1,2,3))
