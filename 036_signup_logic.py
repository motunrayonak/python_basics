import json

with open ("035_signup_data.json","r")as my_file:
    my_list_dict=json.load(my_file)


a=input("enter id:")
b=input("enter first_name:")
c=input("enter last_name:")
d=input("enter email:")
e=input("enter password:")


data_dict={
        "id":a,
        "first_name":b,
        "last_name":c,
        "email":d,
        "password":e
        }


my_list_dict.append(data_dict)
print(my_list_dict)

with open ("035_signup_data.json","w") as my_file:
    json.dump(my_list_dict,my_file)

