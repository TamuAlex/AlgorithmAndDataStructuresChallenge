''' Set of utilities for the challenge
A Module with a set of utilities needed for the challenge. It has been decided to
separate this utilities to another module in order to make the code more readable.

Author: Alejandro Ortega <alejandro.ormar@gmail.com>

Created: 26th November, 2022
'''

def checkDepth(depth):
    ''' Function that checks if the depth has a valid size

    Parameters
    ----------
    depth: integer
        depth to be checked
    
    '''

    assert depth>=1 and depth <=20, 'The depth must be between 1 and 20'

    
def checkBoard(board):
    ''' Function that checks if the board has the correct format. If not,
    throws an AssertionError exception

    Parameters
    ----------
    board: array.integer
        board to be checked
    
    '''

    assert len(board) == 2, 'It must be a two dimension board'
    
    for dimension in board:
        assert dimension >= 1, 'The dimension of the board has to be greater or equal than 1'
        assert dimension <= 10, 'The dimension of the board has to be lower or equal than 10'


def checkSnake(snake):
    ''' Function that checks if the snake is in the correct format.
    If not, throws an AssertionError exception.
    The challenge says that the initial position is guaranteed, so no more verifications are necesary
    for the snake.

    Parameters
    ----------
    snake: array.array.integer
        snake to be checked
    '''
    assert len(snake) >=3, 'The snake\'s lenght must be greater or equal than 3'
    assert len(snake) <=7, 'The snake\'s lenght must be lower or equal than 7'

    for position in snake:
        assert len(position) == 2, 'Each position of the snake must be a x,y coordinate (two numbers)'
        

def isValidMovement(board,snake, movement):
    '''Function that, given the snake, a movement and the board, checks if the movement cell is empty and a valid one
    for the snake to move to.

    Parameters
   ----------
    board: array.integer
        board to be checked

    snake: array.array.integer
        snake to be checked

    movement: String
        movement to check (L,R,D,U)

    Return
    ---------
    boolean: if the cell is valid or not
    '''
    row = -1
    column = -1
    if movement == "L":
        row = snake[0][0]
        column = snake[0][1]-1

    if movement == "R":
        row = snake[0][0]
        column = snake[0][1]+1

    if movement == "U":
        row = snake[0][0]-1
        column = snake[0][1]

    if movement == "D":
        row = snake[0][0]+1
        column = snake[0][1]

    #Checks if the cell is in the board
    if row < board[0] and row >= 0:
        if column < board[1] and column >= 0:
            #Checks if the snake is in the cell
            for position in snake[:-1]:
                if position[0]==row and position[1]==column:
                    return False
            return True
    return False

board = [4,3]
snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]

def moveSnake(snake,movement):
    '''Function that moves the snake 
    
    Parameters
   ----------
    snake: array.array.integer
        snake to move

    movement: String
        movement to make (L,R,D,U) 
 
    '''
    row = -1
    column = -1
    if movement == "L":
        row = snake[0][0]
        column = snake[0][1]-1

    if movement == "R":
        row = snake[0][0]
        column = snake[0][1]+1

    if movement == "U":
        row = snake[0][0]-1
        column = snake[0][1]

    if movement == "D":
        row = snake[0][0]+1
        column = snake[0][1]

    newPosition=[row,column]
    snake.insert(0,newPosition)
    snake.pop(-1)



  
board = [4,3]
snake = [[0,0], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
#moveSnake(snake,"U")
#print(snake)
print(isValidMovement(board,snake,"U"))

