import pandas as pd

df = pd.read_csv('modified.csv')

# df = df.groupby(['Type 1']).mean()  # calculated the mean value by group Type 1
# print(df)

# df = df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) # we took the average of all steel pokemons, they have the highest defense
# print(df)

# df = df.groupby(['Type 1']).sum()
# print(df)

df['count'] = 1
df = df.groupby(['Type 1', 'Type 2']).count()['count']
print(df)
