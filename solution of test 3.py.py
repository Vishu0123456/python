# solution of 1st question


def demo(name, age):
    # print value
    print(name, age)

 #call function
demo("Ben", 25)


# solution of 2nd question


'''def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)'''


# solution of 3rd question:

'''def calculation(a, b):
    addition = a+b
    subtraction = a-b
    # return multiple values separated by comma
    return addition, subtraction


# get result in tuple format
res = calculation(40, 10)
print(res)'''

# solution of 4th question

'''def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")'''

# solution of 5th question

# outer function
'''def outer_func(a,b):
    square = a**b

# inner function
def addition(a,b):
 return a+b
 add = addition(a, b)
# add 5 to the result
 return add + 5

 result = outer_fun(5, 10)
 print(result)'''


 # solution of 6th question
'''
 def addition(num):
     if num:
         # call same function by reducing number by 1
         return num + addition(num - 1)
     else:
         return 0

 res = addition(10)
 print(res)'''





# solution of 7th question 

'''
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

'''


 # solution of 8th question
'''

print(list(range(4, 30, 2)))
'''
# solution of 9th question

a = [4, 6, 8, 24, 12, 2]
print(max(a))






