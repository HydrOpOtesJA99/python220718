# ifelse.py
# 다중라인의 주석 처리: ctrl + / (cmd + /)
# input이 무조건 문자열이라 int (정수)로 바꿔준다

# score = int((input("점수를 입력:"))) 
# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score < 90:
#     grade = 'B'
# elif 70 <= score < 80:
#     grade = 'C'
# else:
#     grade = 'd'

# print("등급은" , grade)

# 반복문
value = 5
while value > 0:
    print(value)
    value -=1

print("---for in ---")
lst = [1,2,3]
for item in lst:
    print(item)

lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 ==0:
        continue
    print("Item:{0}".format(i))
