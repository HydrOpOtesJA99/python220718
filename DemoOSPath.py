# DemoOS.py

import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---샘플링---")
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

# 파일명을 다루는 경우
from os.path import * 
print(abspath("python.exe")) # 절대 경로를 출력
print(basename("c:\\python39\\python.exe")) # 전체 경로를 주면 맨뒤의 파일명만 남김
print(getsize("c:\\python39\\python.exe")) # 파일의 크기가 필요할 경우

# 운영체제 정보를 가져오는 경우
from os import *
print("운영체제명:", name) # 운영체제명: nt -> 윈도우 사용중이라는 뜻
system("notepad.exe") 

# 파일 리스트
import glob
result = glob.glob("c:\\work\\*.py")
print(result)