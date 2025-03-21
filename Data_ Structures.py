#list
letters = ["a","b","c","d"]
matrix = [[1,2,3],["e","f"]]
zeros = [0]*5
print(zeros)
print(zeros + letters + matrix)

#list of range
print(list(range(10)))
char = list("paython programing")
print(char[::-1])#reverse list
print(len(char))

#accessing elements
letters = ["a","b","c","d"]
print(letters[0:3:2])
numbers = list(range(20))
print(numbers[::2])

#list unpecking
numbers = [1,2,3,4,5,6,8]
first ,second , *other = numbers
print(second,other)

#looping over list
laters = [1,2,3,4,5]
for later in enumerate(laters):
    print(later)

#adding and removing item
letters = ["a","b","c","d"]
abc = ["z","y","g"]
letters.append("z")
letters.extend(abc)
letters.insert(2,"t")
print(letters)
print(letters.pop(2))
letters.remove("a")
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters)

#findig item
letters = ["a","b","c","d","e","e","e"]
print(letters.count("e"))
if "e" in letters:
    print(letters.index("e"))

#sorting list
a = [1,2,3,4,5,6]
a.sort()
print(a)
a.sort(reverse = True)
print(a)

# lambda function
b = lambda a:(1+a)
print(b(10))
x = lambda a, b, c : a + b + c
print(x(2, 3, 4))

# map function
mark = [("maths",70),("hindi",75),("gujrati",80)]
# prices = []
# for item in items:
#     prices.append(item[1])

x = list(map(lambda item: item[1],mark))
# for mark in x:
#     print(mark)
print(x)

fruits = ('apple', 'banana', 'cherry')
x = list(map(lambda fruit: len(fruit),fruits))
print(x)

# filter function
ages = [5, 12, 17, 18, 24, 32]

#def myFunc(x):
  #if x < 18:
    #return False
  #else:
    #return True

adults = filter(lambda age: age<18, ages)

for age in adults:
  print(age)

  # list comprehension
ages = [(5, 12), (17, 18), (24, 32)]
#[expression for variable in perameter]
x = [age[1] for age in ages]
print(x)


# zip function
list1 = [1,2,3,4]
list2 = [10,20,30,40]
a = list(zip("abcd",list1,list2))
print(a)

#stack
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)  # Output: [1, 2, 3]

print("Popped:", stack.pop())  # Output: 3
print("Stack after pop:", stack)  # Output: [1, 2]

print("Top element:", stack[-1])  # Output: 2

if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

# queues
from collections import deque
queue = deque([])
queue.extend([1,2,3,4,5])
for i in range(5):
    queue.popleft()
print(queue)
if not queue:
    print("queue is empty")

# swapping variables
a= 10
b = 20
# b = a
# a = b
a,b = b,a
print(a,b)

# Sets
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print(len(thisset))
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

 #Unpecking operator
a = list(range(10))
d = [a,*"milan"]
print(d)



