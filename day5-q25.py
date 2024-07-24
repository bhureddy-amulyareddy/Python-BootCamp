# check how many vowels are in a string
str=input()
vowels="aeiouAEIOU"
count=0
for char in str:
    if char in vowels:
      count+=1
print("the number of vowels:",count)
 
# write a program to print all the count of consonents
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
   if(i in vowel):
      count+=1
for i in inp:
  if(i in consonent): 
     print("number of consonent:",count)  

#or
str=input()
consonents="bcdfghjklmnpqrstvwxyz"
count=0
for char in str:
   if char in consonents:
      count+=1
print("the number of consonets",count) 


# print all the vowels followed by consonents
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
   if(i in vowel):
    ans+=i
for i in inp:
  if(i in consonent): 
     ans+=i
print(ans)

# print the non repeating/unique character in the string
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
  if(i not in ans):
    ans+=i
print(ans)

# to print sum of digits in a string
 
a=input()
sum=0
for i in a:
    if(ord(i)) >=48 and (ord(i)) <=57:
        sum = sum+int(i)
print("the sum is:" + str(sum))

#or

vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello 1234world"
inp=i.lower()
for i in inp:
  if(i in check):
    ans+=int(i)
print(ans)

# reverse the numbers present in a given string
#Homework

# sum of ascii values
a=input()
sum=0
for i in a:
    if(ord(i)) >=48 and (ord(i)) <=57:
        sum = sum+int(i)
print("the sum is:" + str(sum))

# to print all the capital letter in a given string
inp=input()
ans=""
for i in inp:
    if(ord(i)) >=65 and (ord(i)) <=90:
        ans+=1
print(input)

# remove all the brackets from the given algebraic expression
inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
      pass
    else:
       print(i,end="")
print()

#encode and decoding
# abc=4
# efgh #homwork
inp=input()
for i in inp:
    print(chr(ord(i)))




str=int(input())
inp=int(input())
inpp=str.upper()
empty=""
for i in inp:
    empty+=chr(ord(i)+n)
print(empty)

# hello-----wor-----ld
# -----hello world'
inp=int(input())
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+1
print("-"*count+ans)
 
# patterns
# square pattern
n=int(input("enter number of rows"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()


for i in range(10):
    for j in range(10):
        if(i==j):
            print(" ",end="")
        else:
            print("*",end="")
            print()


# print upper triangular matrix
# print lower triangular matrix
# print pararellogram
# ***
#  ***
#   ***
# print rhombus
# print number pyramid












