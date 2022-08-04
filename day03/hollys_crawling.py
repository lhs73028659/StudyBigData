# 할리스 매장정보 크롤링
from bs4 import BeautifulSoup
import urllib.request
import pandas as  pd
import datetime

result = []
def getHollysStoreInfo(result):
    for page in range(1,2):  #53페이지까지 있기 때문
        hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        # print(hollys_url)
        html = urllib.request.urlopen(hollys_url)
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.find('tbody')

        for store in tbody.find_all('tr'):    #tbody 안에 여러 개 있는 tr 찾기
            if len(store) <= 3: break

            store_td = store.find_all('td')
            
            store_name = store_td[1].string #두번쨰값
            store_sido = store_td[0].string #첫번째값
            store_address = store_td[3].string
            store_phone = store_td[5].string

            result.append([store_name]+[store_sido]+[store_address]+[store_phone])






def main( ):
    result = []
    print('할리스 매장 크롤링 >>>')
    getHollysStoreInfo(result)

    columns = ['store','sido-gu','address','phone']
    hollys_df =pd.DataFrame(result, columns=columns)    

   # hollys_df.to_csv('C:/localRepository/StudyBigData\day03/hollys_shop_info.csv',index=True, encoding='utf-8')
    hollys_df.to_csv('./hollys_shop_info.csv', index=True, encoding='utf-8')
    print('저장완료')

if __name__ == '__main__':
    main()