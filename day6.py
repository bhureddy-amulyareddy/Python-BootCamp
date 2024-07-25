#oops concept
#defining class and objects
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
    
obj1=Myclass
obj2=Myclass
print(obj1.add(45,89))
print(obj1.sub(45,99))
print(obj1.mul(45,89))
print(obj1.div(48,9))
print(obj1.mod(45,89))
print(obj2.add(499,89))
print(obj2.sub(499,99))
print(obj2.mul(40,890))
print(obj2.div(56,8))
print(obj2.mod(12,4))

# arrays

class animal:
   def speak():
    return "animal is speasking"
#single inheritance
class dog(animal):
    def bark():
        return "bow---"
# multilevel inheritance
class puppy(dog):
   def puppy_speak():
      return "in puppy"
obj1=animal
obj2=dog
obj3=puppy
print(obj1.speak())
print(obj2.bark())
print(obj3.puppy_speak())


#Multiple
class Father:
    def Father_speak():
        return "Father class"
class Mother:
    def Mother_speak():
        return"Mother Speak"
class kid(Father,Mother):
    def kid_speak():
        return "Im kid.I m having properties of Mother Class and Father Class"
obj1=kid
print(obj1.Father_speak()) 
print(obj1.Mother_speak())
print(obj1.kid_speak())
   
 #method_over_riding
class Animal:
    def Speak():
        return "Speaking...."
class Dog(Animal):
    def Speak():
        return"Dog is speaking...." 
class puppy(Dog):
    def Speak():
        return"Puppy is speaking..."
obj3=puppy
print(obj3.Speak())

def run():
    return"Running...."           
def run():
    return "Hello"
print(run())

# polymorphism


class cal:
    def add(self,args):
        return sum(args)
    
    class cal:
        def add(a,b,c):
            return a+b+c 
        def add(a,b,c,d):
            return a+b+c+d
        def add(a,b,c,d,e):
            return a+b+c+d+e
        def add(self,args):
            sum=0
            for i in args:
                sum+=ireturn sum



obji=cal
print(obj2.self)
print(obj1.add(1,2,3))               
print(obj1.add(1,2,3))               
print(obj1.add(1,2,3))               
               

class cal:
 def add(self,*args):
  sum=0
  for i in args:
     sum+=i
   return sum(args)
                    

#take input
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))