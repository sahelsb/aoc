def part1():
    
    rules, pages = setup()
    
    sum = 0
    for page in pages:
        print(page)
        if rules_met(page, rules):
            sum += int(page[len(page) // 2])

    print(sum)
    

def setup():
    with open ('./data/data5.txt', 'r') as f:
        data = f.read()
    
    first = data.split('\n\n')[0]
    second = data.split('\n\n')[1]

    rules = {}
    for line in first.split('\n'):
        if line.split('|')[1] in rules:
            rules[line.split('|')[1]].append(line.split('|')[0])
        else:
            rules[line.split('|')[1]] = [line.split('|')[0]]
    
    lines = second.splitlines() 
    pages = [line.split(',') for line in lines ]
    
    return rules, pages

def rules_met(page, rules):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if page[i] in rules and page[j] in rules[page[i]]:
                return False
    return True

            
# example = 5 | 3
# pages = [2,3,4,5,6,7]

if __name__ == "__main__":
    part1()