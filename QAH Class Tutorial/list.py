my_list = [1,3,4,8,5,0,6,7,7,8,8]

my_list.append(101)
print(my_list)

my_list.insert(4,29)
my_list.insert(5,500)
print(my_list)

my_list.extend([101,202])
print(my_list)

my_list.remove(8)
print(my_list)

poped_item = my_list.pop()
print(poped_item)
print(my_list)

temp_list = my_list.copy()
print("temp: ",temp_list)
temp_list.clear()
print(temp_list)

print(my_list.count(7))

print("list: ", my_list)
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list.index(101))

print(my_list[3])