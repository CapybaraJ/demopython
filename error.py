# -*- coding: utf-8 -*-
# try except deal the error
# update:2019.9
import requests
import io
import re
import time


def fileioError():
    try:
        imgcontent = open('test.txt', 'rb')
    except IOError:
        print ("Error: No Such File or Reading is not Permitted !!!!!!!")
    else:
        # No Error
        # Good!
        pass
            


def requestError():
    try:
        # 以下except都是用来捕获当requests请求出现异常时，
        # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
        response = requests.get("https://www.baidu.com")
    # 常见错误
    except requests.exceptions.ConnectionError:
        print('ConnectionError -- please wait 3 seconds')   
        time.sleep(3)
    except requests.exceptions.ChunkedEncodingError:
        print('ChunkedEncodingError -- please wait 3 seconds')   
        time.sleep(3)    
    except:
        print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')   
        time.sleep(3)
    else:
        # No Error
        # Good!
        pass

