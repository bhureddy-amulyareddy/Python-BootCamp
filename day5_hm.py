#homework
#print upper triangular matrix
arr = [[4, 5, 6],
       [1, 2, 3],
       [2, 6, 7]]

print("The original matrix: ")
for row in arr:
   print(row)
print()

print("The upper triangular matrix: ")
for i in range(3):
   for j in range(3):
      if(i > j):
         print(end="  ")
      else:
         print(arr[i][j],end=" ")
   print(" ")

   #print lower triangular matrix
arr = [[4, 5, 6],
       [1, 2, 3],
       [2, 6, 7]]

print("The original matrix: ")
for row in arr:
   print(row)
print()

print("The lower triangular matrix: ")
for i in range(3):
   for j in range(3):
      if(i < j):
         print(end="  ")
      else:
         print(arr[i][j],end=" ")
   print(" ")

#upper triangle pattern
for i in range(5):
    for j in range(5):
        if(i==j or i>j) :
            print("*",end="")
    print()        

# lower triangle pattern
for i in range(5):
    for j in range(5):
        if(i==j or i<j) :
            print("*",end="")
    print() 
    
   #Print rhombus pattern
rows = 4
for i in range (1,rows + 1):
    for j in range (1,rows - i + 1):
        print (end=" ")
    for j in range (1,rows + 1):
       print ("*",end=" ")
    print()
    
#or 

num = int(input("Enter the number:"))

for i in range(0, num):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()
    
#or    
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

    #printing parallelogram pattern
rows = int(input("Enter rows:"))
cols = int(input("Enter Cols:"))

for i in range(0, rows):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, cols):
        print("*", end="")
    print()

#print number pyramid
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')