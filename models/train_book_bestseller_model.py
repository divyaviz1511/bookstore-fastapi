import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from preprocessing.author_score import return_author_score

#Read your data from CSV file
data = pd.read_csv("../data/Books.csv")

#Extract the year as we want to have that to help predict price
data['releasedYear'] = pd.to_datetime(data['releasedDate']).dt.year

#Retrieving the author_score from the function. 
data['author_score'] = data['author'].map(return_author_score)
data['author_score'] = data['author_score'].fillna(5)

#Transforming categorical data - genre
encoder = OneHotEncoder(sparse_output = False)
encoded_genre = encoder.fit_transform(data[['genre']])
encoded_genre_cols =  encoder.get_feature_names_out(['genre']) 

#create dataframe of genre_encoded 
encoded_genre_df = pd.DataFrame(encoded_genre, columns=encoded_genre_cols)

# Reset indices before concatenation
data = pd.concat([data.reset_index(drop=True), encoded_genre_df.reset_index(drop=True)], axis=1)

feature_cols = ['pageCount', 'releasedYear', 'author_score'] + list(encoded_genre_cols)

#Choose your data
X = data[feature_cols]
y = data['best_seller_confidence']

#Now split this data into training sets and test sets
[X_train, X_test, y_train, y_test] = train_test_split(X,y, test_size=0.2, random_state=42)

#Now plugged in the x and y training sets into our model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(encoder, 'genre_encoder.pkl')
joblib.dump(model, 'book_bestseller_predictor_model.pkl')