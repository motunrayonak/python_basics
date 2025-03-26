import json
with open ("016_data.json","r") as my_file:
    my_list=json.load(my_file)

a=input("id:")
b=input("firstname:")
c=input("lastname:")
d=input("email:")
e=input("password:")

data_dict={
            "id":a,
            "first_name":b,
            "last_name":c,
            "email":d,
            "password":e
         }

my_list.append(data_dict)
print(my_list)

with open("016_data.json","w") as my_file:
    json.dump(my_list,my_file)
