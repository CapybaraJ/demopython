# coding: utf-8
# File Operation Demo
# update:2019.4
import io
'''
'r'：read
'w'：write
'a'：add to the end
'r+' == r+w（file not exist: IOError）
'w+' == w+r（file auto create if not exist）
'a+' == a+r（file auto create if not exist）
To read/write binary file，just add b：
'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
'''


def readfile(filename):
    cfile = open(filename, 'r') 
    for line in cfile:
        pass # do something
    cfile.close()


def readline(filename):
    cfile = open(filename, 'r') 
    for line in cfile.readlines():
        line=line.strip('\n')
        pass
    cfile.close()

def nocloseread(filename):
    with io.open(filename, "r", encoding="utf-8") as f:         # chose the encoding type
        for line in f:
            line=line.strip('\n')
            pass
    # no need to close;