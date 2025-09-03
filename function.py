#functions
#def my_function():
 # print("Hello from a function")

#my_function()

#def add(a,b):
 #   x = a+b
  #  print(x)

#add(2,3)

#def add(a,b):
 #   x = a+b
  #  return x

#ans = add(2,3)
#print(ans)

#x = [1,2,3,4]
#x.append(5)
#print(x)

#y = [1,3,4,5]
#y.insert(1,2)
#print(y)

#y = [1,2,3,4,5]
#z = [6,7,8]
#y.extend(z)
#print(y)

a = ["cat","bat"]
a.remove("cat")
print(a)

a = ["cat","bat"]
a.pop(0)
print(a)

a = ["cat","bat"]
del a[0]
print(a)

d = {"name":"vb","lang":"python","likes":"100"}
x = d["lang"]
print(x)

d = {"name":"vb","lang":"python","likes":"100"}
x = d.get("lang")
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


d = {"name":"vb","lang":"python","likes":"100"}
z = d.values()
print(x)

a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 20
b = 5
if b > a:
  print("b is greater than a")
elif a > b:
  print("a is greater than b")

a = 20
b = 20
if b > a:
  print("b is greater than a")
elif a > b:
  print("a is greater than b")
else:
  print("a and b are equal")

  day = 4
  match day:
      case 1:
          print("Monday")
      case 2:
          print("Tuesday")
      case 3:
          print("Wednesday")
      case 4:
          print("Thursday")
      case 5:
          print("Friday")
      case 6:
          print("Saturday")
      case 7:
          print("Sunday")

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  for x in range(6):
      print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(2, 6):
  print(x)

#lambda
x = lambda a: a + 10
print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
#arrays
cars = ["Ford", "Volvo", "BMW"]
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

import math
print(math.pi)

from math import factorial
print(factorial(5))

fruits = ["apple","orange","vegetables","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats = ["chciken","fish","turkey"]
groceries = [fruits,vegetables,meats]
print(groceries)

groceries = [["apple","orange","vegetables","coconut"],
             ["celery","carrots","potatoes"],
             ["chciken","fish","turkey"]]
print(groceries[0][0])

groceries = [["apple","orange","vegetables","coconut"],
             ["celery","carrots","potatoes"],
             ["chciken","fish","turkey"]]

for collection in groceries:
    print(collection)

    num_pad = ((1,2,3),
               (4,5,6),
               (7,8,9),
               ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()


class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

