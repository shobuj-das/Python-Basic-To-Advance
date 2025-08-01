x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# set global variable in method
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# change the global variable in a method
name = "Green"

def myfunc():
    global name
    name = "Blue"
    print("inside method: ",name)
myfunc()
print("Outside method: ",name)