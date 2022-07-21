# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

# 우리 웹사이트는 웻봇 금지: 스크립트가 
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        # 오늘의 유머
        data ='http://www.todayhumor.co.kr/board/list.php?kind=total&table=total&page=' + str(n)
        print(data) # 주소확인
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <span class="subject_fixed" data-role="list-title-text">
        #       아이패드 프로 3세대 12.9인치 256g wifi 버전(스마트 키보드 폴리오 케이스 포함)
        # </span>

        # 속성들(attrs) 홈페이지마다 다름
        list = soup.findAll('span', attrs={'data-role':'list_title-text'}) 

        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        title = item.text.strip()
                        if (re.search('아이폰', title)):
                                print(title.strip())
                                print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
