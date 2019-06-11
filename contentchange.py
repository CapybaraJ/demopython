# coding: utf-8
# Change content in a file
# update:2019.6
# source: https://www.cnblogs.com/wc-chan/p/8085452.html
before = '''
This is a test file you can write anything here

abs.asset can be changed to abs??

 [abs.asset/ffffff](https://abs.assets / ffff)
'''


def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)



alter("contentchange.test.txt", "abs.asset", "abs")


after = '''
This is a test file you can write anything here

abs can be changed to abs??

 [abs/ffffff](https://abss / ffff)
'''