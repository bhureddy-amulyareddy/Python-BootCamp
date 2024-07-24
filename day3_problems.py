# find the missing number in the array
list1 = list(map(float,input("enter the list:").split(",")))
n=10
total=n*(n+1)//2
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
print(total-sum)

# find the dublicates in the array

my_list = list(map(int,input().split()))
print("duplicate elements in the given array: ")
for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if(my_list[i]) == (my_list[j]):
           print(my_list[j])

           
for i in list:
    if(i not in []):
        [].appends(i) 
        print([])
#sum of digits using while loop
n=123
sum=0 
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)

#find the sum of squares of digits in a given number

n=123
sum=0 
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)

# find the sum of even values

n=1234
sum=0 
while n>0:
    r=n%10
    if(r%2==0):
        sum=sum+r
    n=n//10
print(sum)

# how to reverse a number
n=1234
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))

# questions
#find the sum of squares of given number
# find sum of squares of even and odd digits(seperate)
# check whether the number is palindrome or not
# write a program first n fibonacci series


