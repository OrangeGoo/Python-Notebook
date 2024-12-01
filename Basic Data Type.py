print("Hello,Python")

counter = 100
miles = 1000.0
name = "runobb"

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1

a, b, c = 1, 2, "runobb"

# 标准数据类型
# Python3中常见的数据类型有：Number，String，bool，List（列表），Tuple（元祖），Set（集合），Dictionary（字典）
# Python3的六个标准数据类型中：不可变数据：Number，String，Tuple；可变数据：List，Set，Dictionary

a = 20
print(type(a))

a = 111
print(isinstance(a, int))

# instance和type的区别在于：
# type（）不会认为子类是一种父类类型
# isinstance（）会认为子类是一种父类类型

# 返回整数部分
# 在混合计算时，Python会把整型转换成为浮点数
print(5 // 4)

string = 'Runoob'
print(string)
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符

print('Ru\noob')
print(r'Ru\noob')

# 另外，反斜杠可以作为续航符，表示下一行是上一行的延续。也可以使用"""或'''跨越多行
# 注意，Python没有单独的字符类型，一个字符就是长度为1的字符串。

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
# 字符串可以用+运算符连接在一起，用*运算符重复
# Python中的运算符有两种索引方式，从左往右以0开始，从右往左以-1开始
# Python中的字符串不能改变

print(True and False)
print(True or False)
print(not True)



list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表
tinylist = [123, 'runoob']

print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist)  # 打印两个列表拼接在一起的结果



tuple = ('abcd', 786 , 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组



sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素



dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值