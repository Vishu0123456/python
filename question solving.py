''' 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :'''

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")


''' 2. Write a Python program to get the Python version you are using'''
'''solution:'''  
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

''' 3.  Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
solution:'''
r=1.1
print(3.14159*r**2)


''' 4. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them'''

fname = input("Input your First Name : ")
lname = input("Input your Last Name :")
print( lname +" "+ fname) 


''' 5. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23'''
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

my_list = ['3','5','7','23']
print(my_list)

t = ('3','5','7','23')
print(t) 

''' 6. Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java
Output : java'''

a = input("abc.java: ")
f_extns = a.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


''' 7. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]'''

color_list = ["Red","Green","White","Black"]
print("%s %s"%(color_list[0],(color_list[-1]))) 


''' 8. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''

exam_st_date = (11,12,2014)
print("The examination will start from : %i / %i / %i "%exam_st_date

''' 9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5
Expected Result : 615'''


a = int(input(": "))
n = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3= int( "%s%s%s" % (a,a,a) )
print (n+n2+n3)


