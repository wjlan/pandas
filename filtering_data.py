import pandas as pd

df = pd.read_csv('pokemon_data.txt', delimiter='\t')

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.to_csv('filtered.csv')

# print(new_df)
# new_df = new_df.reset_index()  # both old index and new index are kept
# print(new_df)

new_df = new_df.reset_index(drop=True)  # drop=True get rif of the old index
print(new_df)

df = df.loc[~df['Name'].str.contains('Mega')]
print(df)