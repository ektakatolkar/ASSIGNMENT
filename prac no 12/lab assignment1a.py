import pandas as pd

df = pd.read_csv('diamonds.csv')

mean_price = df.groupby('cut')['price'].mean()
print("Mean price for each cut:")
print(mean_price)