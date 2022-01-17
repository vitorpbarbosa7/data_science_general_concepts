# install.packages('nonlinearTseries')
require(nonlinearTseries)
setwd('/media/vpb/GD_/USP/DS/01Git/00_datascience_general/01_timeseries')
series = as.vector(read.csv('data/aapl.csv')$close)
qseries 

plot(series, pch = 20)
acf(series,lag.max = 200)


# lagging -----------------------------------------------------------------
lag = 30
end = length(series)-lag+1
length(series[1:end])
length(series[lag:length(series)])
phase = as.data.frame(cbind(series[1:end],series[lag:length(series)]))
plot(x = phase$V1, y = phase$V2)


# lagging with buildtakens ------------------------------------------------
plot(buildTakens(series, 2, 30))


# acf ---------------------------------------------------------------------
plot(series)
acf(series, lag.max = 1200)

# Takens ------------------------------------------------------------------
takens = buildTakens(series, embedding.dim = 6, time.lag = 60)

recurrencePlot(takens, radius = 15)












