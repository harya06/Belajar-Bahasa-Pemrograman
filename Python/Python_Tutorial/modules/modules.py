import mymodules

a = mymodules.person1["age"]
print(a)

print("\n")

#===========================Alias==================

import mymodules as mx

a = mx.person2["name"]
print(a)
print("\n")

#==================================================

from mymodules import person3

print(person3["name"])
print(person3["age"])
print(person3["country"])

x = dir(mymodules)
print(x)