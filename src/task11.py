def part1():
    with open('./data/data11.txt') as f:
        data = f.read()
    
    stones = [int(x) for x in data.split(' ')]
    print(stones)
    blinks = 25
    
    for i in range(blinks):
        stones = rearrange(stones) 
        print(stones) 
    
    
def part2():
    with open('./data/data11.txt') as f:
        data = f.read()
    
    data = [int(x) for x in data.split(' ')]
    blinks = 75
    
    stones = {}
    for stone in data:
        stones[stone] = stones.get(stone, 0) + 1
        
    for i in range(blinks):
        stones = rearrange2(stones)  
        
    print(sum(stones.values()))
    
def rearrange2(stones: dict):
    counter = {}
    for stone, count in list(stones.items()):
        if stone == 0:
            counter[1] = counter.get(1,0) + count
        elif count_digits(stone) % 2 == 0:
            part1 = stone // (10 ** (count_digits(stone) // 2))
            part2 = stone %  (10 ** (count_digits(stone) // 2))
            counter[part1] = counter.get(part1, 0) + count
            counter[part2] = counter.get(part2, 0) + count
        else:
            new_stone = stone * 2024
            counter[new_stone] = counter.get(new_stone, 0) + count
    return counter
            
def rearrange(stones: list):
    new = []
    for stone in stones:
        if stone == 0:
            new.append(1)
        elif count_digits(stone) % 2 == 0:
            part1 = stone // (10 ** (count_digits(stone) // 2))
            part2 = stone %  (10 ** (count_digits(stone) // 2))
            new.append(part1)
            new.append(part2)
        else:
            new.append(stone * 2024)
    return new
    
            
def count_digits(x: int):
    count = 0
    if x == 0:
        count += 1
    while x != 0:
        x  = x // 10
        count += 1 
    return count


if __name__ == "__main__":
    # part1()
    part2()