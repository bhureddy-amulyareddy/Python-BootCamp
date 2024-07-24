# X GOES TO MARKET HE WILL BUY 10 APPLES , 2 DOZEN BANANAS , 8 ORANGES THE COST OF EACH APPLE is 15
# AND COST OF ONE BANANA IS 4  AND COST OF ONE ORANGE IS 5  SHE GAVE 700 RUPPEES TO X IF HE IS LEFT 
# OVER WITH SOME  MONEY THE VENDOR DIDNT FOOL THE VENDOR IF HE IS TELLS TO GIVE MORE MONEY THEN THE 
# VENDOR CHEATED HIM

apples = int(input("No. of apples to buy"))
bananas = int(input("No. of bananas to buy"))
oranges = int(input("No. of oranges to buy"))
costa = 15*apples
costb = 4*bananas
costo = 5*oranges
sum = costa + costb + costo
print(sum)
if(sum > 700):
   print("The kid got cheated by the vendor")
else:
   print("The kid didnot get cheated by the vendor")  

cost_of_apple= 15
cost_of_banana= 8  
cost_of_orange= 5 
print("Enter the no. of apples")
no_of_apples=int(input())
print("Enter the no. of bananas")
no_of_bananas=int(input())
print("Enter the no. of oranges")
no_of_orange=int(input())
print("Enter the amount given by the mother")
amount_given = int(input())
sum = (no_of_apples*cost_of_apple + no_of_bananas*cost_of_banana + no_of_orange*cost_of_orange )
if (sum>700):
   print("He didnt get cheated")
else:
   print("He got cheated")

# Check whether the numbers are even positive or negative and odd negative or positive
a=int(input())
if (a%2==0) and (a>0):
   print("The number is even number and positive") 
elif(a%2==0) and (a<0):
   print("The number is even number and negative")     
elif(a%3==0) and (a>0):
   print("The number is odd number and positive") 
elif(a%3==0) and (a<0):
   print("The number is odd number and negative")   

# Mr Z is selected for olympics is participated in swimming competition only one winner is selected among 
# all the participants anyhow Mr.Z selcted whereas MR Y and MR X are friends of MR Z Mr X is participated
#  in badminton and MR Y is participated in Table tennis according to the selection committie the 
# requirements for badminton players are are height = 140 cm , weight factors of 2 and body fat is less 
# than 12% according to the selection committee criteria for table tennis are height = minimum 118 cm to 
# 148cm , weight is the factors no. of medals won by Mr.Z bodyfat 14%. according to the previous history 
# Z participated in 14 games out of which he is havind success rate of 50%  Write a program to check
#  whether MR X & MR Y &MR Z will travel in a same plane or out.Write a program to check whther this
# people will meet each other not.

X_height= int(input("Height eligiblity for table tennis"))
X_weight=int(input("Weight eligiblity for table  tennis"))
X_bodyfat=int(input("bodyfat eligibilty for table tennis"))
Y_height= int(input("Height eligiblity for badminton "))
Y_weight=int(input("Weight eligiblity for badminton "))
Y_bodyfat=int(input("bodyfat eligibilty for badminton"))
zmedals=(50/100)*14
if(X_height>=140) and (X_weight%2==0) and (X_bodyfat<12):
       if(Y_height>=118 or Y_weight%2==0) and (Y_weight%zmedals==0 and Y_bodyfat==14):
              print("x,yx,z are travelling in same plane")
       else:
          print("only x,z are travelling in same plane")
else:
   print("only z is travelling in the plane")
