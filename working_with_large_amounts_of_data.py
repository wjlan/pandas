import pandas as pd
df = pd.read_csv('modified.csv')
# for df in pd.read_csv('modified.csv', chunksize=5):  # 5 rows are being passed in at a time
#     print("CHUNKSIZE")
#     print(df)

new_df = pd.DataFrame(columns=df.columns) # create a new dataframe with the same columns
for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results])

print(new_df)