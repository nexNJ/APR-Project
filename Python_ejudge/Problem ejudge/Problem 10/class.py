class color():
    def __init__(self,c : str):
        self.color = c
    def set_color(self,c):
        self.color = c
    def get_color(self):
        return self.color

class Circle(color):
    def __init__(self,c : str,r : int):
        super().__init__(c)
        self.radius = r
    def set_radius(self,r):
        self.radius = r
    def get_radius(self):
        return self.radius
    def get_area(self):
        return (3.14*(self.radius)* self.radius)

class Rectangel(color):
    def __init__(self, c: str, w : int, h : int):
        super().__init__(c)
        self.width = w
        self.height = h
    def get_area(self):
        return self.width * self.height
    def set_width(self,w):
        self.width = w
    def set_height(self,h):
        self.height = h
    def __str__(self):
        return "8"

rec1 = Rectangel("Red" , 15 , 15)

print(rec1.get_area())
rec1.set_height(121)
print(rec1.get_area())
        





