import pandas as pd
df = pd.read_csv('diamonds.csv')
price_stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print("Count, Min, Max price for each cut:")
print(price_stats)