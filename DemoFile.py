# DemoFile.py

print("---정렬방식---")
for x in range(1,6):
    print(x,"*", x, "=", x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("---0으로채우기---")
for x in range(1,6):
    print(x,"*", x, "=", str(x*x).zfill(3))

# x: 16진수로 표시
print("{0:x}".format(10))

# b: 2진법으로 표시
print("{0:b}".format(10))

# ,: 천 단위로 끊어서 표시(돈)
print("{0:,}".format(1500000))

# e: 자연상수(e)로 표시
print("{0:e}".format(4/3))

# f: 소수점 표시
print("{0:f}".format(4/3))

#소수점 이하 2자리까지
print("{0:.2f}".format(4/3))

url = "http://www.credu.com/?page=" + str(1)
print(url)

# 파일을 생성
f = open("denmo.txt", "wt")
f.write("첫번쨰\n두번쨰\n세번째\n")
f.close()