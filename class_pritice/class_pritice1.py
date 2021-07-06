class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def set_att(self,value):
        self.value = value

    def eat(self):
        print(f" name : {self.name}, age : {self.age}, gender : {self.gender} i'm eat")

    def drink(self):
        print(f" name : {self.name}, age : {self.age}, gender : {self.gender} i'm drink")

    def run(self):
        print(f" name : {self.name}, age : {self.age}, gender : {self.gender} i'm run")

goulin = person("goulin" , 25 ,"femail")
yangjinzhuo = person("yangjinzhuo" , 24 , "mail")

print(goulin.name)
goulin.run()

goulin.set_att("fat")
print(goulin.value)