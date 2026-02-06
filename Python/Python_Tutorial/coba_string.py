print("Hallo nama saya Harya")

a = "Saya sedang belajar Python"
print(a)

a = """ 
    Saya Harya. Saya sedang belajar python dasar,
untuk belajar fundamental dan analisis data
"""
print(a)

a = "Hallo World"
print(a[0])
print(len(a))

print("\n")

for x in "harya":
    print(x)

print("\n")

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print("\n")

b = "Hello, World!"
print(b[1:5])
print(b[:5])
print(b[1:])
print(b[-5:-2])

print("\n")

a = "Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

print("\n")

a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

print("\n")

age = 20
txt = f"My name is Harya, I am {age}"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)