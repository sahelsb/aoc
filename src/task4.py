def part1():
    
    with open('./data/data4.txt', 'r') as f:
        
        data = [line.strip() for line in f.readlines()]
        
        count = 0 
        
        dirs = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
        
        for i in range(len(data)) :
            for j in range(len(data[i])) :
                if data[i][j] == 'X':
                    for dir in dirs:
                        if check_xmas(data, i, j, dir[0], dir[1]):
                            count += 1
                    
        
    print(count)
     
                    
                                      
def check_xmas(data, posx, posy, dirx, diry):
    
    word = ['M', 'A', 'S']

    if posx + dirx*3 < len(data[posx]) and posx + dirx*3 >=0 and posy +diry*3 < len(data[posy]) and posy + diry*3 >=0:
        for i in range(1,4):
            if data[posx + dirx*i][posy + diry*i] != word[i-1]:
                return False
        return True
                       
       
        
  
def part2():
    with open('./data/data4.txt', 'r') as f:
        
        data = [line.strip() for line in f.readlines()]
        
        count = 0 
        
        dirs = [(1, 1), (-1, 1)]
        
        for i in range(1,len(data)-1):
            for j in range(1,len(data[i])-1):
                if data[i][j] == 'A':
                    check = True
                    for dir in dirs:
                        if not check_x_mas(data, i, j, dir[0], dir[1]):
                            check = False
                    if check:
                        count += 1 
        print(count)     
  
def check_x_mas(data, posx, posy, dirx, diry):
    word = ['M', 'S']  
    
    if data[posx + dirx*1][posy + diry*1] != data[posx + dirx*(-1)][posy + diry*(-1)]:
        if data[posx + dirx*1][posy + diry*1] in word and data[posx + dirx*(-1)][posy + diry*(-1)] in word:
            return True     
        
if __name__=="__main__":
    part2()
    