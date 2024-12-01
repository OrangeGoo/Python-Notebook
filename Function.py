# 计算面积函数
# def area(width, height):
#     return width * height

# def print_welcome(name):
#     print("Welcome", name)

# print_welcome("Runoob")

# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))