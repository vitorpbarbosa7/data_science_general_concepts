n = 200
sigma = 0.1

m_p = c(1.2, 1.2)
m_n = c(0.3, 0.3)

posc = rbind(rnorm(n, m_p[1], sigma), rnorm(n, m_p[2], sigma))
negc = rbind(rnorm(n, m_n[1], sigma), rnorm(n, m_n[2], sigma))

quartz()
plot(t(posc), pch = 1, xlim = c(0, 2), ylim = c(0, 2))
par(new = T)
plot(t(negc), pch = 5, axes = F, xlab = '', ylab = '')


