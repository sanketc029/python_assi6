

class circle:
    pi = 3.14

    def __init__(self):
        self.rad=0.0
        self.area=0.0
        self.circumfernce=0.0

    def accept(self):
        self.rad=int(input("Enter the radius"))

    def calArea(self):
        self.area=(self.rad ** 2) * circle.pi
        return(self.area)

    def calCircmference(self):
        self.circmference=(2*circle.pi)* self.rad
        return self.circmference

    def print(self):
        print("Aera of circle ",circle.calArea(self))
        print("Circumference of circle ",circle.calCircmference(self))

def main():
    print("After calling first object")
    obj1=circle()
    obj1.accept()
    obj1.print()

    print("After calling second object")
    obj2 = circle()
    obj2.accept()
    obj2.print()


if __name__=="__main__":
    main()