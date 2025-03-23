import json

student={
        "id":1,
        "name":"motunrayo",
        "gender":"female",
        "department":"english",
        "school":"unilag"
        }
with open("013_data.json","w") as my_file:
    json.dump(student,my_file)

print(student)
