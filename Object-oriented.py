class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print(f"{self.name}说，我{self.age}岁。")

# 实例化类
p = people('runoob', 10, 30)
p.speak()



#单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        #调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print(f"{self.name}说: 我{self.age}岁了, 我在读${self.grade}年级")

s = student('ken', 10, 60, 3)
s.speak()


#另一个类，多继承之前的准备
class speaker:
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print(f"我叫{self.name}，我是一个演说家，我演讲的主题是 {self.topic}")

#多继承
class sample(speaker,student):
    a =''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, "Python")
test.speak()   #方法名同，默认调用的是在括号中参数位置排前父类的方法



class Parent:        # 定义父类
    def myMethod(self):
      print ('调用父类方法')

class Child(Parent): # 定义子类
    def myMethod(self):
      print ('调用子类方法')

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child, c).myMethod() #用子类对象调用父类已被覆盖的方法



class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private

    def who(self):
        print('name: ', self.name)
        print('url: ', self.__url)

    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
x.__foo()      # 报错




class Vector:
  def __init__(self, a, b):
      self.a = a
      self.b = b

  def __str__(self):
      return f'Vector ({self.a}, {self.b})'

  def __add__(self, other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print (v1 + v2)