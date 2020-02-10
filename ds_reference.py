print('simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
#mylist is just another name pointing to the same  object
mylist = shoplist

#i purchased the first item, so i remove it from the list
del shoplist[0]

print('shop list is', shoplist)
print('mylist is', mylist)

print('copy by making a full slice')
mylist = shoplist[:]
#remove first item
del mylist[0]

print('shoplist is',shoplist)
print('mylist is', mylist)
