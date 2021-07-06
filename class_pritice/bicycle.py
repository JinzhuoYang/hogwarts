'''
第一个类 Bicycle（自行车）类
run() 方法，打印骑行公里数，骑行距离可以通过参数传入
第二个类 EBicycle 继承自 Bicycle
volume（电量）属性
fill_charge(vol) 充电方法
run() 方法用于骑行,每骑行 10km 消耗电量 1 度
当电量消耗尽时调用 Bicycle 的 run 方法骑行
通过传入的骑行里程数，显示骑行结果
'''
class Bicycle:
    # 型号
    model = "26"

    # 骑行方法
    def run(self,km):
        print(f"骑行了{km}公里")

# 继承，把父类类名放到类名后面的括号中
class EBicycle(Bicycle):

    # 如果属性需要传参定义，就可以写到构造函数中
    def __init__(self,value):
        self.value = value

     # 充电方法
    def fill_charge(self,vol):
        self.value = self.value +vol
        if self.value > 30:
            print("充电过多，电瓶爆炸了")
        else:
            print(f"冲了{vol}度电，现在有{self.value}度电")

    def run(self,km):
        # 计算目前电量支持的里程数
        power_km = self.value * 10
        if power_km >= km:
            print(f"用电骑行了{km}km")
        else:
            print(f"用电骑行了{power_km}公里")
            print("没电了")
            #Bicycle().run(km - power_km)
            # 用继承关系调用父类方法
            super().run(km - power_km)


if __name__ == '__main__':
    bike = Bicycle()
    bike.run(10)
    ebike = EBicycle(10)
    ebike.fill_charge(20)
    ebike.run(500)

