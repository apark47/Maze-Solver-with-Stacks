# lab04.py
from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return


def solveMaze(maze, startX, startY):
    s = Stack()
    count = 1

    if maze[startX][startY] == "G":
        return True

    maze[startX][startY] = count
    
    s.push([startX, startY])
           
    while s.size() > 0:
        pos = s.peek()

        x = pos[0]
        y = pos[1]
        

        if maze[x][y] == "G":
            return True

        # North
        if maze[x - 1][y] == " ":
            count += 1
            maze[x - 1][y] = count

            s.push([x - 1, y])
            continue

        if maze[x - 1][y] == "G":
            return True

        # West
        if maze[x][y - 1] == " ":
            count += 1
            maze[x][y - 1] = count

            s.push([x, y - 1])
            continue

        if maze[x][y - 1] == "G":
            return True

        # South
        if maze[x + 1][y] == " ":
            count += 1
            maze[x + 1][y] = count

            s.push([x + 1, y])
            continue

        if maze[x + 1][y] == "G":
            return True


        # East
        if maze[x][y + 1] == " ":
            count += 1
            maze[x][y + 1] = count

            s.push([x, y + 1])
            continue

        if maze[x][y + 1] == "G":
            return True

        else:
            s.pop()
            

    return False
