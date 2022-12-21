import pandas as pd

df = pd.DataFrame({'val':[14,16,19,18]}, index = ['jun','jul','ago','ago'])

var = 'val'
window = 3
i = 2
mms = (df[var][i-1] + df[var][i] + df[var][i+1])/3

print(mms)

ws = [0.2,0.3,0.5]

sum(ws)

mmp = (ws[0]*df[var][i-1] + ws[1]*df[var][i] + ws[2]*df[var][i+1])/(sum(ws))
print(mmp)
