import pandas as pd

reviews = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/winemag-data-130k-v2.csv")

# print(reviews.head())
# print('\n\n')
# print(reviews.sort_values(by='country').head(5))
# print(reviews.sort_index().head())


# --------------------------------------------------------------------------------------------------------------
# 1. What is the data type of the points column in the dataset?
dtype = reviews.points.dtype
print(dtype)

# --------------------------------------------------------------------------------------------------------------
# 2. Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in
# native Python.
point_strings = reviews.points.astype('str')
print(point_strings)

# --------------------------------------------------------------------------------------------------------------
# 3. Sometimes the price column is null. How many reviews in the dataset are missing a price?
n_missing_prices = pd.isnull(reviews.price).sum()

# --------------------------------------------------------------------------------------------------------------
# 4. What are the most common wine-producing regions? Create a Series counting the number of times each value occurs
# in the region_1 field. This field is often missing data, so replace missing values with Unknown. Sort in descending
# order. Your output should look something like this:
after_addingUnknown = reviews.region_1.fillna('Unknown')
counts = after_addingUnknown.value_counts()
sorting = counts.sort_values(ascending=False)
reviews_per_region = sorting
print(reviews_per_region)

