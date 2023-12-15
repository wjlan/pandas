import pandas as pd

# poke = pd.read_csv('pokemon_data.csv')

df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(poke)  # all the data
# print(poke.head(3))  # top three rows of data

# print(df.head(3))

# Read Headers
# print(df.columns)

# Read each column
# print(df.['Name'])
# print(df[['Name', 'Type 1', 'HP']]) 
    #   when you want to select multiple columns from a DataFrame, you use a double set of square brackets [[...]]. This is because the outer brackets denote indexing or selecting columns, and the inner brackets are used to define a list of column names you want to select

# Read each row
# print(df.head(4))
# print(df.iloc[1])    #iloc stands for integer location
# print(df.iloc[0:4]) 

# for index, row in df.iterrows():
    # print(index, row)
    # print(index, row['Name'])

print(df.loc[df['Type 1'] == "Grass"])

# Read a specific location (R, C)
# print(df.iloc[2,1])

