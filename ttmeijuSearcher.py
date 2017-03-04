import requests
import os
from bs4 import BeautifulSoup
def main():
    searchDrama('杀手')
    # searchResource('吸血鬼日记')


#查找种子

def searchResource(keyword):
    payload = {'keyword': keyword, 'range': '1'}
    response = requests.get(url='http://ttmeiju.com/index.php/search/index.html',
                            params=payload)
    save(response.text, 'resource')
    cookASoup(response.text, taste=0)
#查找美剧
def searchDrama(keyword):
    payload = {'keyword': keyword, 'range': '0'}
    response = requests.get(url='http://ttmeiju.com/index.php/search/index.html',
                            params=payload)
    save(response.text, 'dramaList')
    # file = open('searchResult.txt', 'r')
    # cookASoup(file.read())
    cookASoup(response.text,taste=1)
    # print(response.text)

def cookASoup(content,taste):
    print('==='*20)
    soup = BeautifulSoup(content)

    seedTable = soup('table', class_='seedtable')
    infos = seedTable[0]('tr', bgcolor='#ffffff')
    if taste == 0:
        content = getDownloadURL(infos)
    elif taste == 1:
        content = getDramaData(infos)
    print(content)
    print(len(content))
    # refine(infos)
def getDownloadURL(infos):
    content = []
    trIndex = 0
    for list in infos:
        tds = list.find_all('td')
        content.append([])
        for i in range(len(tds)):
            if i == 2:
                urls={}
                items = tds[i].find_all('a')
                for item in items:
                    urls[item.get('title')] = item.get('href')
                content[trIndex].append(urls)
            else:
                content[trIndex].append(tds[i].get_text().strip())
        trIndex += 1
    return content
def getDramaData(infos):
    content = []
    trIndex = 0
    for list in infos:
        tds = list.find_all('td')
        content.append([])
        for i in range(len(tds)):
            if i == 1:
                urls = {}
                item = tds[i].find('a')
                urls[item.get_text()] = 'http://www.ttmeiju.com'+item.get('href')
                content[trIndex].append(urls)
            else:
                content[trIndex].append(tds[i].get_text().strip())
        trIndex += 1
    return content



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
