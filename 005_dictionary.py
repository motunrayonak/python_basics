student_info= { 
               "name":"bola tinubu",
               "age":20,
               "grade":"c",
               "subjects":["maths","physics","chemistry"],
               "address":{"city":"lagos","country":"nigeria"}
               }
print(student_info["name"])

print(student_info.get("age"))

print(student_info["subjects"])

print(student_info["address"]["city"])

student_info["grade"]="A"
print(student_info["grade"])

student_info["gpa"]=4.5
print(student_info)

student_info.update({"age":21,"school":"OAU"})
print(student_info)

del student_info["gpa"]
print(student_info)

age=student_info.pop("age")
print(student_info)

print(len(student_info))

print(student_info.keys())

print(student_info.values())

print(student_info.items())

for keys in student_info:
    print(keys)

for keys,values in student_info.items():
    print(keys,values)

    


