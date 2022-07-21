# db1.py

import sqlite3

# 연결객체 리턴(데이터 베이스 파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")
# 커서 객체(SQL 구문을 실행하는 객체)
cur = con.cursor()
# 테이블 생성
cur.execute("create table PhoneBook(Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');") # values(복수)로 해줘야 함

#외부에서 입력 파라미터로 처리
name = "gildong"
phoneNumber = "010-222"
#입력 파라미터 처리
cur.execute("insert into PhoneBook values(?, ?);", (name, phoneNumber)) # 튜플로 여러개를 묶어서 하나로 리턴

# 다중의 데이터 입력
datalist = (("tom", "010-123"), ("dsp", "010-456"))
cur.executemany("insert into PhoneBook values(?, ?);", datalist)

# 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

# 