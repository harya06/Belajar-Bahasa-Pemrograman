mytuple = ("apple", "banana", "cahrry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("\n")

for x in mytuple:
    print(x)

print(10*"=")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
    
  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(10*"=","\n")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)