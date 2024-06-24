'''
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
'''

name = input('Nhap vao ten cua ban: ').split(' ')
first_name = name[0]
last_name = name[-1]
print(last_name + ' ' + first_name)