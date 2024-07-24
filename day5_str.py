#strings
# string methods are
# alpha
# is digit
# is alpha numeric
# is lower
# is upper
# converting into lower and upper case
# titlecase
# swap case

str="     helaaaaaalo woRld      "
print(str.lower())
print(str.upper())
print(str.title())
print(str.capitalize())
print(str.swapcase())
print(str.strip())
print(str.replace('a','z'))
print(str.split())
print(str.split('a'))


inp="helloworld123"
print(inp.isalpha())
print(inp.isnumeric())
print(inp.isalnum())
print(inp.islower())
print(inp.isupper())
print(inp.istitle())
print(inp.isdigit())

# ascii values addition
print(ord('a')+3)

# using ascii values
print(chr(90))

# print all the ascii values 
for i in range(0,128):
    print (chr(i),end=" ")