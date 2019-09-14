# reading file
import pandas as pd
data = pd.read_csv('resources/91_input.txt')
data.columns = ['symbols']

# data preparation
symbols = []
for i in range(len(data)):
    for j in range(len(data['symbols'][i])):
        symbols.append(data['symbols'][i][j])
data = pd.DataFrame(symbols)
data.columns = ['symbols']

# looking for rare symbols
rare = data['symbols'].value_counts().keys().tolist()
print rare

# get string
answ = ''
list = rare[-9:]
list.remove('>')
for i in range(len(list)-1, -1, -1):
    answ += list[i]
print answ  # answer: 'equality' from rare letters
