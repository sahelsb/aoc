def part1():
    
    # temp = '2333133121414131402'
    # data = list(temp.strip())
    
    with open('./data/data9.txt') as f:
        data = f.read()
    data = list(data.strip())
        
    disk = organize_blocks(data)
    
    disk = move_blocks(disk)
    
    print(checksum_update(disk))
    
def part2():
    
    temp = '2333133121414131402'
    data = list(temp.strip())
    
    # with open('./data/data9.txt') as f:
    #     data = f.read()
    # data = list(data.strip())
        
    disk = organize_blocks(data) 
    
    free_blocks = count_free_blocks(disk)
    
    disk = move_files(disk, free_blocks)
    
    print(checksum_update(disk))
    
def count_free_blocks(disk):
    free_blocks = {}
    count = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            index = i
            count +=1 
        elif disk[i] != '.' and count != 0:
            if count not in free_blocks:
                free_blocks[count] = []
                free_blocks[count].append(index)
                count = 0
            else:
                free_blocks[count].append(index)
                count = 0
    return free_blocks


def move_files(disk, free_blocks):
    j = len(disk) -1
    file = []
    while j >= 0:
        if disk[j] != '.':
            while disk[j] in file or len(file) == 0:
                print('hey')
                print(disk[j])
                file.append(disk[j])
                print(file)
                j -= 1
            if len(file) in free_blocks:
                print(len(file))
                print(free_blocks)
                index = free_blocks[len(file)][0]
                print(index)
                disk[index:index+len(file)] = file
            j -=1
            file = []
    return disk

    
def move_blocks(disk):
    j = len(disk) -1
    for i in range(len(disk)):
        if disk[i] == '.':
            while j >= i:
                if disk[j] != '.':
                    disk[i] = disk[j]
                    disk[j] = '.'
                    j -= 1
                    break
                j -= 1
    return disk
    
def organize_blocks(data):
    disk = []
    current_pos = 0
    
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(int(data[i])):
                disk.append(current_pos) 
            current_pos += 1 
        if i % 2 == 1:
            num = data[i]
            for j in range(int(data[i])):
                disk.append('.')
    return disk    
    
def checksum_update(disk):
    i = 0
    sum = 0
    while disk[i] != '.':
        sum += disk[i]*i
        i += 1
    return sum
        
                
        
    

        
        
    
    
    
if __name__ == "__main__":
    part2()