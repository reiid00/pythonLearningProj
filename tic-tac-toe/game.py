from player import HumanPlayer,RandomComputerPlayer,GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)] #We will use a single list to rep 3x3 board
        self.current_winner = None #Keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+' |')
    
    @staticmethod
    def print_board_nums():
        # 0| 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+' |')
    
    def available_moves(self):
        #concaneted
        return [i for i, spot in enumerate(self.board) if spot==' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', ' ' , 'o'] --> [(0,'x'),(1,' '),(2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #Winner if 3 in a row anywhere.. we have to check all of these!
        #Check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind +1)*3]
        if all([spot == letter for spot in row]):
            return True
        #Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #Check diagonal
        #only if the square is an even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
            
        

def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X' #starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square+1}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter='O' if letter=='X' else 'X'
        if print_game:
            time.sleep(0.8)
    if print_game:
        print('It\'s a tie!')

def play_with_player(x_player,o_player):
    t= TicTacToe()
    play(t,x_player,o_player,print_game=True)

def play_pc_vs_pc(x_player,o_player):
    x_wins = 0
    o_wins = 0
    ties = 0
    x= int(input(' Number of runs: '))
    for _ in range(x):
        t=TicTacToe()
        result = play(t,x_player,o_player,print_game=False)
        if result == 'X':
            x_wins+=1
        elif result == 'O':
            o_wins+=1
        else:
            ties+=1
    print(f'After {x} iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} ties.')



if __name__ == '__main__':
    print('Welcome to TIC-TAC-TOE GAME!!')
    valid_option=False
    while not valid_option:      
        print('Type of game: \n 1: Player vs Random Computer \n 2: Player vs Genius Computer \n 3: Random Computer vs Genius Computer')
        choice = input('Option: ')
        try:
            val=int(choice)
            if val == 1:
                x_player = HumanPlayer('X')
                o_player = RandomComputerPlayer('O')
                play_with_player(x_player, o_player)
            elif val == 2:
                x_player = HumanPlayer('X')
                o_player = GeniusComputerPlayer('O')
                play_with_player(x_player, o_player)
            elif val == 3:
                x_player = RandomComputerPlayer('X')
                o_player = GeniusComputerPlayer('O')
                play_pc_vs_pc(x_player,o_player)
            else:
                raise ValueError
            valid_option = True
        except ValueError:
            print('Invalid option. Try again.')
    print(' \n \n')
    print('Thanks for playing my tic-tac-toe game!!')

    
 
