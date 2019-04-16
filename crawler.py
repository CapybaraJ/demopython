#coding: utf-8
# use bs4 to craw the web content
# it's suggested to use bs4 in python3, but this file is suitable for python2
import requests
from bs4 import BeautifulSoup

def gethtmlcontent(curl):
    response = requests.get(curl) #get page
    soup = BeautifulSoup(response.text, 'lxml') #use lxml format to explain it
    toc = soup.find('div',id='toc') # find dom element by id
    # print entry
    dfslist(1, toc)


def dfslist(classid, content):
    temp = 'toclevel-{}'.format(classid)
    # print temp
    allist = content.find_all('li',{'class':temp})
    if allist is None or not allist:
        return None
    # print allist
    for sublist in allist:
        title = sublist.find('a')
        tcontent = title.find_all('span')
        realtitle = tcontent[0].text + " " + tcontent[1].text
        for i in range(classid-1):
            print " ",
        print realtitle
        dfslist(classid+1,sublist)
        # print subcontent


gethtmlcontent('https://www.owasp.org/index.php/HttpOnly')


'''
you can use this method to get attrs
    soup.a.attrs   return a dict containing all attrs
    soup.a.attrs['href'] get the attr:href
    soup.a['href']
use this method to get content in tag:
    xxx.string
    xxx.text
    xxx.get_text()
    PS: If the tag is nested with another tag, method 1 is None, the others is pure text
'''