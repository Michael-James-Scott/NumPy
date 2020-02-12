import pandas as pd 

grades_dict ={'Wally':[87, 96, 70 ], 'Eva':[100, 87, 90], 'Sam':[94,77,90], 'Katie' :[100,81,82], 'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

#print(grades[grades>=90])

#print test1 and test3 grades 
#iloc will return a dataframe
#print(grades.iloc[[0,2], :3])

#print tests scores >= 80  or < 90
#print(grades[(grades>= 80) | (grades < 90)])
'''
print tests scores >= 80 and < 90
'''
#print(grades[(grades>= 80) & (grades < 90)])

'''
print evas test 2 grade
at method for single value
'''
#print(grades.at['Test2','Eva'])

''' print sams test 1 score '''
#print(grades.iat[0,2])

''' change Eva's test two grade '''

#grades.at['Test2','Eva'] = 100 

#print(grades.at['Test2','Eva'])
print()
print("Describe Grades Data Frame")
print(grades.describe())
print()
print("Describe Grades Data Frame Round 2 Decimals")
pd.set_option('precision',2)
print(grades.describe())
print()
print("Transpose Columns and Rows")
grades.T
print(grades.T)
print()
print("Sort Grades Descending")
print(grades.sort_index(ascending=False))

print()
print("Sort Alphabetically by Column Name")
print(grades.sort_index(axis=1))

print()
print("Sort Test1 by Values Descending")
print(grades.sort_values(by='Test1',axis=1,ascending=False))

print()
print("Sort Test1 by Values Descending and Transpose Coluns")
print(grades.T.sort_values(by='Test1',ascending=False))

print()
print("")
print(grades.loc['Test1'].sort_values(ascending=False))