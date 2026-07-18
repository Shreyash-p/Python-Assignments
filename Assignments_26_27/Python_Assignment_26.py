class Demo:
    value = 11

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def Fun(self):
        print("Inside Fun")
        print(self.no1, self.no2)

    def Gun(self):
        print("Inside Gun")
        print(self.no1, self.no2)


class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0


    def Accept(self):
        self.Radius = float(input("Enter the Radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius * self.Radius)
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")
        

class Arithmetic:
    def __init__(self):
        Value1 = 0
        Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the first number: "))
        self.Value2 = int(input("Enter the second number: "))
        
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed."
        
        return self.Value1 / self.Value2


def main():

    '''
    1: Write a Python program to implement a class named Demo with the following specifications:
    • The class should contain two instance variables: no1 and no2.
    • The class should contain one class variable named Value.
    • Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
    • Implement two instance methods:
    ◦ Fun() - displays the values of instance variables no1 and no2.
    ◦ Gun() - displays the values of instance variables no1 and no2.
        Create two objects of the Demo class as follows:
        Obj1 = Demo(11, 21)
        Obj2 = Demo(51, 101)
        Call the instance methods in the given sequence:
        Obj1.Fun()
        Obj2.Fun()
        Obj1.Gun()
        Obj2.Gun()
    '''
    print("-" * 35)
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

    '''
    2: Write a Python program to implement a class named Circle with the following requirements:
    • The class should contain three instance variables: Radius, Area, and Circumference.
    • The class should contain one class variable named PI, initialized to 3.14.
    • Define a constructor (__init__) that initializes all instance variables to 0.0.
    • Implement the following instance methods:
    ◦ Accept() - accepts the radius of the circle from the user.
    ◦ CalculateArea() - calculates the area of the circle and stores it in the Area variable.
    ◦ CalculateCircumference() - calculates the circumference of the circle and stores it in the Circumference variable.
    ◦ Display() - displays the values of Radius, Area, and Circumference.
    • Create multiple objects of the Circle class and invoke all the instance methods for each object.
    '''
    print("-" * 35)
    print("--- Circle 1 ---")
    c1 = Circle()
    c1.Accept()
    c1.CalculateArea()
    c1.CalculateCircumference()
    c1.Display()

    print("--- Circle 2 ---")
    c2 = Circle()
    c2.Accept()
    c2.CalculateArea()
    c2.CalculateCircumference()
    c2.Display()
    
    '''
    3: Write a Python program to implement a class named Arithmetic with the following characteristics:
    • The class should contain two instance variables: Value1 and Value2.
    • Define a constructor (__init__) that initializes all instance variables to 0.
    • Implement the following instance methods:
    ◦ Accept() - accepts values for Value1 and Value2 from the user.
    ◦ Addition() - returns the addition of Value1 and Value2.
    ◦ Subtraction() - returns the subtraction of Value1 and Value2.
    ◦ Multiplication() - returns the multiplication of Value1 and Value2.
    ◦ Division() - returns the division of Value1 and Value2 (handle division by zero properly).
    • Create multiple objects of the Arithmetic class and invoke all the instance methods.
    '''
    print("-" * 35)
    print("--- Arithmetic Object 1 ---")
    obj1 = Arithmetic()
    obj1.Accept()
    
    print(f"Addition       : {obj1.Addition()}")
    print(f"Subtraction    : {obj1.Subtraction()}")
    print(f"Multiplication : {obj1.Multiplication()}")
    print(f"Division       : {obj1.Division()}")

    print("--- Arithmetic Object 2 ---")
    obj2 = Arithmetic()
    obj2.Accept()
    
    print(f"Addition      : {obj2.Addition()}")
    print(f"Subtraction   : {obj2.Subtraction()}")
    print(f"Multiplication: {obj2.Multiplication()}")
    print(f"Division      : {obj2.Division()}")
    print("-" * 35)

if __name__ == "__main__":
    main()