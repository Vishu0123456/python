# solution of 1st solution

'''i = 1
while(i<=10):
    print(i)
    i+=1'''

# solution of 2nd question

'''''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
  '''

# solution of 3rd question
'''for i in range(1,5):
for j in range (1,i+1):
    print(j,end=" ")
print()'''

'''a = int(input("Enter number "))
b = 1
c = 0
while (b<=10):
    c = b+c
    b = b+1
    print("sum is: ",c)     '''

# solution of 4th question

'''a = int(input())
b = 1
while b<=10:
    print(a*b)
    b=b+1'''

# solution of 5th question 

'''numbers = [12,75,150,180,145,525,500]
for i in numbers:
    if i>150:
        continue
    if i % 5 == 0:
        print(i)'''

# solution of 6th question

'''num = (input())
b = 0
for i in num:
    b=b+1
    print(b)'''


# solution of 7th question 

for i in reversed (range(1,6)):
    for j in reversed  (range(1,i+1)):
      print(j,end=" ")

    print()  


# solution of 8th question

list1=[10,20,30,40,50]

for i in reversed (range(0,len(list1))):
 print(list1[i])


# solution of 9th question 

list1=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

for i in(range(0,len(list1))):
    print(list1[i])

# solution of 10 th solution

for i in range(5):
    print(i)
else:
    print("Done!")

# solution of 11th question

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)

# solution of 12th question

num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    
    num1 = num2
    num2 = res


# solution of 13th question

num= 5
factorial=1
if num < 0:
    print("Factorial does not for negative number")
elif num ==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
        print("the factorial of",num,"is",factorial)

# solution of 14th question
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)


# solution of 15th question
my_list =[10,20,30,40,50,60,70,80,90,100]
for i in my_list[1::2]:
    print(i,end="")


# solution of 16th question

input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))

# solution of 17th question

n = 5

start = 2
sum_seq = 0

for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)


# solution of 18th question 

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")











