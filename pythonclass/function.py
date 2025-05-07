# def factorial(n): #recursive function
#  if n==1 or n==0 :
#     return 1
#  return n*factorial(n-1)
# print(factorial(5))
# #Lambda function
# square=lambda x: x*x  
# print(square(4))

def greet(name):
  return  "Hello, {name}!"  #Keep the value of string in curly bracket
print(greet("Bibek"))

# n= lambda x :"Positive" if x>0 else"Negative" if x<0 else"Zero"
# print(n(5))
# print(n(-3))
# print(n(0))

# calc=lambda x,y:(x+y,x*y)
# res=calc(3,4)
# print(res)

# n=[1,2,3,4,5,6]
# even=filter(lambda x: x%2==0,n)
# print(list(even))

# a=[1,2,3,4]     #Mapping
# b=map(lambda x: x*2,a)
# print(list(b))
