# Q1:password verifier
# mr x is trying to create a new password for his instagram account these are the new conditions for
# creating the new password.
# condition 1:minimum length is 8 maximum length is 15
# condition 2:only @,/ allowed in password
# condition 3:no spaces are allowed 
# condition 4:only alpha numerics are allowed
# you are supposed to print weak if length is exact 8
# length is between 8 to 12
# length is between 12 to 15

    
# peak element 
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]<my_list[i+1]:
        count=i
print(my_list[count])
        
# print all peak elements #optimising code
my_list=list(map(int,input().split()))
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
         print(my_list[i],end=" ")

# swapping the two numbers without any third variable
a=int(input())
b=int(input())

print

#sort elements 1st half in ascending order and next half in decending order
my_list=list(map(int,input().split()))
length=len(my_list)
