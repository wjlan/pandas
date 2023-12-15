import pandas as pd

df = pd.read_csv('modified.txt', delimiter='\t')

# df.loc[df['Type 1'] =='Fire', 'Legendary'] = 'True'
# print(df)

df.loc[df['Total'] > 50, ['Generation', 'Legendary']] = ['Test1', 'Test2']
print(df)