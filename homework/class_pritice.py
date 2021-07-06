
'''
写一个面向对象的例子：
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】
重写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=短毛
添加一个新的方法， 会捉老鼠，
重写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】
复写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=长毛
添加一个新的方法， 会看家
复写父类的【会叫】的方法，改成【汪汪叫】
'''

class Animal():

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def speak(self):
        self.voice = "叫"

    def run(self):
        self.move = "run"

class Cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = "short"

    def skill(self):
        self.skill1 = "catch mice"

    def speak(self):
        self.voice = "miao"

class Dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = "long"

    def skill(self):
        self.skill = "guard home"

    def speak(self):
        self.voice = "wang"

if __name__ == '__main__':

    daidai = Cat("袋袋", "blue", 2, "boy")
    daidai.run()
    daidai.skill()
    print(f"I have a cat called {daidai.name}, he is a {daidai.color} cat.He is {daidai.age} year old and he is a {daidai.gender}")
    print(f"{daidai.name} can {daidai.move} and {daidai.skill1}")
    print(f"{daidai.name} is a {daidai.hair} hair cat")

    ahuang = Dog("阿黄", "yellow", 3, "girl")
    ahuang.run()
    ahuang.skill()
    print(f"I have a cat called {ahuang.name}, he is a {ahuang.color} cat.He is {ahuang.age} year old and he is a {ahuang.gender}")
    print(f"{ahuang.name} can {ahuang.move} and {ahuang.skill}")
    print(f"{ahuang.name} is a {ahuang.hair} hair dog")

    daidai.speak()
    ahuang.speak()
    print(f"when they quarrel {daidai.name} say {daidai.voice}, {ahuang.name} say {ahuang.voice} ")
