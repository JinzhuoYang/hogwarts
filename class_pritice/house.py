# 定义类
class House:
    # 静态属性
    door = ""
    floor = ""

    # 构造函数
    def __init__(self,door,floor):
        # print("构造函数")
        # 在构造函数中定义实例变量,在类实例化的时候先执行
        self.kichen = "cook"
        self.door = door
        self.door = floor

    # 动态方法
    def sleep(self):
        bed = "bid bed"    # 局部变量：在类的方法当中，不以self.开头
        self.table = "something can put on the table"     # 实例变量，在类的方法中，以self.开头，作用于类当中所有的方法
        print(f"sleep in the house,and on the {bed}")

    def cook(self):
#        print(self.table)     # 在其他方法中调用实例变量‘\
        print(self.kichen)    # 调用构造函数的变量
        print("cook in the house")

# 实例化:变量（实例） = 类名（）
north_house = House()
china_house = House()

# 定义北欧风房子的属性
north_house.door = "whith"
north_house.floor = "black"

# 定义中式风房子的属性
china_house.door = "yellow"
china_house.floor = "red"

north_house.cook()
# 调用类的属性
door = House.door
print(door)

# House.door = "blue"
# print(House.door)  #类里面的值会改变但是不影响到实例中的值