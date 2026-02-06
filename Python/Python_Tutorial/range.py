x = range (10)
print(x)

for a in x:
    print(a)

x = range (3, 10)
print(x)

for a in x:
    print(a)

x = range (1, 10, 2)
print(x)

for a in x:
    print(a)

print("\n")
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

print("\n")

r = range(10)

print(r[2])
print(r[:3])
print(r[:6:2])

for x in r[:6:2]:
    print(x)

print("\n")

r = range(0, 10, 2)

print(6 in r)
print(7 in r)
print(len(r))