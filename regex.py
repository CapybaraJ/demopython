# -*- coding: utf-8 -*-
# python with regexper
# update:2019.9
import re

testurl = "<img src=\"xxxxx\" alt=\"set\" /> <img src='ss' /img>"


def getImgUrl(url):
    imgget = r"<img(.*?)(\/>|><\/img>|>)" 
    srcGet = r"(src\s*?=\s*?)(\"|\')(.*?)(\"|\')"
    # not suggested
    regex=re.compile(imgget)
    print (regex.search(url).group(1))                          # result: src="xxxxx" alt="set" 
    
    # suggested
    all = re.findall(imgget, testurl, re.I|re.M)
    for single in all:
        print (single)
    '''result:
    (' src="xxxxx" alt="set" ', '/>')
    (" src='ss' /img", '>')
    '''

    # suggested
    srcfind = re.search(srcGet, regex.search(url).group(1))
    print (srcfind.group())                                     # result: src="xxxxx"


getImgUrl(testurl)


# re.match
print (re.match('p','python'))                                  # <_sre.SRE_Match object at 0x102bbdc60>
print (re.match("p",'www.tpyehon.com'))                         # None

'''
注：
Flags:
1).re.I(re.IGNORECASE): 忽略大小写
2).re.M(MULTILINE): 多行模式，改变’^’和’$’的行为
3).re.S(DOTALL): 点任意匹配模式，改变’.’的行为
4).re.L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
5).re.U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
6).re.X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释 

Methods:
1、match

    re.match(pattern, string[, flags])  
    从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。

2、search

    re.search(pattern, string[, flags])  
    若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个。

3、findall

    re.findall(pattern, string[, flags])  
    返回string中所有与pattern相匹配的全部字串，返回形式为数组。

4、finditer

    re.finditer(pattern, string[, flags])  
    返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。


若匹配成功，match()/search()返回的是Match对象，finditer()返回的也是Match对象的迭代器，
获取匹配结果需要调用Match对象的group()、groups或group(index)方法。
'''