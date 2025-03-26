# exception is kind of error that terminates the program execution
numbers = [1,2]
print(numbers[3])

age = int(input("age:"))

# handling exeption
try:
    age = int(input("age:"))

except ValueError:
    print("you didn't enter valid age")
print("execution continuous")

try:
    age = int(input("age:"))
    xfactor = 10/age

except ValueError:
    print("you didn't enter valid age")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print(" no exception were thrown ")

    # cleaning up
try:
    file = open("exception.py")
    age = int(input("age:"))
    xfactor = 10/age
except ValueError:
    print("you didn't enter valid age")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print(" no exception were thrown ")
finally:
    file.close()