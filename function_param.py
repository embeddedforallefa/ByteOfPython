def print_max(a, b):
    if a>b:
        print(a, 'is max')
    elif a==b:
        print(a, 'is equal to',b)
    else:
        print(b, 'is max')

#directly pass literal values
print_max(3,4)

x=6
y=4

#pass varialbes as arguments
print_max(x,y)
