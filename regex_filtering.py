import pandas as pd
import re

df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# df = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
# df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)] # flags=re.I: ignore the uppercase or lowercase

df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

print(df)