import re

class Maze:
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr)
        self.M = len(arr[0]) if self.N > 0 else 0
    
    def get_moves(self, position):
        x,y = position
        moves = []
        if y < self.N and self.check_square(x,y+1):
            moves.append((x, y+1))
        if y > 1 and self.check_square(x,y-1):
            moves.append((x, y-1))
        if x < self.M and self.check_square(x+1,y):
            moves.append((x+1, y))
        if x > 1 and self.check_square(x-1,y):
            moves.append((x-1, y))     
        return moves     
    
    def check_square(self, x,y):
        return True if self.arr[y-1][x-1] == 1 else False 
    
    def find_path(self, position, visited):
        if position == (self.M, self.N):
            return True
        visited.add(position)
        available_moves = self.get_moves(position)
        for move in available_moves:
            if move not in visited:
                if self.find_path(move, visited):
                    return True
        return False  
            
s = input()
# Extract all substrings inside brackets
rows = re.findall(r"\[(.*?)\]", s)
for i,row in enumerate(rows):
    try:
        rows[i] = [int(x) for x in row.split(",")]
    except ValueError:
        rows[i] = []

maze = Maze(rows)
if maze.N > 0 and maze.M > 0 and maze.check_square(1,1):
    print(maze.find_path((1,1), set()))
else:
    print(False)
