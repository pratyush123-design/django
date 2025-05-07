#Strings method in Python 
# Strings are immumatable
a=("Pratyush@!!!!!! Pratyush ")
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("@,!"))     #rstrip
# replace
b=a.rstrip('@!') 
print(a.replace("Pratyush","don"))  #replace
print(a.split(" "))                 #split
c="WELCOME TO MY CHANNEL"           #center
print(c.center(100))

#count
x=("p p p p   p p  p p p")
print(x.count("p"))

#endswith
y=("Pratyush")
print(y.endswith("h"))

#find()
str1=("He is dan. He is a honest man")
print(str1.find("is"))