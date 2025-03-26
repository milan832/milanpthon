#function
#defining function
def greet():
    print("hii my name is milan varu")
    print("welcome to nivzen")


greet()    

#argument
def greet(First_name, Last_name):
    print(f"hii{First_name}{Last_name}")
    print("welcome to nivzen")

greet("milan","varu")

#Keyword Argument
def person_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

person_details(name="Milan", age=21, city="porbandar")

#Default Argument
def greet(name="Milan"):
    print(f"welcome, {name}!")

greet()         # Default value "Milan" 
greet("jay")   # Custom value "jay" 

#xargs
def multiply(*numbers):
    print(numbers)

multiply(1,2,3,4,5)    


