# function2.py
print("---불변형식---") 
a = 1.2
print(id(a))

a = 2.3
print(id(a))

print("---가변형식---") # 주소가 바뀌면 안됨
lst = [1,2,3]
print(id(lst))

lst.append(4)
print(id(lst))