# funtion4.py
# 기본값 세팅
def times( a=10, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5,6))

# 가변인자(입력 parameter 객수가 가변적인 경우)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print (union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

# 정의되지 않은 인자(dictionary 형식으로 받음)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

# 호출
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234"))
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234", name=";mike"))
