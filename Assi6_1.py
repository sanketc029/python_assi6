
class Demo:
    def __init__(self,no1,no2):
        self.val1=no1
        self.val2=no2

    def fun(self):
        print("Inside Fun ")
        print(self.val1)
        print(self.val2)

    def gun(self):
        print("Inside Gun ")
        print(self.val1)
        print(self.val2)


def main():
    obj1=Demo(11,23)
    obj2=Demo(45,89)

    print("After calling first object :")
    obj1.fun()
    obj1.gun()

    print("After calling second object :")
    obj2.fun()
    obj2.gun()


if __name__=="__main__":
    main()