def part1():
    with open('./data/data14.txt') as f:
        position = []
        velocity = []
        data = [line.strip() for line in f.readlines()]
        for line in data:
            pos = line.split(' ')[0].split('=')[1]
            vel = line.split(' ')[1].split('=')[1]
            
            # position.append((int(pos.split(',')[0]), int(pos.split(',')[1])))
            # velocity.append((int(vel.split(',')[0]), int(vel.split(',')[1])))
            
            position.append(tuple(map(int, pos.split(','))))
            velocity.append(tuple(map(int, vel.split(','))))
            
    seconds = 100
    width = 101
    height = 103
    for second in range(seconds):
        for i in range(len(position)):
            pos_x = position[i][0] + velocity[i][0]
            pos_y = position[i][1] + velocity[i][1]
            if pos_x < 0:
                pos_x = width - abs(pos_x)
            elif pos_x >= width:
                pos_x = pos_x - width
            if pos_y < 0:
                pos_y = height - abs(pos_y)
            elif pos_y >= height:
                pos_y = pos_y - height
        
            position[i] = (pos_x, pos_y)
    
    print(position)
    
    quadrant_count = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}
    for pos in position:
        x, y = pos
        if x < width // 2 and y < height // 2:
            quadrant_count['Q1'] += 1
        elif x > width // 2 and y < height // 2:
            quadrant_count['Q2'] += 1
        elif x < width // 2 and y > height // 2:
            quadrant_count['Q3'] += 1
        elif x > width // 2 and y > height // 2:
            quadrant_count['Q4'] += 1
        
    safety = quadrant_count['Q1'] * quadrant_count['Q2'] * quadrant_count['Q3'] * quadrant_count['Q4']
    print(f"Safety factor:{safety}")
                

if __name__=="__main__":
    part1()