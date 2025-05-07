a=input("Enter your name:")
print("My name is",a)
 
x=input("Enter first number:")
y=input("Emter Second Number:")
print(x+y)      # String will print here becuase the entered is a string data type 
# insteacd
print(int(x)+int(y))    # this is typecasting
# print(x-y) 
# print(x*y) 
# print(x/y) 
# print(x%y) 
# print(x**y) 
# print(x//y) 
print(int(x)-int(y)) 
print(int(x)*int(y)) 
print(int(x)/int(y)) 
print(int(x)%int(y)) 
print(int(x)**int(y)) 
print(int(x)//int(y)) 

#Strings in python
name="Pratyush Khatiwada"
age="20"
print("hello,my name is " +name + " and i M " +age + " Years old")
#Looping through string 
#list ma characcter print  hunxA
grade='''football, Basketball, volleyball'''
hobby="Football"
print("Let us use loop \n")  
for character in grade:
  print(character) 
# printing of only one character
name = "Pratyush"  
print(name[0])

