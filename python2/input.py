# coding: utf-8
# get a input from console
# update:2019.6

import os


str = raw_input("Enter your input: ")
print ("Received input is : ", str)


# input() 函数和raw_input() 函数基本能够互换。
# input会如果你的输入是一个有效的Python表达式，并返回运算结果。这应该是两者的最大差别。


str = input("Enter your input: ");
print "Received input is : ", str



'''
Enter your input: fdsfsd
('Received input is : ', 'fdsfsd')
Enter your input: 3+4
Received input is :  7
'''