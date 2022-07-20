# DemoRE.py

import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())


result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())


# 함정추가
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# 함정추가
# result = re.match("[0-9]*th", " 35th")
# print(result)
# print(result.group()) # None 이라고 결과가 나옴

print(bool(re.search("apple", "this is apple"))) # search는 this is apple 전체 보고 apple 찾는다
print(bool(re.match("apple", "this is apple"))) # match는 this 까지만 보고 확인하지 못했다고 결론지음

result = re.search("\d{4}", "올해는 2022년") # 4개 연속된 문자열을 출력?
print(result.group())
result = re.search("\d{5}", "우리 동네는 47714입니다") # 5개 연속된 문자열을 출력?
print(result.group())