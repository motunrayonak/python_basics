import json
a=input("user id")
b=input("user first_name")
c=input("user lastname")
d=input("user email")
e=input("user password")

user={
"id":a,
"first_name":b,
"last_name":c,
"email":d,
"password":e
}

with open ("015_register.json","w")as my_file:
    json.dump(user,my_file)

print(user)

