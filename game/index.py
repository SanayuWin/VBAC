name = "sanayu"
age = 20

# print(f"name : {name}, age : {age}")


name = str("sanayu")
age = int(20)
score = float(75.5)
boolean = True
# print(f"name : {name}, type {type(name)}")
# print(f"age : {age}, type {type(age)}")
# print(f"score : {score}, type {type(score)}")
# print(f"boolean : {boolean}, type {type(boolean)}")

thislist = ["apple", "banana", "cherry"]
# print(thislist)
# print(len(thislist))
thislist[1] = "kiwi"
print(thislist)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
# thistuple[1] = "kiwi"
# print(thistuple)
changetuplie = list(thistuple)
changetuplie[1] = "kiwi"
thistuple = tuple(changetuplie)
print(thistuple)

a = 300
b = 200
if b > a:
    print("b มากกว่า a")
elif a == b:
    print("a เท่ากับ b")
else:
    print("a มากกว่า b")

i = 0
while i <= 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("จบการวนซ้ำ")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    if x == "banana":
        break

def my_function(name):
    print("Hello " + name)

my_function("sanayu")