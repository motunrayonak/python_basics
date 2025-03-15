string_list=["apple","banana","cherry","date","fig"]
int_list=[5,3,8,1,9,2]

print(string_list + int_list)

print(len(string_list))

print(string_list[0])

print(string_list[-1])

print(int_list[0:4])

string_list.append("grape")
print(string_list)

string_list.insert(2 , "orange")
print (string_list)

int_list2=[10,11,12]
int_list.extend(int_list2)
print(int_list)

string_list.remove("banana")
print(string_list)

int_list.pop()
print(int_list)

string_list.reverse()
print(string_list)

int_list.sort()
print(int_list)

int_list.sort(reverse=True)
print(int_list)

print(min(int_list))

print(max(int_list))

print(sum(int_list))

print(string_list.index("cherry"))

print("fig" in string_list)

for index,list in enumerate(string_list):
    print(index,list)

string_str='- '.join(string_list)
print(string_str)

new_list=["apple","banana","cherry","date"]
list_str='- '.join(new_list)
print(list_str)

fruit_tuple=("mango","pineapple","papaya","guava")
print(fruit_tuple)

for fruit in fruit_tuple:
    print(fruit)
 
print(fruit_tuple[0:-2])

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.union(set2))





