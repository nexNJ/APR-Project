class Player():
    def __init__(self, name : str):
        self.name = name
        self.hp = 100
        self.exp = 0
        self.status = "awake"
    def attack(self,another):
        if another.status == "asleep":
            another.hp -= 20
        else:
            if self.exp > another.exp :
                another.hp -= 10
            else:
                self.hp -= 10
                self.exp += 10
        another.exp += 10 
    def sleep(self):
        self.status = "sleep"
        self.hp += 20
        if self.hp >= 100:
            self.hp =100
        else:
            pass
    def __str__ (self):
        return self.name + " is " + self.status + " hp " + str(self.hp)


            
p1 = Player("JACK")
p2 = Player("SAM")

p1.attack(p2)
print(p1)