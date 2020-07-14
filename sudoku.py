import time  
board = [[6,5,0,3,0,0,0,0,0],
         [0,0,4,0,0,0,3,0,1],
         [0,0,0,2,0,8,0,0,5],
         [3,0,5,0,0,0,0,4,0],
         [0,0,1,8,0,5,9,0,0],
         [0,2,0,0,0,0,7,0,3],
         [9,0,0,6,0,1,0,0,0],
         [5,0,6,0,0,0,8,0,0],
         [0,0,0,0,0,2,0,3,9]]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            #print("\n\n")
            #print_board(bo)
            if solve(bo):
                return True

            bo[row][col] = 0

    return False



def print_board(bo):
    for i in range(len(bo)):

        if i%3==0 and i!=0:
            print("-------------------")

        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("|", end ="")

            if j == 8:
                #time.sleep(0.1)
                print(bo[i][j])
            else:
                #time.sleep(0.1)
                print(str(bo[i][j]) + " ",end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return(i , j)  #row,col

    return None

def valid(bo, num , pos):
    
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False 

    return True


print_board(board)
solve(board)

if not find_empty(board):
    print("\n\nSolved board:\n\n")
    print_board(board)
else:
    print("\n\t\t\tError : Board imported cannnot be solved with sudoku rules. Please enter a correct Solvable Board :)\n\n")