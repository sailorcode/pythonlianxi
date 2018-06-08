from functools import reduce
#----------高级特性,切片,迭代,列表生成式,迭代器
#[起始索引:结束索引:步长] 开始和结束索引不论正数开始还是倒数开始都是左闭右开
tuple1=(1,2,3,4,5,6,7)
list1=[1,2,3,4,5,6,7]
str1='helloWord'
print(tuple1[1::2])
print(list1[1::2])
print(str1[1::2])
print(isinstance('a',str))
if 9 in list1:
    print(True)

d = {'a': 1, 'b': 2, 'c': 3}
#列表生成式
print([a+str(b)+'' for a,b in d.items()])
#双层循环生成list
print([m + n for m in 'ABC' for n in 'XYZ'])
#同时迭代list的索引和元素
for i,value in enumerate(list1):
    print(i,value)

#generator
#第一种方法,把一个列表生成式的[]改成()，就创建了一个generator
first_generator=(x for x in range(3))
for v in first_generator:
    print('第一个generator'+str(v))
#第二种方法,使用yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f=fib(3)
for v in f:
    print(v)
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


#map  第一个参数是函数,第二个参数是  map(func, *iterables)
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(a):
    return DIGITS[a]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#测试
print(str2int('123'))
print('s' and '2')








