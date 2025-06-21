def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark <=79 and mark >=70:
        return "B"
    elif mark >= 50 and mark <= 69:
        return "C"
    else:
        return "F"

student_name = input("Enter user name: ")

mark_1 = int(input("Enter first subject mark: "))
mark_2 = int(input("Enter second subject mark: "))
mark_3 = int(input("Enter third subject mark: "))

print("------ Student Report --------")
# calculate
total_marks = mark_1 + mark_2 + mark_3
print("total marks: ", total_marks)

average_marks = total_marks / 3
print("average mark : ", average_marks)

# percentage_mark =

# assign grade
print("First subject grade: ", get_grade(mark_1))
print("Second subject grade: ", get_grade(mark_2))
print("Third subject grade: ", get_grade(mark_3))

# check pass or fail
if mark_1 >= 40 and mark_2 >= 40 and mark_3 >= 40:
    print(f"{student_name} has passed the exam")
else:
    print(f"{student_name} has failed the exam")

# check scholarship eligibility
if average_marks >= 85:
    if mark_1 >= 80 and mark_2 >= 80 and mark_3 >= 80:
        print(f"{student_name} is eligible for scholarship")
    else:
        print(f"{student_name} is not eligible for scholarship")
else:
    print(f"{student_name} is not eligible for scholarship")

# add bonus mark
mark_1 += 5
mark_2 += 5
mark_3 += 5

total_marks = mark_1 + mark_2 + mark_3
average_marks = total_marks / 3
print("Total marks after adding bonus mark: ", total_marks)
print("Average mark after adding bonus mark: ", average_marks)