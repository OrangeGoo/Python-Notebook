age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)
### 退出提示
input("点击 enter 键退出")


# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")



num = int(input("输入一个数字"))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2，但不能整除3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")



def httpError(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
mystatus = 400
print(httpError(mystatus))