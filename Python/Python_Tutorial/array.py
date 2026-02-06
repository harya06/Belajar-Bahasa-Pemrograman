cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)

print("\n")
print(cars[2])
print(len(cars))

print("\n")
cars.append("Honda")

for x in cars:
    print(x)

print("\n")
cars.pop(0)

for x in cars:
    print(x)

print("\n")
cars.remove("BMW")

for x in cars:
    print(x)