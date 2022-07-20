# DemoFile2.py

# 파일을 생성 -> denmo.txt 파일이 work 폴더에 생성된 걸 확인가능
f = open("denmo.txt", "wt")
f.write("첫번쨰\n두번쨰\n세번째\n")
f.close()

# 파일을 읽어서 처리 -> 터미널에 denmo.txt 파일을 읽어들인다.
f = open("denmo.txt", "rt")
result = f.read()
print(result)
print(f.tell())
f.seek(0) # 처음으로 돌아가라
lst = f.readlines() # 처음부터 읽어서 list 개체로 return
print(lst)

for item in lst:
    print(item, end="") # print 함수가 원래 줄을 한번 바꿔주므로 end=""로 줄바꿈 엇ㅂ애줌

# 처음으로 리셋
f.seek(0)
print(f.readline()) # line을 1개씩만 읽는다, print가 줄 바꿔주고 파일 속 \n이 하나 더 있어 줄이 또 바뀜
print(f.readline(), end="")
f.close()

# with 구문을 같이 사용하는 경우
with open("denmo.txt", "rt") as f: # with 블록 안에서만 파일을 쓰고 나갈때는 닫고 나간다
    for item in f.readlines():
        print(item, end="")
    # with 블록 안에서는 f.close()가 없어도 됨

# a+ 뒤에 내용을 첨부할 경우
print("---첨부하는 경우---")
f = open("denmo.txt", "a+") # 뒤에 내용을 첨부할 때 a+사용
f.write("다른 데이터\n")
f.close()

# wt 덮어쓰기를 하는 경우
# print("---덮어쓰기하는 경우---")
# f = open("denmo.txt", "wt") # 뒤에 내용을 첨부할 때 wt사용 조심할 것 !
# f.write("다른 데이터\n")
# f.close()