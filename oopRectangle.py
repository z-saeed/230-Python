#oopRectangle.py
#Zaid Saeed
#11.6.14


class Rectangle(object):
    def __init__(self, width = 0, height = 0):
        object.__init__(self)
        self.setStats(width, height)

    def setArea(self, width, height):
        self.area = width * height

    def setPerimeter(self, width, height):
        self.perimeter = (2 * width) + (2 * height)

    def setStats(self, width, height):
        self.setArea(width, height)
        self.setPerimeter(width, height)

    def getStats(self):
        self.setStats(self.width, self.height)
        return "width:\t{}\nheight:\t{}\narea:\t{}\nperimeter:\t{}".format(self.width, self.height, self.area, self.perimeter)

def main():
    print ("Rectangle a:")
    a = Rectangle(5, 7)
    print ("area:      {}".format(a.area))
    print ("perimeter: {}".format(a.perimeter))
    
    print ("")
    print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print (b.getStats())

if __name__ == '__main__':
    main()