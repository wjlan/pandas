import pandas as pd

df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(df.head(5))

# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df)

# df = df.drop(columns=['Total'])
# print(df)

df['Total'] = df.iloc[:, 4:10].sum(axis=1)  # axis=1 means sum up horizontally, axis=0 means vertically sum up
# print(df.head(5))

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))

df.to_csv('modified.csv', index=False)  # index=False可以去掉index
# df.to_excel('modified.xlsx', index=False)
df.to_csv('modified.txt', index=False, sep='\t')  # sep='\t' means seperate with tabs
