# This is my first python program that ask you for a number and print the following
# Its multiplication table upto 15
#Factorial
#Square
#Cube
#Prime or not
#binary representation
#Octal representation
#Hexal representation
# This is written using Class of python
import sys
sys.setrecursionlimit(10**6)# the setrecursionlimit function is used to modify the default recursion to avoid stack overflow

class Numberphile:
    def tables(obj, n):  # Method  for Multiplication table
        print("Multiplication table of ", n, "is below")
        for i in range(1, 16, 1):
            result = n * i
            print(n, " x ", i, " = ", result)

    def fact(self, n):  # Method for Factorial
        if n < 6000: #Number greater than this will cause stack overflow with the given recursion limit
            if n == 0:
                return 1
            else:
                return n * self.fact(n - 1)  # Using recursion for a factorial
        else:
            return 'stack_error'

    def prime(self,n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    print(n, "is not a prime number", "\n")
                    break
            else:
                print(n, "is a prime number", "\n")
        else:
            print(n, "is not a prime number", "\n")

    def squr(self, n):  # Method for Square
        print("Square of ", n, "is", n * n, "\n")

    def cube(self, n):  # Method for Square
        print("Cube of ", n, "is", n * n * n, "\n")

    def binary(self, n):  # Method for Binary representation
        print("Binary representation of ", n, "is :", bin(n), "\n")

    def octal(self, n):  # Method for Octal representation
        print("Octal representation of ", n, "is :", oct(n), "\n")

    def hexal(self, n):  # Method for Hexa representation
        print("Hexa representation of ", n, "is :", hex(n), "\n")


try:
    n = int(input("Which number Multiplication table you want?"))
    Num_object = Numberphile()  # Object for the class Numberphile

    Num_object.squr(n)
    Num_object.cube(n)
    Num_object.prime(n)
    Num_object.binary(n)
    Num_object.octal(n)
    Num_object.hexal(n)
    Fact_result = Num_object.fact(n)
    if Fact_result == 'stack_error':
        print("Factorial of ", n, "cannot be displayed")
    else:
        print("Factorial of", n, "is :", Fact_result, "\n")
    Num_object.tables(n)
except ValueError as e:
    print("Input only number", "\n\n")
except Exception as e:
    print("Something went wrong.... brief info => ", e, "\n\n")
