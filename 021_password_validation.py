password="python123"
while True:
    user_pswd=input("enter password")
    if user_pswd==password:
        print("access granted")
        break
    else:
        print("wrong password,try again!")
