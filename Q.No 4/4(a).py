# Question 4
# a)
# You are given a 2D grid representing a maze in a virtual game world. The grid is of size m x n and consists of
# different types of cells:
# 'P' represents an empty path where you can move freely. 'W' represents a wall that you cannot pass through. 'S'
# represents the starting point. Lowercase letters represent hidden keys. Uppercase letters represent locked doors.
# You start at the starting point 'S' and can move in any of the four cardinal directions (up, down, left, right) to
# adjacent cells. However, you cannot walk through walls ('W').
# As you explore the maze, you may come across hidden keys represented by lowercase letters. To unlock a door
# represented by an uppercase letter, you need to collect the corresponding key first. Once you have a key, you can
# pass through the corresponding locked door.
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English
# alphabet in the maze. This means that there is exactly one key for each door, and one door for each key. The letters
# used to represent the keys and doors follow the English alphabet order.
# Your task is to find the minimum number of moves required to collect all the keys and reach the exit point. The
# exit point is represented by 'E'. If it is impossible to collect all the keys and reach the exit, return -1.
# Example:
# Input: grid = [ ["S","P","P","P"], ["W","P","P","E"], ["P","b","W","P"], ["P","P","P","P"] ]
# Input: grid = ["SPaPP","WWWPW","bPAPB"]
# Output: 8
# The goal is to Collect all key






from collections import deque

def min_steps_to_collect_all_keys(maze):
    rows = len(maze)
    cols = len(maze[0])

    target_keys = 0
    start_x = 0
    start_y = 0

    # Extract information from the maze
    for i in range(rows):
        for j in range(cols):
            cell = maze[i][j]
            if cell == 'S':
                start_x = i
                start_y = j
            elif cell == 'E':
                target_keys |= (1 << ('f' - ord('a')))  # Set the bit for the exit door
            elif 'a' <= cell <= 'f':
                target_keys |= (1 << (ord(cell) - ord('a')))  # Set the bit for the key


    queue = deque()  # Perform BFS traversal
    visited = [[[False] * (1 << 6) for _ in range(cols)] for _ in range(rows)]  # 1 << 6 represents the keys bitmask
    queue.append((start_x, start_y, 0, 0))  # (x, y, keys, steps)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, keys, steps = queue.popleft()

        if keys == target_keys:
            return steps  # All keys collected, return the steps

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != 'W':
                cell = maze[new_x][new_y]

                if cell == 'E' or cell == 'P' or ('a' <= cell <= 'f') or ('A' <= cell <= 'F' and (keys & (1 << (ord(cell) - ord('A')))) != 0):
                    new_keys = keys
                    if 'a' <= cell <= 'f':
                        new_keys |= (1 << (ord(cell) - ord('a')))  # Collect the key

                    if not visited[new_x][new_y][new_keys]:
                        visited[new_x][new_y][new_keys] = True
                        queue.append((new_x, new_y, new_keys, steps + 1))

    return -1  # All possible moves explored and keys not collected, return -1

# Example usage:
maze = [
    "SPaPP",
    "WWWPW",
    "bPAPB"
]
result = min_steps_to_collect_all_keys(maze)
print("The Minimum number of moves :", result)  # Output: 8