# check a number positive and even

number = int(input("Enter a number: "))

positive = number > 0
even = True if(number % 2 == 0) else False

if(positive and even):
    print("YES : The number is positive and even number")
else:
    print("NO")