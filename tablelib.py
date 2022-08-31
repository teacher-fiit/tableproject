import openpyxl
import pandas as pd


def get_table(filename, column_name):
    result = pd.read_csv(filename, delimiter=',')
    res = result[['login', 'Score']]
    sort_res = res.sort_values(by='login')
    sort_res.rename(columns={'Score': column_name}, inplace=True)
    return sort_res


def merge_table(table1, table2):
    res = pd.merge(table1, table2, on='login', how='outer')
    res = res.fillna(0)
    s = res.columns[1:]
    res[s] = res[s].astype('int')
    return res
