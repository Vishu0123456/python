my_list = [1,2,3]
print(len(my_list))
a = [1,2,3,4,5,6,]
print(len(a))

b = ['vishwajeet',100,25,36.2]
print(len(b))

c = ['one','two','three']
print(c[0])
print(c[2])
print(c[0:])

d = ['four','five','six']
print(c+d)
d[0] = 'vishwajeet'
print(d)

c[0] = 'vishwajeet'
print(c)

my_list = c+d
print(my_list)

my_list[0] = 'india is going to win this year world cup t20 2022'
print(my_list)

my_list.append('vishwajeet')
print(my_list)

# for removing Elememt from list we use listname.pop() as i doing below
my_list.pop()
print(my_list)

popped_item = my_list.pop()
print(popped_item)
print(my_list)

my_list.pop(0)
print(my_list)

# for arranging elements in order

my_list = ['apple','banana','mango','grapes']
num_list = ['0','5','9','8']

my_list.sort()
print(my_list)

my_list.sort()
my_sorted_list = my_list
print(my_sorted_list)

print(num_list)
num_list.sort()
print(num_list)

num_list.sort()
num_sorted_list = num_list
print(num_sorted_list)

# for writting element of list in reverse we use this
num_list.reverse()
print(num_list)

# dictionaries situation example

my_dict = {'key1':'Apple','key2':'mango'}
print(my_dict)

print(my_dict['key1'])
print(my_dict['key2'])

store_item = {'Pen':'5','Notebook':'100'}
print(store_item)



a = {'v1':'2563','v2':'7895'}
print(a)
print(a['v1'])

b = {'s1':'100252','s2':[0,4,9,8,6,3]}
print(b)

# tuples with python

t=(1,2,3,4)
print(type(t))
print(len(t))

t = ('Apple',5)
print(t[0])
print(t[1])

t = (1,2,3,3,5,6,1,2,3,4,5,6,5,4,7,8,9,3,2,1,7,8,9,1,2,1,2,1,5,4,4,5)
print(t.count(1))
print(t.count(2))
print(t.count(3))
print(t.count(4))
print(t.count(5))

# for finding where element is present we use this

print(t.index(4))

# sets in python

myset = set()
print(myset)

myset.add(2)
print(myset)