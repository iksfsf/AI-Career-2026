import json

student={
    "name":"Tabish",
    "age":22,
    "university":"ITU",
    "degree":"BSCS",
    "skills":["Python", "JavaScript", "SQL"],
    "goal":"Machine Learning Engineer"

}


with open("student2.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student2.json", "r") as file:
    data=json.load(file)

print(data)


student["skills"].append("Data Analysis")
with open("student2.json", "w") as file:
    json.dump(student,file, indent=4)
    
    
with open("student2.json", "r") as file:
    updated_student=json.load(file)
    print(updated_student)