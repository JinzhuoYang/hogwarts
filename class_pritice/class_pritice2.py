class pet:
    # 名字
    name = ""
    # 品种
    variety = ""
    # 性格
    character = ""

    def set_name(self,name):
        self.name = name
        print(f"宠物名字是:{self.name}")

    def set_variety(self,variety):
        self.variety = variety
        print(f"宠物的品种是：{self.variety}")

    def set_character(self,character):
        self.character = character
        print(f"宠物的性格是：{self.character}")

# 对象
daidai = pet()
daidai.set_name("袋袋")
daidai.set_variety("cat")
daidai.set_character("lazy")

aoliao = pet()
aoliao.set_name("奥利奥")
aoliao.set_variety("cat")
aoliao.set_character("cool")

dafu = pet()
dafu.set_name("大福")
dafu.set_variety("pig")
dafu.set_character("stupid")

