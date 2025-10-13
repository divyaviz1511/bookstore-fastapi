import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Read your data from CSV file
data = pd.read_csv("data/Books.csv")

#Extract the year as we want to have that to help predict price
data['releasedYear'] = pd.to_datetime(data['releasedDate']).dt.year

#Hard coded the popularity score (1-10) which also help in predicting the price
author_score_map = {
    "JK Rowling" : 10,
    "Dan Brown" : 8,
    "Stephenie Meyer" : 7
}
data['author_score'] = data['author'].map(author_score_map)

data['author_score'] = data['author_score'].fillna(5)

feature_cols = ['pageCount', 'releasedYear', 'author_score']

#Choose your data
X = data[feature_cols]
y = data['price']

#Now split this data into training sets and test sets
[X_train, X_test, y_train, y_test] = train_test_split(X,y, test_size=0.2, random_state=42)

#Now plugged in the x and y training sets into our model
model = LinearRegression()
model.fit(X_train, y_train)

#Completely for yourself if you want to know the Coefficients/Intercept
print("Coefficient value: ", model.coef_)
print("Intercept value: ", model.intercept_)

joblib.dump(model, 'book_price_predictor_model.pkl')
