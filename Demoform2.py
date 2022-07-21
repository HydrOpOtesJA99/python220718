# Demoform2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 웹 서버와 통신할 경우 웹서버에 요청을 해야함
import urllib.request
# 크롤링
from bs4 import BeautifulSoup

# 폼디자인을 로딩(2번폼)
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

# 클래스 정의 (QMainWindow)
class DemoForm(QMainWindow, form_class):
    # 초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self) # setupUI로 초기화
    # 슬롯 메서드
    def firstClick(self):    
        # 파일로 저장
        f = open("webtoon.txt", "wt", encoding="utf-8")
        # 페이징 처리를 위해 range()함수를 사용
        # 에러처리
        try:
            for i in range(1,6):
                # 여러 문장 들여쓰기 : tab, 여러문장 들여쓴거 다시 돌리기: shift + tab
                # 여러 페이지에서 데이터를 전체 가져오고 싶은 경우에는 url 주소를 확인해 page=n 에서 n값이 바뀌는걸 확인하면 됨
                url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
                # 네이버에서 실행한 페이지 결과를 문자열로 받기
                data = urllib.request.urlopen(url)
                # 검색이 용이한 객체
                soup = BeautifulSoup(data, "html.parser")
                #특정한 태그를 검색
                cartoons = soup.find_all("td", class_="title") # "title"인 애들만 빼내라       

                # <td class="title">
                # 	<a href="/webtoon/detail">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
                # </td>
                # print("갯수:{0}".format(len(cartoons)))
                # title = cartoons[0].find("a").text # <a>에서 text를 가져와라
                # link = cartoons[0].find("a")["href"] # href라는 attribute가 궁금하니 그걸 가지고와라
                # print(title)
                # print(link)

                for item in cartoons:
                    item2 = item.find("a") # <a> 페이지를 찾아라
                    title = item2.text.strip() # .strip 앞 뒤 공백문자 제거
                    print(title)
                    f.write(title + "\n")
        except:
            pass
        f.close()
        self.label.setText("웹툰 크롤링 종료")
            # 슬롯 method
    def fristClick(self):
        self.label.setText("첫번째 클릭")
    # 슬롯 method
    def secondClick(self):
        self.label.setText("두번째 클릭")
    # 슬롯 method
    def thirdClick(self):
        self.label.setText("세번째 클릭")
    
# 진입점을 체크
#if __name__ == "__main__": # 체크를 안할 경우에는 빼버린다
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec()