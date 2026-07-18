class BookStore:
    NoOfBooks = 0

    def __init__(self, a, b):
        self.Name = a
        self.Author = b
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")

class BankAccount:
    ROI = 10.5

    def __init__(self, name, initial_amount):
        self.Name = name
        self.Amount = float(initial_amount)

    def Display(self):
        print(f"Account Holder : {self.Name}")
        print(f"Current Balance: {self.Amount:.2f}")

    
    def Deposit(self, amount):
        self.Amount = self.Amount + amount
        print(f"Successfully deposited ${amount:.2f}")
        
    def Withdraw(self, AmountToWithDraw):
        if self.Amount > AmountToWithDraw:
            self.Amount = self.Amount - AmountToWithDraw
            print(f"Successfully withdrew ${AmountToWithDraw:.2f}")
        else:
            print(f"Transaction Denied: Insufficient balance. \nAttempted to withdraw {AmountToWithDraw:.2f}")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100

        return Interest
    

class Numbers:
    def __init__(self, a):
        self.Value = a

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        lst = []
        if self.Value <= 0:
            print(f"Factors of {self.Value}: None")
            return
            
        print(f"Factors of {self.Value}: ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                lst.append(i)
        print(lst)

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum = sum + i
        return sum

    def ChkPerfect(self):
        # A perfect number equals the sum of its proper positive divisors (excluding itself)
        if self.Value <= 1:
            return False
        
        # Sum of proper divisors = total sum of factors minus the number itself
        proper_sum = self.SumFactors() - self.Value
        return proper_sum == self.Value


def main():
    '''
    1: Write a Python program to implement a class named BookStore with the following specifications:
    • The class should contain two instance variables:
    ◦ Name (Book Name)
    ◦ Author (Book Author)
    • The class should contain one class variable:
    ◦ NoOfBooks (initialize it to 0)
    • Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
    • Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
    • Implement an instance method:
    ◦ Display() - should display book details in the format:
    <BookName> by <Author>. No of books: <NoOfBooks>

    Example usage:
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display() # Linux System Programming by Robert Love. No of books: 1
    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2
    '''
    print("-" * 35)
    print("\n--- BookStore Obj 1 ---")
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    print("\n--- BookStore Obj 2 ---")
    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()

    '''
    2: Write a Python program to implement a class named BankAccount with the following requirements:
    • The class should contain two instance variables:
    ◦ Name (Account holder name)
    ◦ Amount (Account balance)
    • The class should contain one class variable:
    ◦ ROI (Rate of Interest), initialized to 10.5
    • Define a constructor (__init__) that accepts Name and initial Amount.
    • Implement the following instance methods:
    ◦ Display() - displays account holder name and current balance
    ◦ Deposit() - accepts an amount from the user and adds it to balance
    ◦ Withdraw() - accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
    ◦ CalculateInterest() - calculates and returns interest using formula:
        Interest = (Amount * ROI) / 100
    • Create multiple objects and demonstrate all methods.
    '''
    print("-" * 35)
    print("\n--- BankAccount Obj 1 ---")
    account1 = BankAccount("Rohit Patil", 1000.0)
    account1.Display()
    account1.Deposit(500.0)
    account1.Withdraw(200.0)
    account1.Display()

    interest_earned1 = account1.CalculateInterest()
    print(f"Expected Interest Earned at {BankAccount.ROI}% ROI: ${interest_earned1:.2f}")

    print("\n--- BankAccount Obj 2 ---")
    account2 = BankAccount("Somnath Patil", 250.0)
    account2.Display()
    
    account2.Withdraw(300.0) 
    account2.Deposit(100.0)
    account2.Withdraw(50.0)
    account2.Display()
    
    interest_earned2 = account2.CalculateInterest()
    print(f"Expected Interest Earned at {BankAccount.ROI}% ROI: ${interest_earned2:.2f}")

    '''
    3: Write a Python program to implement a class named Numbers with the following specifications:
    • The class should contain one instance variable:
    ◦ Value
    • Define a constructor (__init__) that accepts a number from the user and initializes Value.
    • Implement the following instance methods:
    ◦ ChkPrime() - returns True if the number is prime, otherwise returns False
    ◦ ChkPerfect() - returns True if the number is perfect, otherwise returns False
    ◦ Factors() - displays all factors of the number
    ◦ SumFactors() - returns the sum of all factors
    • Create multiple objects and call all methods.
    '''
    print("-" * 35)
    print("\n--- Numbers Obj 1 ---")
    print("Testing Number 11")
    num1 = Numbers(11)
    print("Is Prime:")
    print(num1.ChkPrime())
    num1.Factors()
    print("Sum of Factors:")
    print(num1.SumFactors())
    print("Is Perfect:")
    print(num1.ChkPerfect())

    print("\n--- Numbers Obj 2 ---")
    print("Testing Number 6")
    num2 = Numbers(6)
    print("Is Prime:")
    print(num2.ChkPrime())
    num2.Factors()
    print("Sum of Factors:")
    print(num2.SumFactors())
    print("Is Perfect:")
    print(num2.ChkPerfect())

if __name__ == "__main__":
    main()