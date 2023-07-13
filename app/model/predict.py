from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd
import numpy as np
import pickle
import os

directory = os.listdir('.')
print(directory)

def load():
    with open('./app/model/best_regressor.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('./app/model/lut.pkl', 'rb') as f:
        lut = pickle.load(f)
    
    return model, lut

def imputed_value(rows, column):
    values = np.append(rows[column].values, [np.nan]).reshape(-1, 1)
    imputer = IterativeImputer(max_iter=10, random_state=42)
    return imputer.fit_transform(values)[-1][0]

def fill_missing(X, LUT):
    course = X['Course'].values[0]
    term = X['Term'].values[0]

    rows = LUT[(LUT['Course'] == course) & (LUT['Term'] == term)]

    X['TF_IDF'] = imputed_value(rows, 'TF_IDF')
    X['Cap'] = round(imputed_value(rows, 'Cap'), 0)
    X['Enrolled Ratio'] = imputed_value(rows, 'Enrolled Ratio')

    X['Dept Desc'] = rows['Dept Desc'].values[0]
    X['Class Yr'] = rows['Class Yr'].values[0]

    return X

def construct_instance(LUT):
    X_new = pd.DataFrame({
        'Course': ['CSC 225'],
        'TF_IDF': [np.nan],
        'Term': ['Summer'],	
        'Term Yr': [2024],	
        'Class Yr': [np.nan],	
        'Dept Desc': [np.nan],
        'Cap': [np.nan],		
        'Enrolled Ratio': [np.nan]
    })

    X_filled = fill_missing(X_new, LUT)

    return X_filled


def perform_algorithm():
    model, LUT = load()
    X = construct_instance(LUT)
    prediction = round(model.predict(X)[0], 0)

    print(f"For {X['Course'].values[0]} in {X['Term'].values[0]} {X['Term Yr'].values[0]}:\nWe predict {prediction} students will enroll 🎉")
    
    return prediction

perform_algorithm()