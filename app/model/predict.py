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
        lut.reset_index(drop=True, inplace=True)

    return model, lut


def imputed_value(rows, column):
    values = np.append(rows[column].values, [np.nan]).reshape(-1, 1)
    imputer = IterativeImputer(max_iter=10, random_state=42)

    return imputer.fit_transform(values)[-1][0]


def fill_missing(X, LUT):
    course = X['Course'].values[0]
    term = X['Term'].values[0]

    rows = LUT[(LUT['Course'] == course) & (LUT['Term'] == term)]

    # There is no combination of course and term in the lookup table
    if rows.empty:
        # The course is in the lookup table, but not the term
        if course in LUT['Course'].values:
            rows = LUT[LUT['Course'] == course]
        # The course is not in the lookup table, i.e. it is a new course
        else:
            filter1 = LUT[(LUT['Course'].str.startswith(
                course.split()[0])) & (LUT['Term'] == term)]
            filter2 = filter1[filter1['Course'].str.contains(
                course.split()[1])]
            if not filter2.empty:
                rows = filter2
            else:
                rows = filter1

    X['TF_IDF'] = imputed_value(rows, 'TF_IDF')
    X['Cap'] = round(imputed_value(rows, 'Cap'), 0)
    X['Enrolled Ratio'] = imputed_value(rows, 'Enrolled Ratio')

    X['Dept Desc'] = rows['Dept Desc'].values[0]
    X['Class Yr'] = rows['Class Yr'].values[0]

    return X


def construct_instance(LUT, course, term, year):
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

    X_filled = fill_missing(X_new, LUT)

    return X_filled


def perform_algorithm(course, term, year):
    model, LUT = load()
    X = construct_instance(LUT, course, term, year)
    prediction = round(model.predict(X)[0], 0)

    return prediction
