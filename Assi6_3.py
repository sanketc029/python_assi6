

class arithmatic:

    def __init__(self):
        self.val1=0
        self.valu2=0
        self.result=0

    def accept(self):
        self.val1=int(input("Enter the first no"))
        self.val2=int(input("Enter the second no"))

    def Addition(self):
        self.result=(self.val1 + self.val2)
        return(self.result)

    def Substraction(self):
        if self.val1 < self.val2:
            self.val1,self.val2=self.val2,self.val1
        self.result = (self.val1 - self.val2)
        return (self.result)

    def Multiplication(self):
        print(self.val1)
        self.result=(self.val1 * self.val2)
        return(self.result)

    def Division(self):
        print(self.val1)
        self.result=int(self.val1/self.val2)
        return(self.result)

    def print(self):
        print("Addition ",arithmatic.Addition(self))
        print("Substraction ",arithmatic.Substraction(self))
        print("Multiplication ", arithmatic.Multiplication(self))
        print("Division ", arithmatic.Division(self))

def main():
    print("After calling first object")
    obj1=arithmatic()
    obj1.accept()
    obj1.print()

    print("After calling second object")
    obj2 = arithmatic()
    obj2.accept()
    obj2.print()


if __name__=="__main__":
    main()





'''
    def Multiplication(self):
        if (self.val1== 0 and self.val2==0):
            self.val1=1
            self.val2=1
        elif self.val1==0:
            self.val1=1
        elif self.val2==0:
            self.val2=1
        self.result=(self.val1 * self.val2)
        return(self.result)

    def Division(self):
        if (self.val1== 0 and self.val2==0):
            self.val1=1
            self.val2=1
        elif self.val1==0:
            self.val1=1
            self.val1, self.val2 = self.val2, self.val1
        elif self.val2==0:
            self.val2=1
        elif self.val1< self.val2:
            self.val1, self.val2 = self.val2, self.val1
        self.result=(self.val1 // self.val2)
        return(self.result)
'''