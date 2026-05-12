import pandas as pd

movies = pd.read_csv('movies_small.csv', sep=';')

movies.head(6)
print(movies.shape)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
movies['overview'] = movies['overview'].fillna("")

tfidf_matrix = tfidf.fit_transform(movies['overview'])

feature_names = tfidf.get_feature_names_out()

tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# Display the head to verify
tfidf_df.head()

from sklearn.metrics.pairwise import linear_kernel

Matx_similar

movies_idx = movies.loc[movies['title'] == 'Kung Fu Panda 3']['original_title'].index[0]
movies_idx

scores = list(enumerate(Matx_similar[movies_idx]))
scores

sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
sorted_scores

movies_rt = [tlp[0] for tlp in sorted_scores[1:4]]
movies_rt

movie_title = list(movies['title'].iloc[movies_rt])
movie_title

def movie_recommendation(movie_name, nr_of_movie):
    movies_idx = movies.loc[movies['title'] == movie_name]['original_title'].index[0]
    scores = list(enumerate(Matx_similar[movies_idx]))
    movies_rt = [tlp[0] for tlp in sorted_scores[1:nr_of_movie+1]]
    movie_title = list(movies['title'].iloc[movies_rt])
    return movie_title

movie_recommendation('Cars 2', 2)
