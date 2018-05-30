print(len('中文'))
print('中文'.encode('utf-8'))
print(len('中文'.encode('utf-8')))
#list里可以放不同类型的数据
classmates = ['Michael', 'Bob', False,1]
print(len(classmates),classmates[0],classmates[-1])
#新增指定位置
classmates.insert(1,'qian')
#list末尾新增元素
classmates.append(['qian','wang'])
#删除,pop传的是索引,remove传的元素

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
