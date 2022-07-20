# Demostr.py

# 목록 확인
# print(dir(str))

strA = "파이썬은 강력해"
strB = "python is very powerul"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.startswith("py"))
print(strB.endswith("ful"))
print(strB.endswith("ful", 7))
print(strB.count("p"))
print(strB.count("p", 7))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())

u = " spam and ham " # 앞 뒤의 공백문자를 없애고 싶다
result = u.strip()
print(u)
print(result)

u = "<<< spam and ham >>>" # 꺽쇄를 없애고 싶다
result = u.strip("<>") # 앞 뒤에 있는 어떤 문자를 없애고 싶다.
print(u)
print(result)

result = result.replace("spam", "span egg")
print(result)
lst = result.split() # split은 list로 바꾸고
print(lst)
print(":)".join(lst)) # 전체를 str로 바꾼다