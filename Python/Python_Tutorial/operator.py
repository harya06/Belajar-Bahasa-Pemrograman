print(465+54)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5

print(1 < x < 10)

print(1 < x and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)