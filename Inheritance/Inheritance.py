class Shape:
    def __init__(self, color:str= "green", filled:bool= True):
        self.color = color
        self.filled = filled

    def setFilled(self, filled:bool):
        self.filled = filled

    def FILLED(self):
        return self.filled

    def getColor(self):
        return self.color

    def setColor(self, co:str):
        self.color = co

    def toString(self):
        x=""
        if self.FILLED() == True:
            x ="A Shape with color of "+self.color+" and filled"
        elif self.FILLED() == False:
            x = "A Shape with color of "+self.color+" and Not filled"
        return x

class Circle(Shape):
    def __init__(self, radius:float=1.0):
        Shape. __init__(self)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, ra):
        self.radius = ra

    def getArea(self):
        return (3.14*(self.radius**2))

    def getPerimeter(self):
        return (3.14*self.radius*2)

    def toString(self):
        x= Shape.toString(self)
        return "A Circle with radius="+str(self.radius)+", which is a subclass of "+str(x)

class Rectangle(Shape):
    def __init__(self, width:float=1.0,length:float=1.0):
        Shape. __init__(self)
        self.width = width
        self.length = length

    def getWidth(self):
        return self.width

    def setWidth(self, wi):
        self.width = wi

    def getLength(self):
        return self.length

    def setLength(self, le):
        self.length = le

    def getArea(self):
        return (self.length*self.width)

    def getPerimeter(self):
        return ((self.width*2)+(self.length*2))

    def toString(self):
        x= Shape.toString(self)
        return "A Rectangle with width="+str(self.width)+" and length="+str(self.length)+", which is a subclass of "+str(x)

class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)
        self.width = self.length
    def setLength(self, Side:float):
        self.width = self.length = Side
    def setWidth(self, Side:float):
        self.width = self.length = Side
    #I do not need to overwrite the gettArea/getPerimetere
    def toString(self):
        x= Shape.toString(self)
        return "A Square with side="+str(self.width)+", which is a subclass of "+str(x)

if __name__ == '__main__':
    mah = Circle("Rad",True)
    print(mah.toString())

    mah.setFilled(False)
    print(mah.FILLED())

    mah.setColor("Red")
    print(mah.getColor())

    print(mah.toString())

