import math
import re

import numpy as np


def part1():
    
#     data = '''Button A: X+94, Y+34
#               Button B: X+22, Y+67
#               Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
#     '''
    
    with open('./data/data13.txt') as f:
        data = f.read()
    
        
    machines = data.split('\n\n')
    x_ptrn = r"X\+(\d+)"
    y_ptrn = r"Y\+(\d+)"
    prize_ptrn = r"X=(\d+), Y=(\d+)"
    tokens = 0
    
    for machine in machines:
        x = []
        y = []
        coefficient = []
        constant = None
        x = re.findall(x_ptrn, machine)
        y = re.findall(y_ptrn, machine)
        coefficient.append(x)
        coefficient.append(y)
        print(coefficient)
        constant = re.findall(prize_ptrn, machine)
        print(constant)
        
        coefficient = [[int(x), int(y)] for x, y in coefficient]
        constant = list(map(int, constant[0]))
        
        print(coefficient)
        print(constant)
        
        tokens = solve(coefficient, constant)
        print(f"tokens: {tokens}")
            
        
def solve(coefficient, constant):
    x = np.linalg.solve(coefficient, constant)
    print(x[0], x[1])
    if x[0] <= 100 and x[1] <= 100 and math.isclose(x[0], round(x[0]), abs_tol=0.0001) and math.isclose(x[1], round(x[1]), abs_tol=0.0001):
        print(f"solution is {x}")
        tokens += x[0] * 3 + x[1]
        print(f"Tokens:{tokens}")
    else:
        print("No solution")  
    return tokens


def part2():
    
    data = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279'''

    # with open('./data/data13.txt') as f:
    #     data = f.read()
    
        
    machines = data.split('\n\n')
    x_ptrn = r"X\+(\d+)"
    y_ptrn = r"Y\+(\d+)"
    prize_ptrn = r"X=(\d+), Y=(\d+)"
    tokens = 0
    
    for machine in machines:
        x = []
        y = []
        coefficient = []
        constant = None
        error = 10000000000000
        
        x = re.findall(x_ptrn, machine)
        y = re.findall(y_ptrn, machine)
        coefficient.append(x)
        coefficient.append(y)
        print(coefficient)
        constant = re.findall(prize_ptrn, machine)
        print(constant)
        
        coefficient = [[int(x), int(y)] for x, y in coefficient]
        constant = list(map(int, constant[0] ))
        constant = [const + error for const in constant]    
        
        print(coefficient)
        print(constant)
        
        x = np.rint(np.linalg.solve(coefficient, constant))
        print(x[0], x[1])
        print(round(x[0]), round(x[1]))
        if np.all(coefficient @ x == constant):
            print(f"solution is {x}")
            tokens += x[0] * 3 + x[1]
        else:
            print("No solution")  
        print(f"tokens: {tokens}")
    
           
        
if __name__ == "__main__":
    # part1()
    part2()
        
    