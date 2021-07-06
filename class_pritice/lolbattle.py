'''
一个回合制游戏，有两个英雄，分别是 EZ 和 JINX。
每个英雄都有 hp 属性和 power 属性，分别代表血量和攻击力
EZ 初始值： hp，1100； power，190
Jinx 初始值： hp，1000； power，210
每个英雄都有一个 fight 方法：
hero_final_hp = hero_hp - enemy_power
enemy_final_hp = enemy_hp - hero_power
对比 hero_final_hp 和 enemy_final_hp，血量先为零的人输掉比赛
'''
import random


class Hero:

    def __init__(self, name, hp, power):
        #初始化英雄属性
        self.my_name = name
        self.my_hp = hp
        self.my_power = power

    # 打斗方法
    def fight(self, enemy_name, enemy_hp, enemy_power):
       # 比赛结果
        result = ""
        while True:
            self.my_hp = self.my_hp - enemy_power
            enemy_hp = enemy_hp - self.my_power
            print(f"我{self.my_name}的血量为：{self.my_hp}")
            print(f"敌人{enemy_name}的血量为：{enemy_hp}")
            # 判断输赢
            if self.my_hp > enemy_hp:
                result = "I WIN"
            elif self.my_hp < enemy_hp:
                result = "I LOSE"
            else:
                result = "平局"

            # 如果有人血量小于0跳出循环
            if enemy_hp <= 0 or self.my_hp <= 0:
                break

        return result
'''
后裔，后裔继承了 Hero 的 hp 和 power。并多了护甲属性。
重新定义另外一个 defense 属性：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个 hp 进行对比，血量先为零的人输掉比赛
'''
class HouYi(Hero):
    def __init__(self, name, hp, power):
        self.defensse = 100
        # 继承父类构造函数，父类构造函数中有传参，需要手动传进去
        super().__init__(name, hp, power)

    def fight(self, enemy_name, enemy_hp, enemy_power):
        # 比赛结果
        result = ""
        while True:
            self.my_hp = self.my_hp + self.defensse - enemy_power
            enemy_hp = enemy_hp - self.my_power
            print(f"我{self.my_name}的血量为：{self.my_hp}")
            print(f"敌人{enemy_name}的血量为：{enemy_hp}")
            # 判断输赢
            if self.my_hp > enemy_hp:
                result = "I WIN"
            elif self.my_hp < enemy_hp:
                result = "I LOSE"
            else:
                result = "平局"

            # 如果有人血量小于0跳出循环
            if enemy_hp <= 0 or self.my_hp <= 0:
                break

        return result

if __name__ == '__main__':
    # 定义英雄属性
    EZ_hp = 1100
    EZ_power = 190
    # Jinx_hp = 1000
    # Jinx_power = 210
    # 列表推导式
    hp = [x for x in range(990, 1010)]
    Jinx_hp = random.choice(hp)
    print(Jinx_hp)
    Jinx_power = random.randint(190, 210)
    # # 实例化英雄
    # ez = Hero("EZ", EZ_hp, EZ_power)
    # # 调用打斗方法
    # r = ez.fight("Jinx", Jinx_hp, Jinx_power)
    # # 打印比赛结果
    # print(r)
    houyi = HouYi("寒冰", 900, 220)
    r = houyi.fight("Jinx", Jinx_hp, Jinx_power)
    print(r)