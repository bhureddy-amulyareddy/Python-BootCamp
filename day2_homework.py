#write a program to find area of a triangle
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))    
s = (a + b + c) / 2  
area = (s*(s-a)(s-b)(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)

#write a program to find perimeter of a circle
print("Enter Radius of Circle: ")
r = float(input())
π = 3.14    
c = 2 * π * r
print("\nCircumference = ", c)


#write a program to find the perimeter of triangle
print("Enter the Length of First Side: ")
a = int(input())
print("Enter the Length of Second Side: ")
b = int(input())
print("Enter the Length of Third Side: ")
c = int(input())

p = a+b+c
print("\nPerimeter = ", p)

#Write a program to  find area of a circle
π = 3.14  
Radius = float (input ("Please enter the radius of the given circle: "))  
area_of_the_circle = π * Radius * Radius  
print (" The area of the given circle is: ", area_of_the_circle)

#write a program to find the prime number using the sqrt method
n= int(input())
flag = 0
if (n>1):
  for k in range(2,int.sqrt(n)+1):
    if(n%k) == 0:
       flag == 1
    break 
if (flag == 0):
  print(n," is a prime number ")
else:
  print(n," is not a prime number")

  