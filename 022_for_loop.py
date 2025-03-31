x=int(input("enter a starting number"))
y=int(input("enter a ending number"))

print("even number in the given range:")

for num in range (x,y + 1):
    if num % 2 ==0:
        print(num)


