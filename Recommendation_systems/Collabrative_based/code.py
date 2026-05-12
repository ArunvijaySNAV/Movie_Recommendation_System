# load libraries

import pandas as pd

ratings = pd.read_csv('ratings.csv')

ratings = ratings[['userId', 'movieId', 'rating']]

!pip install scikit-surprise

trainset = dataset.build_full_trainset()

# Model definition

from surprise import SVD

svd = SVD()

svd.fit(trainset)
svd.predict(1, 1061)

actual_data = pd.read_csv('ratings.csv')

from surprise import model_selection

cross_validation = model_selection.cross_validate(svd, data=dataset, measures=['rmse'])

cross_validation
