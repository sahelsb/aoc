def part1():
    
    temp = '''....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...'''

    # data = [list(line) for line in temp.split('\n')]


    with open('./data/data6.txt') as f:
        data = [list(line.strip()) for line in f.readlines()]
    
    print(count_visited_positions(data))

def count_visited_positions(map):
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find the guard starting pos
    rows, cols = len(map), len(map[0])
    start_row, start_col, start_dir = None, None, None
    for r in range(rows):
        for c in range(cols):
            if map[r][c] in '^>v<':
                start_row, start_col = r, c
                if map[r][c] == '^':
                    start_dir = 0
                if map[r][c] == '>':
                    start_dir = 1
                if map[r][c] == 'v':    
                    start_dir = 2
                if map[r][c] == '<':
                    start_dir = 3
                break
        if start_row is not None:
            break

    current_row, current_col = start_row, start_col
    current_dir = start_dir
    visited_positions = set()
    visited_positions.add((current_row, current_col))

    while True:
        dr, dc = dir[current_dir]
        next_row, next_col = current_row + dr, current_col + dc

        # Check out of bounds
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break 

        if map[next_row][next_col] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            current_row, current_col = next_row, next_col
            visited_positions.add((current_row, current_col))

    return len(visited_positions)



      

    
if __name__ == '__main__':
    part1()