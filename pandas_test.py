import pandas as pd
df=pd.read_csv('./spotify_history.csv')

print(df.head(10))
print(df.tail(10))
print(df.size)
print(df.shape)
print(df.columns)
