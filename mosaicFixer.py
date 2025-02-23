import sys
import ast

board, changes = sys.stdin.read().strip(), 0
board = ast.literal_eval(board)
finishedBoard1 = []
finishedBoard2 = []
fixes1 = fixes2 = 0

for i in range(len(board)):
    finishedRow1 = []
    finishedRow2 = []
    for j in range(len(board[i])):
        if (i + j) % 2 == 0:
            correctColour1 = board[0][0]
            correctColour2 = "g" if board[0][0] == "o" else "o"
        else:
            correctColour1 = "g" if board[0][0] == "o" else "o"
            correctColour2 = board[0][0]
        
        if board[i][j] != correctColour1:
            fixes1 += 1
        if board[i][j] != correctColour2:
            fixes2 += 1
        
        finishedRow1.append(correctColour1)
        finishedRow2.append(correctColour2)
    
    finishedBoard1.append(finishedRow1)
    finishedBoard2.append(finishedRow2)

if fixes1 <= fixes2:
    message = {"board": finishedBoard1, "changes": fixes1}
else:
    message = {"board": finishedBoard2, "changes": fixes2}


import json
print(json.dumps(message))