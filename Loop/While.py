i=1
while i<10:
    print(i)
    i+=1



x = 1
while x < 10:
    print(x)
    if(x==4):
        break
    x+=1

x = 1
while x < 10:
    if x == 4:
        x += 1
        continue
    else:
        print(f'x = {x}')
    x+=1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")