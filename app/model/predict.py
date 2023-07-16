from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd
import numpy as np
import pickle

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

def construct_instance(LUT,course,term,year):
    X_new = pd.DataFrame({
        'Course': [course],
        'TF_IDF': [np.nan],
        'Term': [term],	
        'Term Yr': [year],	
        'Class Yr': [np.nan],	
        'Dept Desc': [np.nan],
        'Cap': [np.nan],		
        'Enrolled Ratio': [np.nan]
    })
    print(course,term)
    X_filled = fill_missing(X_new, LUT)

    return X_filled


def perform_algorithm(course,term,year):
    model, LUT = load()
    X = construct_instance(LUT,course,term,year)
    prediction = round(model.predict(X)[0], 0)
    
    return prediction