# fail to run until now with error : AttributeError: module 'dart_fss' has no attribute 'set_api_key'

# https://dart-fss.readthedocs.io/en/latest/
# https://github.com/josw123/dart-fss

#import sys
#sys.path.append('/usr/local/lib/python3.7/site-packages')

import dart_fss as dart

# Open DART API KEY 설정
f = open("dart.key" , "r")
dart_key = f.readline().strip()
print("dart_key:" + dart_key + "\n")
#api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
print('get key : ' + dart.get_api_key())
dart.set_api_key(api_key=dart_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
samsung = corp_list.find_by_corp_name('삼성전자', exactly=True)[0]

# 2012년부터 연간 연결재무제표 불러오기
fs = samsung.extract_fs(bgn_de='20120101')

# 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
fs.save()
