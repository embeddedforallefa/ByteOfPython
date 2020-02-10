# This is a string object
name = 'Veeresh'

if name.startswith('Vee'):
    print('Yes, the string starts with "Vee"')

if 'a' in name:
    print('yes, it contains the string "a"')

if name.find('res') != -1:
    print('yes, it contains the string "res"')

delimiter = '_*_'

mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))