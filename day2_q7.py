#Your given with a  , separated natural numbers 1 to 10 print only the even numbers
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
   # print(my_list[i])
    count+=1
    print(count)
#your given with a space separated integer list find the number of even elements and number of odd elemets in given list
my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list),1):
    if(my_list[i]%2==0):
         even+=1
    else:
        odd+=1
print(even)
print(odd)
 
