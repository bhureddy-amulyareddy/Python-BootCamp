#find even or odd using while loop
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Find the greatest of three
num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

# Find the sum of all the elements in an array
my_list=list(map(int,input().split()));     
sum = 0;    
     
#Loop through the array to calculate sum of elements    
for i in range(0, len(my_list)):    
   sum = sum + my_list[i];    
     
print("Sum of all the elements of an array: " + str(sum))
 

def findPeak(L):
    results = []
    for i in range(1, len(L) - 1):
        if L[i] > L[i-1] and L[i] > L[i+1]:  # check both sides for each
            results.append(L[i])              # ^ element of list excluding edge cases
    if L[0] > L[1]: results.append(L[0])     # check edge cases
    if L[-1] > L[-2]: results.append(L[-1])
    return results
my_list = list(map(int,input().split()))
print("Peak points are: ", findPeak(my_list))

#Find the maximum element in an array 
my_list=list(map(int,input().split()))
my_list.sort()
print (my_list[-1])

#Find the second maximum element in an array
my_list=list(map(int,input().split()))
my_list.sort()
print (my_list[-2])

#Reverse an array without using built-in functions
my_list=list(map(int,input().split()))
print("The array: ", my_list)
l = len(my_list)
for i in range(l // 2):
    my_list[i], my_list[l - i - 1] = my_list[l - i - 1], my_list[i]

print("The reversed array: ", my_list)

#Find the sum of squares of a given number
total = 0 
count = 1 
n = int(input("Enter the number of squares to compute: ")) 
while count <= n: 
    total += count ** 2 
    count += 1 
print(f"The sum of the squares of the first {n} numbers is: {total}")