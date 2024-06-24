'''
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

list_data = input('Nhap vao 1 chuoi so (eg: 3, 5, 7, 23): ').split(', ')
tuple_data = tuple(list_data)
print(list_data)
print(tuple_data)