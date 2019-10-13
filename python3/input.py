# coding: utf-8
# get a input from console
# update:2019.6
import sys

# Python3将raw_input和input进行整合成了input....去除了raw_input()函数....

# 其接受任意输入, 将所有输入默认为字符串处理,并返回字符串类型

def getraw():
    str = input("Enter your input: ")
    print ("Received input is : ", str)

    '''
    Enter your input: 3+5
    Received input is :  3+5
    '''

# sys.stdin的方法得到输入
# in cannot work in python2
def getstdin():
    for line in sys.stdin:
        print (line)
        a = line.split()
        print(a)


# sys.stdin的另一种方法
# it can work in python2
def getstdins():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        print (values)

getstdins()