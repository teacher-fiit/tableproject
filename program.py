import openpyxl
import pandas as pd


def get_table(filename, column_name):
    result = pd.read_csv(filename, delimiter=',')
    res = result[['login', 'Score']]
    sort_res = res.sort_values(by='user_name')
    sort_res.rename(columns={'Score': column_name}, inplace=True)
    return sort_res


def merge_table(table1, table2):
    res = pd.merge(table1, table2, on='login', how='outer')
    res = res.fillna(0)
    s = res.columns[1:]
    res[s] = res[s].astype('int')
    return res


s1 = get_table('standings-38838.csv', 'Score1')
print(s1)
s2 = get_table('standings-38839.csv', 'Score2')
s3 = get_table('standings-38840.csv', 'Score3')
s4 = get_table('standings-38841.csv', 'Score4')
s5 = get_table('standings-38842.csv', 'Score5')
s6 = get_table('standings-38843.csv', 'Score6')


res = merge_table(s1, s2)
res = merge_table(res, s3)
res = merge_table(res, s4)
res = merge_table(res, s5)
res = merge_table(res, s6)

res['result'] = res['Score1'] + res['Score2'] + res['Score3'] + res['Score4'] + res['Score5'] + res['Score6']

print(res)

sort_res = res.sort_values(by='result', ascending=False)
print(sort_res)

sort_res.to_excel('result.xlsx')