R_emp_f_alg1 = 0.01
R_emp_f_alg2 = 0.05

n=1:100000

N_F_2n_alg1 = n^10
N_F_2n_alg2 = n^4

delta = 0.05 #nivel de confianca desejado

R_exp_f_alg1 = R_emp_f_alg1 + sqrt(4/n*(log(2*N_F_2n_alg1) - log(delta)))
R_exp_f_alg2 = R_emp_f_alg2 + sqrt(4/n*(log(2*N_F_2n_alg2) - log(delta)))

#print(R_exp_f_alg1)

plot(R_exp_f_alg1, t="l", ylim = c(0,1), col=1)
lines(R_exp_f_alg2, col=2)
#legend(1, 95, legend=c("n^10", "n^4"), col=c(1,2))
legend(x = "topright", legend=c("Line 1", "Line 2"),
       col=c("black", "red"), lty=1, cex=0.8)
