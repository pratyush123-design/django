#function arguments
#1. default function
# def name ( fname, mname="Nath",lname="Khatiwada"):
#     print("Hello,", fname,mname,lname)
# name("Bhola")
# def name (fname,mname,lname):
#     print("Hello ,", fname,mname,lname)
# name(fname=input(),mname=input(),lname=input())

#keyword argument
# def name(a,b):
#     print("Hello", a+b)
# name(a="Ram ",b="Hari")

# #required argument
# def name(fname,mname,lname="Don"):
#     print("Hello, ", fname, mname, lname)
# name("Pratyush", "Khatiwada")

#keyword arguments
#**args
# def greet(*names):
#     for name in names:
#         print(f"Hello, {name}!")
# greet("Ram","Hari","Pratyush") 
# def greet(*Numbers):
#     for number in Numbers:
#         print(f"Number is: {number}")
# greet(3,2,4)

def greet(*names):
    for item in names:
        print (item)
   
har=["Pratyush","Hari"]
greet(*har)