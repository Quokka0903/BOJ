maze = [['#'] * 101 for _ in range(101)]

x_here, y_here = 50, 50
max_x, min_x, max_y, min_y = 50, 50, 50, 50
maze[y_here][x_here] = '.'
direction = 3

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

N = int(input())
move = input()
for m in move :
    if m == 'L' :
        direction += 1
    elif m == 'R' :
        direction -= 1
    elif m == 'F' :
        x_here += di[direction % 4]
        y_here += dj[direction % 4]
        maze[y_here][x_here] = '.'

        if x_here > max_x :
            max_x = x_here
        elif x_here < min_x :
            min_x = x_here

        if y_here > max_y :
            max_y = y_here
        elif y_here < min_y :
            min_y = y_here

for i in range(min_y, max_y + 1) :
    print(''.join(maze[i][min_x : max_x + 1]))