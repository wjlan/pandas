import pandas as pd

df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# df = df.sort_values('Name')  # sort_values is a function, it returns a sorted object, not the original object dataframe

df = df.sort_values('Name', ascending= False)  # descending

df = df.sort_values(['Type 1', 'HP'], ascending= False)

df = df.sort_values(['Type 1', 'HP'], ascending= [1,0])  # Type1 from low to high, HP from high to low
print(df)

