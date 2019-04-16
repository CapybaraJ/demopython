# coding: utf-8
# File Operation Demo
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
    file.close()

def readbylines(filename):
    cfile = open(filename, 'r') 
    for line in file.readlines():
        line=line.strip('\n')
        pass
    file.close()

