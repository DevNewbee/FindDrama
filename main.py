import requests
import os
from bs4 import BeautifulSoup
def main():
    keyword = '杀手'
    payload = {'keyword': keyword, 'range': '0'}
    response = requests.get(url='http://ttmeiju.com/index.php/search/index.html?keyword=%E5%B0%91%E7%8B%BC&range=0', params=payload)

    cookASoup(response.text)

def cookASoup(content):
    print('==='*20)
    titles = []
    soup = BeautifulSoup(content)
    seedTables = soup('table', class_='seedtable')

    for seedTable in seedTables:
        titles.append(seedTable('td'))

    assembler(titles)

def assembler(lists):
    result=[{}]
    resultIndex = 0
    for list in lists:
        titles = []
        values = []
        for index,item in enumerate(list):
            if index == 0:
                continue
            if index <= 6:
                titles.append(item.get_text().strip())
            elif index < 13:
                values.append(item.get_text().strip())
        for index, title in enumerate(titles):
            result[resultIndex][title] = values[index]

        resultIndex += 1

    print(result)

def printList(list):
    for item in list:
        print('===')
        print(item.get_text().strip())

def save(content: str, fileName):
    filePath = os.getcwd() + '/' + fileName + '.txt'
    f = open(filePath, 'w+')
    print('正在保存 ' + fileName  + '.hmtl 信息')
    print('=' * 40)
    f.write(content)
    f.close()


if __name__ == '__main__':
    main()
