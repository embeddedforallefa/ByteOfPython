age = 29
name = 'Veeresh'

print('{0} was {1} years old when first read byte of python book'.format(name, age))
print('{0} is playing with python now'.format(name))
print(f'using f-strings')
print(f'{name} was {age} years old when he wrote this book') # notice the 'f' before the string
print(f'Why is {name} playing with that python?') # notice the 'f' before the stringprint('{0} was {1} years old now'.format(name, age))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
#fill with _ with the text entered
#(^) tp 11 width '__hello__'
print('{0:_^11}'.format('hello'))
#keywork based 'veeresh wrote a byte of python'
print('{name} wrote {book}'.format(name='veeresh', book = 'A byte of python'))
