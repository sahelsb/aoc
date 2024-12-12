import re

def part1():
    
    with open('./data/data3.txt', 'r') as f:
        data = f.read()
        
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    muls = re.findall(pattern, data)
    
    sum = 0
    for mul in muls:
        nums = mul.replace("mul(", "").replace(")", "")
        num1, num2 = nums.split(",")
        sum += int(num1) * int(num2)
    
    print(sum)
    
def part2():
    with open('./data/data3.txt', 'r') as f:
        data = f.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    
    exps = re.findall(pattern, data)
    sum = 0
    mul = True
    
    for exp in exps:
        if re.fullmatch("do\(\)", exp):
            mul = True
        elif re.fullmatch("don't\(\)", exp):
            mul = False
        elif re.fullmatch("mul\(\d{1,3},\d{1,3}\)", exp) and mul:
            nums = exp.replace("mul(", "").replace(")", "")
            num1, num2 = nums.split(",")
            sum += int(num1) * int(num2)
            
    print(sum)
        
if __name__=="__main__":
    part2()
   
   
   
   
import re

def evaluate_corrupted_memory(memory_string):
    # Regex patterns to extract instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    
    # Initial state: mul is enabled
    mul_enabled = True
    total_sum = 0

    # Split the memory string into tokens based on recognized patterns
    tokens = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory_string)
    
    for token in tokens:
        if do_pattern.fullmatch(token):
            # Enable mul instructions
            mul_enabled = True
        elif dont_pattern.fullmatch(token):
            # Disable mul instructions
            mul_enabled = False
        elif mul_pattern.fullmatch(token) and mul_enabled:
            # Evaluate the mul instruction if enabled
            x, y = map(int, mul_pattern.match(token).groups())
            total_sum += x * y

    return total_sum

# Test with the given example
test_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
result = evaluate_corrupted_memory(test_memory)
result
 