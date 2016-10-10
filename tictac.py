# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:     Emily Chou
# -----------------------------------------------------------------------------
'''
Enter the module docstring here
'''
import tkinter
import random

class Game(object):
    '''
    """
    Plays a game of tic tac toe between a player and the computer

    Argument:
    parent (tkinter.Tk): the root window, parent of the frame

    Attributes:
    game_board (list): represents each square
    loc (dictionary): location of square
    """
    '''

    # Add your class variables if needed here

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        # Add your instance variables  if needed here
        # Create the restart button widget
        self.restart_button = tkinter.Button(self.parent, text = 'RESTART',
                                             command = self.restart)
        self.restart_button.grid()
        # Create a canvas widget
        self.canvas = tkinter.Canvas(self.parent, width = 300, height = 300)
        self.canvas.grid()
        # Create a label widget for the win/lose message
        self.label = tkinter.Label(self.parent)
        self.label.grid()
        self.canvas.bind("<Button-1>", self.play)
        self.canvas.grid()
        for row in range(3):
            for col in range(3):
                self.canvas.create_rectangle(100 * col, 100 * row,
                                             100 * (col + 1), 100 * (row + 1),
                                             fill = 'grey')
        self.initialize_game()

    def initialize_game(self):
        '''
        Initializations that happen at the beginning and after restarts
        '''
        # tictactoe game board with 9 empty values representing each square
        self.game_board = [None, None, None, None, None, None, None,None, None]
        # dictionary of location of each square
        self.loc = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4,
                    (1, 2): 5, (2, 0): 6, (2, 1): 7,(2, 2): 8}
        self.label.config(text = '')

    def restart(self):
        '''
        Invoked when the user clicks the restart button
        '''
        # Erase the canvas
        self.canvas.itemconfigure('all', fill = 'grey')
        # invoke initialize_game
        self.initialize_game()

    def play(self, event):
        '''
        Invoked when user clicks on a square
        :return: None if the square is already taken
        '''
        # This method is invoked when the user clicks on a square.
        # If the square is already taken, do nothing.
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        closest = self.canvas.find_closest(x,y)[0]
        if self.game_board[self.loc[(y // 100, x // 100)]] is None:
            self.game_board[self.loc[(y // 100, x // 100)]] = 'cyan'
            self.canvas.itemconfigure(closest, fill = 'cyan')
        else:
            return None

        if self.check_game() is True:
            return None
        self.moves()
        self.computer_play()
        self.check_game()


    def check_game(self):
        '''
        Checks if the game is won, lost, or tied
        :return: True if won, lost, or tied. False if game is not finished
        '''
        if (self.game_board[0] == self.game_board[1] == self.game_board[2] == 'cyan') \
            or (self.game_board[3] == self.game_board[4] == self.game_board[5] == 'cyan') \
            or (self.game_board[6] == self.game_board[7] == self.game_board[8] == 'cyan') \
            or (self.game_board[0] == self.game_board[3] == self.game_board[6] == 'cyan') \
            or (self.game_board[1] == self.game_board[4] == self.game_board[7] == 'cyan') \
            or (self.game_board[2] == self.game_board[5] == self.game_board[8] == 'cyan') \
            or (self.game_board[0] == self.game_board[4] == self.game_board[8] == 'cyan') \
            or (self.game_board[2] == self.game_board[4] == self.game_board[6] == 'cyan'):
            self.label.configure(text = 'WIN')
            self.game_board = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                               'grey', 'grey', 'grey']
            return True
        elif (self.game_board[0] == self.game_board[1] == self.game_board[2] == 'orange') \
            or (self.game_board[3] == self.game_board[4] == self.game_board[5] == 'orange') \
            or (self.game_board[6] == self.game_board[7] == self.game_board[8] == 'orange') \
            or (self.game_board[0] == self.game_board[3] == self.game_board[6] == 'orange') \
            or (self.game_board[1] == self.game_board[4] == self.game_board[7] == 'orange') \
            or (self.game_board[2] == self.game_board[5] == self.game_board[8] == 'orange') \
            or (self.game_board[0] == self.game_board[4] == self.game_board[8] == 'orange') \
            or (self.game_board[2] == self.game_board[4] == self.game_board[6] == 'orange'):
            self.label.config(text = 'LOSE')
            self.game_board = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                               'grey', 'grey', 'grey']
            return True
        elif None not in self.game_board:
                self.label.configure(text = 'TIE')
                return True
        else:
            return False

    def moves(self):
        '''
        Moves that computer can make in squares that are not taken
        :return: list of moves
        '''
        moves = []
        for loc in range(0, 9):
            if self.game_board[loc] is None:
                moves.append(loc)
        return moves

    def computer_play(self):
        '''
        The computer's move generated randomly from the list of moves returned
        in the moves method above
        '''
        while None in self.game_board:
            computer_move = random.randint(0, 8)
            if computer_move in self.moves():
                self.game_board[computer_move] = 'orange'
                self.canvas.itemconfigure(computer_move + 1,
                                              fill = 'orange')
                break
            else:
                continue

def main():
    '''
    Main method that instantiates a root window and a game object, and enters
    the main event loop
    :return:
    '''
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    tictactoe = Game(root)
    # Enter the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()