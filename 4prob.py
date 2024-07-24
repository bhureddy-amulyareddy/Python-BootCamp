# peek element
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
         count=i
        # print(my_list[i],end=" ")
if(my_list[-1]>my_list[-2] and my-list{-1}>count):
    count=len(my_list)-1
print(my_list[count])

# gcd of 2 numbers
# euclidean algorithm
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
while b!=0:
    a,b=b,a%b
print("gcd of 2 number is:",a)
 
 # lcm of 2 numbers
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
lcm=0
while b!=0:
    a,b=b,a%b
lcm=(a*b)//a
print("lcm of 2 numbers is:,"a)

# prime number or not
#input=5
a=int(input("enter a number:"))
r=a**0.5
count=0
if a==1:
    print("not a prime number")
elif a==2:
    print("prime number")
for i in range(2,int(r+2)):
    if a%i==0:
        count=1
        break
    if count == 0:
        print("prime number")
    elif(count>0):
        print("prime number or not")

# write a program to print all the prime numbers in a given range
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
count=0
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            print(i)

# print a leap year in a given range
inp=int(input())
for i in range(2000,2025):
    if():
      print(i)

#leap year 
year=int(input())
if(year%400 == 0):
    print("leap year")
else:
    print("not a leap year")    
    