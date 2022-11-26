print('This is  string {}'.format('INSERTED'))
print('the {} {} {}'.format('fox','brown','colour'))
print('the {0} {1} {2}'.format('fox','brown','colour'))
print('the {b} {q} {f}'.format(f='fox',b='brown',q= 'quick'))



#float formating


## float formating follows "{value:width.precesion f}"



a = (100/77)
print(a)
print("the result was {a}".format(a=100/77))
print("the result was {a:1.3f}".format(a=100/77))

print("the result was {a:5.3f}".format(a=100/77))

print("the value was {a:10.3f}".format(a=100/77))


# it means if i increase width then the result is separated by some distance from "the result was " just like show if we print..


print("the value was {a:1.5f}".format(a=100/77))

name = "vishwajeet"
print('Hello, his name is {}'.format(name))

print(f'Hello , his name is {name}')

name = "vishwajeet"
Age = 18
print(f'{name} is {Age} years old')

name = "jonny"
Age = 25
print(f'{name} is {Age} years old')

a = "rules! "
print('python {}'.format(a))

print('python {}' .format('rules!'))
print('I like {}'.format('apples'))






##### Basic Formatting ##########################

x = '%s %s' % ('three' ,'four')
print(x)

y = '{}' '{}'.format ('three' , 'four')
print(y)

a = '%s %s' % ('3' , '4')
print(a)

b = '{}' '{}'.format('3' ,'4')
print(b)



################ Value conversion ########################

