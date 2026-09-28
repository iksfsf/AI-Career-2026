# with open("student.txt","w") as file:
    
#     file.write("Name: Tabish\n")
#     file.write("Age: 22\n")
#     file.write("University: ITU\n")
#     file.write("Degree: BSCS\n")
    
    
# with open("student.txt", "r") as file:
#     data=file.read()
    
    
# print(data)

# with open("student.txt", "a") as file:
#     file.write("Goal: AI Engineer\n")
    
    
# with open("student.txt", "r") as file:
#     data=file.read()
        
# print(data)



# import json

# student = {
#     "name": "Tabish",
#     "age": 22,
#     "university": "ITU",
#     "goal": "AI Engineer"
# }

# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)

print(student["name"])
print(student["age"])
print(student["university"])
print(student["goal"])

student["goal"] = "Machine Learning Engineer"

print(student)

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)