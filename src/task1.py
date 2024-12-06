from collections import Counter


def part1():
    with open("./data/data1.txt") as f:
        data = [l.strip() for l in f]
    
    first = []
    second = []
    diff = 0
    
    for line in data:
        first.append(int(line.split()[0]))
        second.append(int(line.split()[1]))
        
    sorted_first = sorted(first)
    sorted_second = sorted(second)
    
    for first,second in zip(sorted_first,sorted_second):
        diff += abs(first-second)
    print(diff) 
    
def part2():

    
    with open("./data/data1.txt") as f:
        data = [l.strip() for l in f]
    
        
    first = []
    second = []
    for line in data:
        first.append(int(line.split()[0]))
        second.append(int(line.split()[1]))
        
    count = {}
    # count = Counter(second)
    # for i in range(len(second)):
    #     count[second[i]] = count[second[i]] + 1 if second[i] in count else 1
    # print(count)
    
    # for e in second:
    #     count[e] = count[e] + 1 if e in count else 1

    for e in second:
        count[e] = count.get(e, 0) +1 
        
    similarity = 0  
    for e in first:
        similarity+= e * count.get(e, 0)
    
    print(similarity)
        
       
if __name__ == "__main__":        
    #part1()
    part2()
        