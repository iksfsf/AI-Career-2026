


def sayhello():
    print("hello Tabish")
    
    
    
    
sayhello()
sayhello()
sayhello()

def greet(name):
    print("hello",name)
    
    
greet("Tabish")
greet("Ali")
greet("Ahmed")




def add(a, b):
    return a + b




c=add(5, 10)
d=add(20, 30)
e=add(100, 50)
print(c)
print(d)
print(e)


def square(number):
    return number * number




result=square(5)
print("square of 5 is", result)



def check_age(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")

check_age(25)
check_age(15)
check_age(18)





def calculate_total(subjects):
    total = 0
    for score in subjects:
        total += score
        
    return total
    

subjects = [85, 90, 78, 92, 88]
total = calculate_total(subjects)

def calculate_average(subjects):
    total = calculate_total(subjects)
    if len(subjects) == 0:
        return 0
    else:
        return total / len(subjects) 
    

average = calculate_average(subjects)

def calculate_subject_grade(subjects):
    average = calculate_average(subjects)
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


grade = calculate_subject_grade(subjects)

print("Total:", total)
print("Average:", average)
print("Grade:", grade)