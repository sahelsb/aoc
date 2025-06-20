def part1():
       
#     temp = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''
            
#     data = temp.split('\n')
#     print(data)

    with open ('./data/data7.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    sum = 0
    
    for equation in data:
        test_val = int(equation.split(':')[0])
        nums = [int(x) for x in equation.split(':')[1].split()]
        if check_results(nums, test_val):
            sum += test_val
    print(sum)
        
def check_results(nums, test_val):
    results = [nums[0]]
    nums = nums[1:]
    for num in nums:
        current_results = []
        for result in results:
            current_results.append(num * result)
            current_results.append(num + result)
            current_results.append(int(str(result) + str(num)))
        results = current_results
    if test_val in results:
        return True
    else:
        return False

def part2():
    
    with open ('./data/data7.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]

    sum = 0
    
    for equation in data:
        test_val = int(equation.split(':')[0])
        nums = [int(x) for x in equation.split(':')[1].split()]
        if check_results(nums, test_val):
            sum += test_val
    print(sum)
    
    
if __name__ == '__main__':
    part2() 
        
        