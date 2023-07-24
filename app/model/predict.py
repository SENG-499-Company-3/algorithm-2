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

def get_rows(LUT, dept, term, class_yr, course=None, not_found=True):
    if not_found:
        rows = LUT[(LUT['Dept Desc'] == dept) & (LUT['Term'] == term)]
        if rows['Class Yr'].any() == class_yr:
            return rows[rows['Class Yr'] == class_yr]
        else:
            # If we can't find the exact class year, try to find the closest
            match class_yr:
                case '1':
                    query_res = rows[rows['Class Yr'] == 2]
                case '2':
                    query_res = rows[rows['Class Yr'].isin([1, 3])]
                case '3':
                    query_res = rows[rows['Class Yr'].isin([2, 4])]
                case '4':
                    query_res = rows[rows['Class Yr'] == 3]
                case _:
                    query_res = rows
            
            # If we still can't find anything, return the original rows
            if query_res.empty:
                return rows
    else: 
        return LUT[(LUT['Course'] == course) & (LUT['Term'] == term)]

def course_extract(course):
    departments = {
        'CSC': 'Computer Science',
        'ECE': 'Electrical & Computer Engg',
        'SENG': 'Engineering & Computer Science'
    }

    course_dept = departments[course.split(' ')[0]]
    course_yr = course.split(' ')[1][0]

    return course_dept, course_yr

def fill_missing(X, LUT):
    course = X['Course'].values[0]
    term = X['Term'].values[0]
    dept, class_yr = course_extract(course)

    # Check if the course is contained in the LUT
    if LUT['Course'].str.contains(course).any():
        rows = get_rows(LUT, dept, term, class_yr, course=course, not_found=False)
    else:
        # Start super specific, then get more general if we can't find anything
        rows = get_rows(LUT, dept, term, class_yr)

    X['TF_IDF'] = imputed_value(rows, 'TF_IDF')
    X['Cap'] = round(imputed_value(rows, 'Cap'), 0)
    X['Enrolled Ratio'] = imputed_value(rows, 'Enrolled Ratio')
    X['Dept Desc'] = dept
    X['Class Yr'] = class_yr

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

    X_filled = fill_missing(X_new, LUT)

    return X_filled

def perform_algorithm(course, term, year):
    model, LUT = load()
    X = construct_instance(LUT, course,term,year)
    prediction = round(model.predict(X)[0], 0)
    
    return prediction