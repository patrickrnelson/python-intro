msg = 'Hello World'
print(msg)

boolean = True
print(boolean)

# Can't put ints and strings together
# number = 8 
# string = 'eight'
# print(number + string)

hello = 'Hello'
world = 'World'
print(hello + ' ' + world + '!') 

helloWorld = hello + ' ' + world
helloWorldScream = helloWorld.upper()
print(helloWorldScream)

nameList = ["Patrick", "Ashley", "Willow"]
print(nameList)

print(len(nameList))

for i in range(len(nameList)):
  print(nameList[i])

for x in nameList:
  print(x)

firstDictionary = {
  "make": "Jeep",
  "model": "Cherokee",
  "year": 2016
}

carYear = firstDictionary["year"]

print(firstDictionary)
print(carYear)

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

def newFunction(word):
  print('I love ' + word)

newFunction('Pizza')

c = 50
d = 55
def equalFunc():
  global c
  if d > c:  
    c += 1
    print("D is greater")
    equalFunc()
  elif c == d:
    print("C and D are now equal!")

equalFunc()

class patsClass:
  a = 5
  b = 10

p2 = patsClass()
print(p2.b)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("And I am " + str(self.age) + " years old")

p1 = Person("Robert", 36)
p1.myfunc()

numList = range(1, 31)
def fizzBuzz(list): 
  for i in list:
    if i % 15 == 0:
      print('fizzBuzz')
    elif i % 5 == 0:
      print('Buzz')
    elif i % 3 == 0:
      print('Fizz')
    else:
      print(i)

fizzBuzz(numList)