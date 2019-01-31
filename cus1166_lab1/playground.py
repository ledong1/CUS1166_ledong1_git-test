print("Basic program")

print("Hello World")
myname = input("What is your name:")
print("Hello" + str(myname))
print("Hello %s" % myname)

print("Done basic programs")

print("Variables")

i = 120
print(f"Variable i has the value {i}")

f = 1.2342354
print(f"Variable i has the value {f} and is of type {type(f)}")

b = True
print(f"Variable i has the value {b}")

n = None
print(f"Variable i has the value {n}")

i = 120
print(f"Variable i has the value {i} and is of type {type(i)}")
i = 120.0
print(f"Variable i has the value {i} and is of type {type(i)}")

c = (10,20,30)
print(f" c[0] has the value {c[0]} and is of type: {type(1)}")

s = set()
s.add(1)
s.add(2)
print(s)


grades = {"Tom" : "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"
print(grades)
mydictionary = dict()

print("Done Variables")


print("Conditions")
x=0
if (x > 0):
    print("The number x is positive")
elif (x<0):
    print("The number x is negative")
else:
    print("The number x is zero")

print("Done Conditions")

print("Loops")
for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )

print("Done Loops")


print("Functions")
def is_even(x):
    if (x%2 == 0):
        print("The number x is even")
    else:
        print("The number is odd")

print("Done Functions")

print("Classes")
class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)

print("Done Classes")

print("Define a module file")

print("Done Define a module file")

print("Use a module")
from mymodules.helper_utils import square
print(square(100))
print("Done Use a module")
