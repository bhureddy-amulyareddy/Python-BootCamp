#Take a space separated input from an user and print alternate elements
my_list=list(map(int,input().split()))
for i in range(0,len(my_list),2):
    print(my_list[i])
    
 