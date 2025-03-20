#for loop
for i in range(10):
    print("milan",i)   

#for else
Sucessful = False
for p in range(3):
    print("try again!")
    if Sucessful:
        print("sucessful")
        break
else:
    print("tried 3 times and failed")

    #nested loops
for x in range(7):
    for y in range(5):
        print(f"({x}*{y})")

#iterable string
for z in "nivzen":
    print(z)

for k in "milan":
    print(k)   

    
#iterate string fro list
city_name = ["rajkot","vadodara","surat","mumbai","jaipur"]
for item in city_name:
    print(item)


#while loop
n = int(input("value of n : "))
while n > 0:
    print(n)
    n//=2

#exercise
count = 0
for i in range(1,8):
    if i%2==0:
        print(i)
        count+=1
print(f"we have {count} even nummbrs")

