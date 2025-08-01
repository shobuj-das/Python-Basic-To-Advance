import GlobalVariables


def myFun():
    print("My fun")

myFun()

def fun(a,b):
    print(a+b)

fun(1,2)


def myReturn(a,b):
    return a+b

print(myReturn(2,9))


def callAnotherFun(x,y):
    return myReturn(x,y)
print(callAnotherFun(3,3))

print(callAnotherFun(myReturn(9,9),2))

# call from another file
print(GlobalVariables.myfunc())