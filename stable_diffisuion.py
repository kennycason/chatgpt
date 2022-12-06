width = 10
height = 10
grid = [[0 for j in range(height)] for i in range(width)]
grid[width // 2][height // 2] = 1
iterations = 100
for i in range(iterations):
    next = [[0 for j in range(height)] for i in range(width)]
    for x in range(width):
        for y in range(height):
            sum = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        sum += grid[nx][ny]
            if sum == 3:
                next[x][y] = 1
            elif sum == 2:
                next[x][y] = grid[x][y]
    grid = next
for x in range(width):
    for y in range(height):
        print("O" if grid[x][y] == 1 else ".", end="")
    print()