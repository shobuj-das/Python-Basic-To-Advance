def get_average(number_list, total_number):
    sum = 0
    for number in number_list:
        sum += number
    return sum / total_number

total_number = 5
number_list = []

for x in range(total_number):
    x = int(input("enter a number: "))
    number_list.append(x)

print("Average of 5 numbers: ", get_average(number_list, total_number))