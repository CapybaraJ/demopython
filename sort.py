#coding:utf-8



# before: d = {'d1':2, 'd2':4, 'd4':1,'d3':3,}
# after : 'd1':2, 'd2':4, 'd3':3, 'd4':1
def sortByKey(d):

    return sorted(d)
    '''
    for k in sorted(d):
        print(k,d[k])
    '''


# 利用value排序：__getitem__
# before: d = {'d1':2, 'd2':4, 'd4':1, 'd3':3,}
# after: 'd4':1, 'd1':2, 'd3':3, 'd2':4
def sortByValue(d):
    '''
    for k in sorted(d,key=d.__getitem__):
        print(k,d[k])
    '''
    return sorted(d, key=d.__getitem__)