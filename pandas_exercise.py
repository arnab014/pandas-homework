#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}')


# Creating a dataframe from a data file
insurance = pd.read_csv('insurance.csv', sep=',', header=0)
pretty_print("Printing an entire dataframe", insurance.to_string())
pretty_print("Show all column names for a dataframe", insurance.columns)
pretty_print("Show index", insurance.index)
pretty_print("Dataframe Datatype", insurance.dtypes)
pretty_print("Dataframe Shape", insurance.shape)
pretty_print("Dataframe Info", insurance.info())
pretty_print("Dataframe Info", insurance.describe())

pretty_print("Selecting only the column Age", insurance['age'])
pretty_print("Selecting multiple columns: the Age, Children and Charges columns", insurance[['age', 'children', 'charges']])
pretty_print("Selecting First 5 rows of multiple columns: the Age, Children and Charges columns",
             insurance[['age', 'children', 'charges']].head(5))
pretty_print("Selecting Average of column Charges ", insurance['charges'].mean())
pretty_print("Selecting Minimum of column Charges ", insurance['charges'].min())
pretty_print("Selecting Maximum of column Charges ", insurance['charges'].max())
pretty_print("Selecting multiple columns:", insurance[insurance['charges'] > 10797.3362])
pretty_print("Selecting Specific Columns:",
             insurance[['age', 'sex', 'smoker']][insurance['charges'] == 10797.3362])

mx_chg = insurance['charges'].max()
pretty_print("Selecting Specific Columns:",
             insurance['age'][insurance['charges'] == mx_chg])
