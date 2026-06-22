import sys

def main():
    a = int(input("Enter a number : "))
    print("Value entered:", a)
    print("Data type:", type(a))
    print("Data memory location:", id(a))
    print("Size of data:", sys.getsizeof(a))

if __name__ == "__main__":
    main()