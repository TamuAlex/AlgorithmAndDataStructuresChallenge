''' Main module of the Challenge
Module where the main code of the challenge is

Author: Alejandro Ortega <alejandro.ormar@gmail.com>

Created: 26th November, 2022
'''

#Imports
import utils


#Code
def recursiveMovement(depth,board,snake,currentMovement):
    ''' main function that checks the movements
    This function uses recursion to check the movements of the snake, and then 
    save the valid ones in a global variable

    Parameters
    ---------
    depth: integer
        current depth of the recursion

    board: array.integer
        game's board
    
    snake: array.array.integer
        game's snake

    currentMovement: String
        the hypotetical movement that the snake has done so far
    
    '''
    global validMovements
    global movements
    if depth > 1:
        for movement in movements:
            if utils.isValidMovement(board,snake,movement):
                snakeTemp = snake.copy()
                utils.moveSnake(snakeTemp,movement)
                currentMovement = currentMovement + movement
                recursiveMovement(depth-1,board,snakeTemp,currentMovement)
                currentMovement = currentMovement[:-1]
                

    else:
        for movement in movements:
            if utils.isValidMovement(board,snake,movement):
                currentMovement = currentMovement + movement
                validMovements.append(currentMovement)
                currentMovement = currentMovement[:-1]



def testInitialConditions(board,snake,depth):
    '''Function that test the initial conditions to check everything has the
    correct format
    
     Parameters
    ---------
    depth: integer
        depth to be checked

    board: array.integer
        board to be checked
    
    snake: array.array.integer
        snake to be checked
    '''

    utils.checkBoard(board)
    utils.checkSnake(snake)
    utils.checkDepth(depth)


if __name__ == '__main__':
    movements = ["L","R","U","D"]
    #TEST 1
    depth = 3
    board = [4,3]
    snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    validMovements=[]

    testInitialConditions(board,snake,depth)
    recursiveMovement(depth,board,snake,"")
    print(validMovements)
    print(len(validMovements))

    #TEST 2
    depth = 10
    board = [2,3]
    snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    validMovements=[]

    testInitialConditions(board,snake,depth)
    recursiveMovement(depth,board,snake,"")
    print(validMovements)
    print(len(validMovements)) 

    #TEST 3
    depth = 4
    board = [10,10]
    snake = [[5,5], [5,4], [4,4], [4,5]]
    validMovements=[]

    testInitialConditions(board,snake,depth)
    recursiveMovement(depth,board,snake,"")
    print(validMovements)
    print(len(validMovements)) 