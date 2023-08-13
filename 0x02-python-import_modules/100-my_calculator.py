#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add as addition, sub as subtraction, mul as multiplication, div as division

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <num1> <operator> <num2>")
        exit(1)
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        operator = sys.argv[2]
        
        if operator == '+':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif operator == '-':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif operator == '*':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif operator == '/':
            print(f"{num1} / {num2} = {division(num1, num2)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
