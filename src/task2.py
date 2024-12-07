def part1():
    
    temp = '''7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9'''
    
    reports = temp.split('\n')
    
    
    # with open('./data/data2.txt') as f:
    #     reports = [line.strip() for line in f.readlines()]
        
    safe = 0

        
    for report in reports:
        report = report.split()
        if is_safe(report):
            safe += 1
            
    print(safe) 
    
    
def part2():
    
    # temp = '''7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9'''
    
    # reports = temp.split('\n')
    
    with open('./data/data2.txt') as f:
        reports = [line.strip() for line in f.readlines()]
        
    safe = 0
    for report in reports:
        report = report.split()
        if is_safe(report):
            safe += 1
        else:
            for j in range(len(report)):
                report_new = report[:j] + report[j+1:]
                if is_safe(report_new):
                    safe += 1
                    break
    print(safe)


def is_safe(report):
    decrease = True
    increase = True
    for i in range(1, len(report)):
        diff = int(report[i]) - int(report[i-1])
        if diff not in (1, 2, 3):
            increase = False
        if diff not in (-1, -2, -3):
            decrease = False
    return decrease or increase
           
        
if __name__ == "__main__":
    # part1()
    part2()