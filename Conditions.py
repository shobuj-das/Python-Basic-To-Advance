a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# --------------- Logical and or not
print("------------- Logical and or not-------")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")