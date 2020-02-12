import numpy as np
'''
integers = np.array([x for x in range(2,21,2)])

print(integers)
print()
print(np.full((3,5),13))
print()
print(np.arange(5))
print()
print(np.arange(5,10))
print()
print(np.arange(10,1,-1))'''


numbers = np.arange(1,6)
numbers2 = np.linspace(1.1,5.5,5)
print(numbers2)
print(numbers * numbers2)
print(numbers >=3)
print(numbers2 < numbers)
print(numbers2 == numbers)



'''
print (grades.sum())
print (grades.min())
print (grades.max())
print (grades.mean())
print (grades.std())
print (grades.var())

print(grades.mean(axis=0)) 
print(np.sqrt(numbers)) '''

numbers3 = np.arange(1,6)*10
print(numbers)
print(numbers3)
print(np.add(numbers,numbers3))
print(np.multiply(numbers,numbers3))
'''numbers4 = numbers3.reshape(2,3)
numbers5 = np.arange([2,4,6],[1,3,5])

print(np.multiply(numbers4,numbers5))
'''

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])
grades2 = np.array([[94,77,90],[100,81,82],[66,78,30],[79,98,99]])

print(grades[0][1])

#print second and fourth row of grades 
print(grades[1],grades[3])

#second and third value for each row
#grades[:] opens all rows 
#below grabs first and third items
print(grades[:,[1,2]])

#shallow copies

h_grades = np.hstack((grades,grades2))
print(h_grades)

v_grades = np.vstack((grades,grades2))
print(v_grades)