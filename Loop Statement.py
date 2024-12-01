count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

sites = ["Baidu", "Google", "Runnob", "Taobao"]
for site in sites:
    print(site)


'''
在Python中，for...else语句用于在循环结束后执行一段代码
当循环执行完毕（即遍历完iterable中的所有元素）后，会执行else字句中的代码，如果在循环过程中遇到了break语句，则会中断循环，此时不会执行else子句
'''

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


a = ['Google', 'Baidu', 'Runoob', 'Taobao' ,'QQ']
for i in range(len(a)):
    print(i, a[i])


a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
