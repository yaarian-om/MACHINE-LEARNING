import pandas as pd

reviews = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/winemag-data-130k-v2.csv")

# print(reviews.head())
# print('\n\n')
# print(reviews.sort_values(by='country').head(5))
# print(reviews.sort_index().head())

'''
# --------------------------------------------------------------------------------------------------------------
# 1. region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews
# with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
print(renamed)

# --------------------------------------------------------------------------------------------------------------
# 2. Set the index name in the dataset to wines.
reindexed = reviews.rename_axis('wines', axis='rows')
print(reindexed)

# --------------------------------------------------------------------------------------------------------------
# The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") on
# reddit.com. Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and another
# dataframe for products mentioned on the r//movies subreddit.
gaming_products = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/movies.csv")
movie_products['subreddit'] = "r/movies"
# 3. Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products, movie_products])
print(combined_products)
'''
# --------------------------------------------------------------------------------------------------------------
# 4. The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets and a separate one
# for powerlifting competitors. Run the cell below to load these datasets into dataframes:
powerlifting_meets = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/meets.csv")
powerlifting_competitors = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/openpowerlifting.csv")
# Both tables include references to a MeetID, a unique key for each meet (competition) included in the database.
# Using this, generate a dataset combining the two tables into one.
powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index('MeetID'))
print(powerlifting_combined)