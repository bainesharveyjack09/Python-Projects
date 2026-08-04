from time import sleep as wait
import random
def choice():
    print("yo")
    wait(1)
    choice = input("add, subtract, divide or multiply?")
    match choice:
        case "add":
            ops("add")
        case "subtract":
            ops("minus")
        case "divide":
            ops("dive")
        case "multiply":
            ops("mult")
        
def ops(operation):
    op = operation
    fst_no = float(input("Input first number"))
    sec_no = float(input("Input second number"))
    match op:
        case "add":
            res = fst_no + sec_no
        case "minus":
            res = fst_no - sec_no
        case "dive":
            res = fst_no / sec_no
        case "mult":
            res = fst_no * sec_no
    print(f"Ur answer is {res}")
    input()
choice()
