# -*- coding: utf-8 -*-
# Deal writing ditc/list into file
# update:2019.9
import json

# repo : https://www.cnblogs.com/yanwuliu/p/9593826.html
dictObj = {
	"class_name": 20140406,
	"stu_info": 
	[
	  	{
			"id": 309, "name": "小白", "sex":"不详",
		},
		{
			"id": 310, "name": "小白", "sex": "男",
		}
	]
}
print (dictObj['stu_info'])                                                 # is a dict
jsObj = json.dumps(dictObj, indent=2, ensure_ascii=False)                   # is a string
with open('jsonFile.json','w') as f:
    f.write(jsObj)

with open('jsonFile.json','r') as f:
    content = f.read()                      # is a string
    user_dic=json.loads(content)            # is a dict
    print(str(user_dic['stu_info']).encode('utf-8').decode('unicode_escape'))
    '''result:
    [{u'id': 309, u'name': u'小白', u'sex': u'不详'}, {u'id': 310, u'name': u'小白', u'sex': u'男'}]
    '''

'''注：
load/loads
loads()传的是字符串，而load()传的是文件对象
使用loads()时需要先读文件再使用，而load()则不用

dump/dumps
.dump()不需要使用.write()方法，只需要写哪个字典、哪个文件即可；而.dumps()需要使用.write()方法写入
如果要把字典写到文件里面的时候，dump()好用；但如果不需要操作文件，或需要把内容存到数据库和Excel，则需要使用dumps()先把字典转成字符串，再写入

ensure_ascii=False #为False时内容输出显示正常的中文，而不是转码
indent= #使用参数indent，为字符串换行+缩进;可以理解为格式化输出
'''