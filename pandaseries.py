import pandas as pd 
'''grades = pd.Series([87,100,94], index=['Wally','Eva','Sam'])'''
'''
print(grades)
print(grades.count())
print(grades.mean())
print(grades.std())
print(grades.describe())
print(grades.count())
print(pd.Series (98.6, range(3)))'''



grades = pd.Series ({'Wally':87, 'Eva':100,'Sam':94})
print(grades['Eva'])
print(grades.Wally)

hardware = pd.Series(['Hammer','Saw','Wrench'])

print(hardware.str.contains('a'))