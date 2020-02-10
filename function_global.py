x = 5

def func():
    global x
    
    print('x is',x)
    x=2
    print('x in lcoal is',x)

func()
print('x is still',x)
