# Popularity_Based_Movies_Recommendation
# Setup and data loading

# Import core library for data manipulation
import pandas as pd

# Load ratings, movies, and credits data from CSV files in the project root
df_rating_csv = pd.read_csv('ratings.csv')
df_movies_csv = pd.read_csv('movies.csv')
df_credits_csv = pd.read_csv('credits.csv')

# Preview a few rows from the ratings data
df_rating_csv.head()

# Preview a few rows from the credits data
df_credits_csv.head()

'''Compute weighted rating parameters (m and C)

Calculate a weighted rating
Formula:-    wr = (v / (v+m))* R + (m / (v+m))*C
            v - number of votes for a movie
            m - minimum number of votes required
            R - average rating of the movie
            C - average rating cross all movies

'''

v = df_movies_csv['vote_count']
print(v)

# theroshold value for vote count

m = df_movies_csv['vote_count'].quantile(0.9)
print(m)

C = df_movies_csv['vote_average'].mean()
print(C)

# Formula:-    wr = (v / (v+m))* R + (m / (v+m))*C

def weighted_rating(df, m=m, C=C):
    v = df_movies_csv['vote_count']
    R = df_movies_csv['vote_average']

    wr = (v / (v+m))* R + (m / (v+m))*C
    return wr

wr_series = weighted_rating(df_movies_csv)

df_movies_csv['weighted_rating'] = wr_series
df_movies_csv.head()

df_filtered_movies_csv = df_movies_csv.loc[df_movies_csv['vote_count'] >= m].copy()

df_filtered_movies_csv.shape

df_movies_csv.shape

top_movies = df_filtered_movies_csv.sort_values('weighted_rating', ascending=0)['title'].head(10)

top_movies.squeeze().to_dict()
