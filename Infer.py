names = ['Bob', 'Tom', 'Alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 0]
print(new_names)

listDemo = ['Google', 'Runnob', 'Taobao']
newdict = {key: len(key) for key in listDemo}
print(newdict)

setNew = {i ** 2 for i in (1, 2, 3)}
print(setNew)

a = (x for x in range(1, 10)) # 返回生成器对象
tuple(a) # 将生成器对象转换成元祖