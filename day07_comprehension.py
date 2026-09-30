numbers=[i for i in range(1,11)]
print(numbers)



squares=[i*i for i in range(1,11)]
print(squares)



cube=[i*i*i for i in range(1,11)]
print(cube)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers= [i for i in numbers if i%2==0]
print(even_numbers)

odd_numbers = [i for i in numbers if i%2!=0]
print(odd_numbers)


marks = [45, 78, 92, 33, 67, 88, 51, 29]
names= ["imran","sami", "aslam","kashif","riaz", "adnan", "zubair", "hanif"]

passed = [i for i in marks if i>=60]
print(passed)


passed_double=[i*2 for i in marks if i>=60]
print(passed_double)

students = ["Ali", "Ahmed", "Sara", "Usman"]
marks = [85, 55, 92, 48]

passed_students=[students[i] for i in range(len(students)) if marks[i]>=60]
passed_students_marks=[marks[i] for i in range(len(students)) if marks[i]>=60]
print(passed_students)
print(passed_students_marks)

students2 = ["Ali", "Ahmed", "Sara", "Usman", "Hassan"]
marks2 = [85, 65, 92, 48, 78]
passed_Students2=[students2[i] for i in range(len(students2)) if marks2[i]>=70]
passed_Students_marks2=[marks2[i] for i in range(len(students2)) if marks2[i]>=70]
print(passed_Students2)
print(passed_Students_marks2)

increased_marks=[marks2[i]*1.10 for i in range(len(students2)) ]
print(increased_marks)


students = ["Ali", "Ahmed", "Sara", "Usman", "Hassan", "Ayesha"]
marks = [85, 55, 92, 48, 78, 66]

passed_students=[students[i] for i in range(len(students)) if marks[i]>=60]
passed_students_marks=[marks[i] for i in range(len(students)) if marks[i]>=60]
failed_students=[students[i] for i in range(len(students)) if marks[i]<60]
increased_marks=[marks[i]+5 for i in range(len(students)) ]

print("Passed Students:", passed_students)
print("passed Students Marks:", passed_students_marks)
print("failed Students: ", failed_students)
print("increased marks students: ", increased_marks)
