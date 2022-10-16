a = [10,20]

b = [10,20]

c = a
print(a is c) # it will return true because a is same object as c
print(b is c) # it will return false althrough they have same value but not printing the same memory location
print(a==b) # it will return true because a is equal to b


# is not operator return true if both variable are not same object

print(a is not c) # it will return false because a and b is same object 
print(b is not c) # it will return true because b and c is not same object
print(a != b) # it will return false because a is equal to b



# Membership operators

# These operators are used to test if a sequence is present or not in object

a = [10,20,30,40]
print(20 in a)
print(20 not in a)

# in => it will return true if sequence is present in an object
# not in => it will retun true if sequence is not present in an object


# BITWISE OPERATORS
# They are used for compare binary number 

# & ->AND -> if both bits are 1 , it sets each bit to 1 ,otherwise 0
# | -> OR -> if one of the two bits is 1 ,it set each bit to 1 , othewise 0
# ^ -> XOR -> if only one of the two bits is 1, it ser each bit to 1
# ~ -> NOT =>  complement operators , it returns one's complement of the number 
# << => Zero fill left shift => the binary number appended with 0's at the  end 
# >> => Zero fill right shift => in simple term , the right side of bits are removed 



x = 20
y = 7

print (x/y)

