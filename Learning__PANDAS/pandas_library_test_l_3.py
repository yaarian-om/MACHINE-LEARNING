import pandas as pd

reviews = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/winemag-data-130k-v2.csv")


print(reviews.head())
print('\n\n')
print(reviews.sort_values(by='country').head(5))
print(reviews.sort_index().head())
