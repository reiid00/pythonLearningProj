import random
import re

class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        #create board
        self.board=self.create_new_board()
        self.assign_values_to_board()
        #set of locations we've uncovered
        self.dug=set()

    def create_new_board(self):
        #generate new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #plants the bombs
        bombs_planted=0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted+=1
        return board

    def assign_values_to_board(self):
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                if self.board[x][y] == '*':
                    continue
                self.board[x][y] = self.get_num_neighbor_bombs(x,y)

    def get_num_neighbor_bombs(self,r,c):
        num_neighbor_bombs=0
        for x in range(max(0,r-1), min(self.dim_size-1,r+1)+1):
            for y in range(max(0,c-1),min(self.dim_size-1,c+1)+1):
                if x==r and y==c:
                    continue
                if self.board[x][y]=='*':
                    num_neighbor_bombs+=1
        return num_neighbor_bombs  
    
    def dig(self,r,c):
        self.dug.add((r,c))
        if self.board[r][c]=='*':
            return False
        elif self.board[r][c]>0:
            return True
        for x in range(max(0,r-1), min(self.dim_size-1,r+1)+1):
            for y in range(max(0,c-1),min(self.dim_size-1,c+1)+1):
                if(x,y) in self.dug:
                    continue
                self.dig(x,y)
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                if(x,y) in self.dug:
                    visible_board[x][y]=str(self.board[x][y])
                else:
                    visible_board[x][y]=' '
         # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play (dim_size,num_bombs):
    # step 1: create the board and plant the bombs
    board = Board(dim_size,num_bombs)
    # step 2: show the user the board and ask for where they want to dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively unitl each square is at least next to a bomb
    # step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe=True
    while len(board.dug)<board.dim_size**2-num_bombs:
        print(board)
        user_input=re.split(',(\\s)*',input("Where would you like to dig? Input row,col:"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row<0 or row> dim_size or col<0 or col>=dim_size:
            print("Row and Col must be within the board. Input again!")
            continue
        safe = board.dig(row,col)
        if not safe:
            break
    if safe:
        print("YOU WON!")
    else:
        print(f"YOU LOST. Bomb was at row: {row} , col: {col}")
    board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]    
    print(board)   

if __name__ == '__main__':
    p=0
    while(p>=0):
        print("CHOOSE DIFFICULTY: 1. EASY(5 Bombs) 2. MEDIUM (10 Bombs) 3. HARD (20 Bombs)")
        p = int(input("Option: "))
        if p==1:
            play(10,5)
            p=-1
        elif p==2:
            play(10,10)
            p=-1
        elif p==3:
            play(10,20)
            p=-1
        else: 
            continue

