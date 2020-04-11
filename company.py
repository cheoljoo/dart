# https://opendart.fss.or.kr/guide/main.do?apiGrpCd=DS001

import sys
import pandas as pd
import requests
import zipfile
import json

#다트 오픈 api 에서 회사고유번호 다운받기
from requests import get  # to make GET request

def download(url, file_name):
    with open(file_name, "wb") as file:  
        response = get(url)              
        file.write(response.content)      

if __name__ == '__main__':
    f = open("dart.key" , "r")
    dart_key = f.readline().strip()
    print("dart_key:" + dart_key + "\n")
    url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=" +dart_key
    print("dart_url:[" + url + "]\n")
    ret = download(url,"codes.zip")
    #print(ret.status)
    #print(ret.message)
    with zipfile.ZipFile("codes.zip","r") as zip_ref:
        zip_ref.extractall("codes")
#[출처] 다트(dart) 오픈 api 사용하기(python=3.7)|작성자 선인

#xml 파일 읽기
import xml.etree.ElementTree  as ET
tree = ET.parse('./codes/CORPCODE.xml')
root = tree.getroot()
kids = root.getchildren()

data=[]
for child in kids:
    if child.tag == "list":
        temp=[]
        for i in child:
            temp.append(i.text)
        data.append(temp)
#[출처] 다트(dart) 오픈 api 사용하기(python=3.7)|작성자 선인

고유번호=[]
회사이름=[]
종목코드=[]
변경일=[]
for i in data:
    고유번호.append(i[0])
    회사이름.append(i[1])
    종목코드.append(i[2])
    변경일.append(i[3])
    #print("i:" + ' id:' + i[0] + " cname:" + i[1] + " code:" + i[2] + " date:" + i[3] + "\n")
df=pd.DataFrame({"고유번호":고유번호,"회사이름":회사이름,"종목코드":종목코드,"변경일":변경일})

#회사이름으로 고유번호 찾기
df2=df.loc[df["회사이름"]=="굿모닝아이텍"]
#특정단어 포함한 회사 찾기
df.loc[df["회사이름"].str.contains('삼성')]
#[출처] 다트(dart) 오픈 api 사용하기(python=3.7)|작성자 선인




from urllib.request import urlopen
import webbrowser
from bs4 import BeautifulSoup

company_code="00356370"

# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019002
#url = "http://dart.fss.or.kr/api/search.xml?auth="+dart_key+"&crp_cd="+company_code+"&start_dt=19990101&bsn_tp=A001&bsn_tp=A002&bsn_tp=A003"
#url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=" + dart_key + "&corp_code=" + company_code
url = "https://opendart.fss.or.kr/api/company.json?crtfc_key=" + dart_key + "&corp_code=" + company_code
r=requests.get(url)
print(r.url)
print(r.status_code)
print(r.content)
#print(r.text)
#print(r.json())
#xmlsoup = BeautifulSoup(r.content,'html.parser')
#print(xmlsoup)





#resp=requests.get("https://opendart.fss.or.kr/api/fnlttSinglAcnt.json?crtfc_key=" + dart_key + "&corp_code=100120&bsns_year=2019")
resp=requests.get("https://opendart.fss.or.kr/api/list.json?crtfc_key=" + dart_key + "&bgn_de=20200117&end_de=20200117&corp_cls=Y&page_no=1&page_count=10")
resp.encoding = 'utf-8'
print("\nresp:")
print(resp)
print("\nresp.json:")
print(resp.json())
dict=resp.json()
print("\ndict:")
print(dict)
df2=pd.DataFrame(dict["list"])
print("\ndf2:")
print(df2)
#[출처] 다트(dart) 오픈 api 사용하기(python=3.7)|작성자 선인


# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS004&apiId=2019021
resp=requests.get("https://opendart.fss.or.kr/api/majorstock.json?crtfc_key=" + dart_key + "&corp_code=00356370")
resp.json()
print("\nresp.json:")
print(resp.json())
dict=resp.json()
df4=pd.DataFrame(dict["list"])
df4
print("\ndf4:")
print(df4)
#[출처] 다트(dart) 오픈 api 사용하기(python=3.7)|작성자 선인

sys.exit()

resp=requests.get("https://opendart.fss.or.kr/api/empSttus.json?crtfc_key=" + dart_key + "&corp_code=00356370&bsns_year=2018")
resp.json()
dict=resp.json()
df3=pd.DataFrame(dict["list"])
df3
#[출처] 다트(dart) 오픈 api 사용하기(python=3.7)|작성자 선인


