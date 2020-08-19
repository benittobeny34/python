#-----------SUDOKU LOGIC-----------

EMPTY  = 0
def sudoku(board):
    if is_complete(board):
        return board
    
    r, c = find_first_empty(board)

    #set values 1 to 9 and check;
    for i in range(1, 10):
        board[r][c] = i
        
        #print(board)
        if valid_so_far(board):
            #print(board)            
            result = sudoku(board)
            #print(result)
            if is_complete(result):
                return result
        board[r][c] = EMPTY
    return board
        

def is_complete(board):
    return all(all(val is not EMPTY for val in row) for row in board)

def find_first_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:     
                return i,j;
    
    return False

def valid_so_far(board):
    if not rows_valid(board):
        return False
    if not cols_valid(board):
        return False
    if not blocks_valid(board):
        return False
    
    return True

def rows_valid(board):
    for row in board:
        if duplicates(row):
            return False
   
    return True

def cols_valid(board):
    for j in range(len(board[0])):
        if duplicates([board[i][j] for i in range(len(board))]):
            return False
    
    return True

def blocks_valid(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(board[i+k][j+l])
            if duplicates(block):
                return False
    
    return True




def duplicates(arr):
    c = {}
    for val in arr:
        if val in c and val is not EMPTY:
            return True
        c[val]=True
    return False

print("!Note that the empty fields are filled with zero(0):")

board = [
    [2,5,0,0,3,0,9,0,1],
    [0,1,0,0,0,4,0,0,0],
    [4,0,7,0,0,0,2,0,8],
    [0,0,5,2,0,0,0,0,0],
    [0,0,0,0,9,8,1,0,0],
    [0,4,0,0,0,3,0,0,0],
    [0,0,0,3,6,0,0,7,2],
    [0,7,0,0,0,0,0,0,3],
    [9,0,3,0,0,0,6,0,4]
    ]



print("prefilled sudoku:>>>")

for i in range(len(board)):
    for j in range(len(board)):
            print(board[i][j],end="  ")       
    print()
print('*' * 50)
print("The complete sudoku is:")

board = sudoku(board)


for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] != 0:
            print(board[i][j],end="  ")
        else:
            print(" ",end=" ")
    print()



'''
board = [
    [4,0,0,0,0,0,8,0,5],
    [0,3,0,0,0,0,0,0,0],
    [0,0,0,7,0,0,0,0,0],
    [0,2,0,0,0,0,0,6,0],
    [0,0,0,0,8,0,4,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,6,0,3,0,7,0],  
    [5,0,0,2,0,0,0,0,0],
    [1,0,4,0,0,0,0,0,0]
    ]
    

board = [
    [8,5,0,0,0,2,4,0,0],
    [7,2,0,0,0,0,0,0,9],
    [0,0,4,0,0,0,0,0,0],
    [0,0,0,1,0,7,0,0,2],
    [3,0,5,0,0,0,9,0,0],
    [0,4,0,0,0,0,0,0,0],
    [0,0,0,0,8,0,0,7,0],  
    [0,1,7,0,0,0,0,0,0],
    [0,0,0,0,3,6,0,4,0]
    ] 
        
        
''' 
