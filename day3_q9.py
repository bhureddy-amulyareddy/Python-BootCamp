#Q9.find the element that is present k+n index k is given by user 
# k=3
# n=2
 #6 8 4 61 2
# Expected output is 2

# k=3
# n=4
# 80 70 54 36 72

k = int(input())
n = int(input())
t=k+n
my_list=list(map(int,input().split()))
if(len(my_list) < (k+n)):
    print("error")
else:
     for i in range(len(my_list)):
        print(my_list[t])
        break

# print the element in the particular k index 
# k=3 
# 3 6 8 4 61 2 
# op:4 

# k=8
# 80 70 54 36 72
# op:36
# op format=12 34 45 677
# 5
# 34 


my_list=list(map(int,input().split()))
k = int(input())
idx = k%len(my_list)
print(my_list[idx])


# 10 find the maximum element in the given list

my_list=list(map(int,input().split(" ")))
max=0
for i in range(len(my_list)):
    if(max<my_list[i]):
        max=my_list[i]
print("the maximum element in the list is:",max)

 # 10 find the minimum element in the given list

my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(len(my_list)):
    if(min>my_list[i]):
        min=my_list[i]
print("the mainimum element in the list is:",min)

# replace the elements in the array with the average of maximum and minimum element 
# 0
# 13 2 67 20 68
# 68+2=70==35
# 35 35 35 35 35

my_list = list(map(float,input().split()))
max = my_list[0]
min = my_list[0]
for i in range(len(my_list)):
    if(min > my_list[i]):
        min = my_list[i]
for i in range(len(my_list)):
    if(max < my_list[i]):
        max = my_list[i]
avg=(max+min)//2
for i in range(len(my_list)):
    avg = my_list[i]
print(my_list)
    
    # find the even or odd
    # find the greatest of three
    #find the sum of all the elements in an array
    # find the peak element in the array
    # find max element in array
    # find 2nd largest element in the array
    # reverse an aarray without using any builtin functions


    

