## 데이터포털 API 크롤링
import os
import sys
from threading import gettrace
import urllib.request
import datetime
import time
import json
import pandas as pd

ServiceKey =   'Ody77GLuYeR%2FeFqbpduMN2Bi4Cka2fztbgnj6E2Eux1kUhy3e4epR28XKBUaObiqPoVzAizxXMBPXtMyuC9v9Q%3D%3D'

def getRequestUrl(url): 
    req = urllib.request.Request(url) 

    try :
        res = urllib.request.urlopen(req)   
        if res.getcode() == 200:   #200 OK   40X error   50X Server error
            print(f'{datetime.datetime.now()}] Url Request success')
            return res.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None 


def getTourismStatesItem(yyyymm, nat_cd, ed_cd):
        service_url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
        params = f'?_type=json&serviceKey={ServiceKey}'  # 인증키
        params += f'&YM={yyyymm}'
        params += f'&NAT_CD={nat_cd}'
        params +=f'&ED_CD={ed_cd}'
        url =service_url + params

        retData = getRequestUrl(url)

        if retData == None:
            return None
        else :
            return json.loads(retData)

def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = [ ]
    result = [ ]
    natName = ''
    dataEnd = f'{nEndYear}{12:0>2}'
    isDataEnd = False #데이터 끝 확인용 플래그

    for year in range(nStartYear, nEndYear+1):
            for month in range(1,13):
                    if isDataEnd == True: break

                    yyyymm = f'{year}{(month):0>2}' # 2022 1월 202201
                    jsonData = getTourismStatesItem(yyyymm,nat_cd,ed_cd )


                    if jsonData['response']['header']['resultMsg'] == 'OK':
                        #데이터가 없으면 서비스 종료
                        if jsonData['response']['header']['resultMsg'] == '':
                            isDataEnd = True
                            dataEnd = f'{year}{month-1:0>2}'
                            print(f'제공되는 데이터는 {year}년 {month-1}월까지 입니다')
                            break

                        print(json.dumps(jsonData, indent = 4, sort_keys = True, ensure_ascii=False))
                        natName = jsonData['response']['body']['items']['item']['natKorNm']
                        natName = natName.replace('','')
                        num = jsonData['response']['body']['items']['item']['num']
                        ed = jsonData['response']['body']['items']['item']['ed']

                        jsonResult.append({'nat_name': natName, 'nat_cd':nat_cd,
                                                          'yyyymm':yyyymm, 'visit_num':num })      
                        result.append([natName, nat_cd, yyyymm,num])

    return (jsonResult, result, natName, ed, dataEnd)

def main():
        jsonResult = []
        result = []
        natName = ''
        ed = ''
        dataEnd = ''






        print('<< 국내 입국한 외국인 통계데이터를 수집합니다>>')
        nat_cd = input('국가코드 입력(중국 : 112 / 일본 : 130 / 필리핀:155) > ')
        nStartYear = int(input('데이터를 몇년부터 수집할까요? '))
        nEndYear = int(input('데이터를 몇년까지 수집할까요? '))
        ed_cd = 'E' # D:한국인외래관광객 / E : 방한외국인

        getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)

        if natName =='':
            print('데이터 전달 실패. 공공데이터포털 서비스 확인요망')
        else:
            columns = ['입국국가', '국가코드', '입국연월', '입국자수']
            result_df = pd.DataFrame(result, columns=columns)
            result_df.to_csv(f'./{natName}_{ed}_{nStartYear}_{dataEnd}.csv',index=False,
                                        encoding='utf-8')

            print('csv파일 저장완료')
       

if __name__ == '__main__':
    main()