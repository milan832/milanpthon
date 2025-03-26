#comparision operator
a = 15
b = 20
print(a < b)  
print(a >= b)  

print(a == 15) 
print(a != b) 

#conditional statement
temp = int(input("temp value : "))
if temp > 30 :
    print("its heat")

elif temp < 30:
    print("its cool")

  #logical operator
age = 20
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

#chaining comparision operator
patientAge = int(input("enter petient age:"))
if 18<= patientAge<60:
    print("eligible for vacccination")
else:
    print("not eligible for vaccination")

#check if odd or even
num = int(input("Enter a number: "))

if num % 3 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")