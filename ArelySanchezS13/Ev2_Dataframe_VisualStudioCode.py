import pandas as pd

dataframe = pd.read_excel('C:/Users/pedro/Downloads/ev2lista.xlsx', index_col=0,
                          engine='openpyxl')
print(dataframe.head())