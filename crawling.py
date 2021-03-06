import requests
#import beautifulsoup as bs4
from bs4 import BeautifulSoup
#import BeautifulSoup4
import json
import re

#key : Dart의 api 키. Dart에 가입 후 api 키를 할당받는다.
#number : 종목코드
#year : 사업보고서 년도 검색
key='721d86110d18200b38ae64b788b43a8e14688217'
number='005930'
year='2019'

# step 1 : 해당년도의 사업보고서 검색
req = requests.get('http://dart.fss.or.kr/api/search.json?auth='+key+'&crp_cd='+number+'&start_dt='+year+'0101&end_dt='+year+'1231&bsn_tp=A001')
html = req.text
code=json.loads(html)
url='https://dart.fss.or.kr/dsaf001/main.do?rcpNo='+code['list'][0]['rcp_no']
print('사업보고서 url = '+url)

#  step 2 : 사업보고서를 크롤링
req2=requests.get(url)
html2=req2.text
soup2=BeautifulSoup(html2, 'html.parser')
#제무제표 페이지 찾기
body=str(soup2.find('head'))
a=re.search(' 재무제표', body).span()
# 요약재무정보 근처에서 숫자 정보 찾기(자바스크립트로 되어있지만 정규표현식으로 검색)
b=re.search(r'viewDoc(.*);',body[a[0]:a[1]+1000]).group()
#필요없는 부분 제거
list=b[8:-2].split(', ')
list=[i[1:-1] for i in list]
url_final='http://dart.fss.or.kr/report/viewer.do?rcpNo='+list[0]+'&dcmNo='+list[1]+'&eleId='+list[2]+'&offset='+list[3]+'&length='+list[4]+'&dtd=dart3.xsd'
print('재무제표 url = '+url_final)
# step 3 : 사업보고서의 재무제표 페이지까지 진입 후, 테이블 크롤링. 이 곳부터 자신의 방식에 맞게 Pandas나 csv를 사용하세요. 저는 그냥 텍스트 탭(\t) 크롤링.

req3=requests.get(url_final)
html3=req3.text
#판다스 이용해서 테이블 얻어내기
import pandas as pd
import lxml
df = pd.read_html(html3)

import openpyxl
df[1].to_excel('data.xlsx')
