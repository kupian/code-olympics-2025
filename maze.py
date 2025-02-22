import re

class Maze:
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr)
        self.M = len(arr[0])
    
    def get_moves(self, x, y):
        moves = []
        if y < self.N and self.check_square(x,y+1):
            moves.append((x, y+1))
        if y > 0 and self.check_square(x,y-1):
            moves.append((x, y-1))
        if x < self.M and self.check_square(x+1,y):
            moves.append((x+1, y))
        if x > 0 and self.check_square(x-1,y):
            moves.append((x-1, y))     
        return moves     
    
    def check_square(self, x,y):
        return True if self.arr[y-1][x-1] == 1 else False 
    
    def find_path(self, position, previous):   
        available_moves = self.get_moves(position).remove(previous)
        if len(available_moves) == 0:
            return False
        elif (self.N, self.M) in available_moves:
            return True
        else:
            return any(find_path(move, position) for move in available_moves)  
            
s = input()
# Extract all substrings inside brackets
rows = re.findall(r"\[(.*?)\]", s)
for i,row in enumerate(rows):
    rows[i] = [int(x) for x in row.split(",")]

maze = Maze(rows)
position = (0,0)
maze.find_path(position, None)
            