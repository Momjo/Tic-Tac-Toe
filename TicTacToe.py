import random

def drawBoard(board):
     # This function prints out the board that it was passed.

     # "board" is a list of 10 strings representing the board (ignore index 0)
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def inputPlayerLetter():
	letter=""
	while not(letter == 'X' or letter == 'O'):
		print('Do You want to be X or O ?')
		letter =input().upper()

		#the first elemnt in the list is the player's letter, the second is the computer's letter
		if letter =='X':
			return['X','O']
		else:
			return['O','X']

def whoGoesFirst():
	
	#Rabdomly chose the player who goes first
	if random.randint(0, 1)==0:
		return'computer'
	else:
		return 'player'

def playAgain():
	print('Do you want to play again?(yes or no)')
	return input().lower().startswith('y')

#The makeMove() function is simple and only one line. 
#The parameters are a list with ten strings named board, 
#one of the players letters (either 'X' or 'O') named letter, 
#and a place on the board where that player wants to go (which is an integer from 1 to 9) named move.

def makeMove(board, letter, move):
	board[move]= letter

def isWinner(bo, le):
	return (
		(bo[7]== le and bo[8]==le and bo[9]==le)or
		(bo[4]== le and bo[5]==le and bo[6]==le)or
		(bo[1]== le and bo[2]==le and bo[3]==le)or
		(bo[7]== le and bo[4]==le and bo[1]==le)or
		(bo[8]== le and bo[5]==le and bo[2]==le)or
		(bo[9]== le and bo[6]==le and bo[3]==le)or
		(bo[7]== le and bo[5]==le and bo[3]==le)or
		(bo[9]== le and bo[5]==le and bo[1]==le))

#making a copy from default board
def getBoardCopy(board):
	dupeBoard=[]

	for i in board:
		dupeBoard.append(i)
	return dupeBoard

def isSpaceFree(board, move):
	return board[move]==''

def getPlayerMove(board):
	move=''
	while move not in '1 2 3 4 5 6 7 8 9'.split()or not isSpaceFree(board, int(move)):
		print('What is your next move?(1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, moveList):
	possibleMoves= []
	for i in moveList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if len(possibleMoves)!= 0 :
		return random.choice(possibleMoves)
	else:
		return None


#Creating the Computer’s Artificial Intelligence(Hosh masnoii)
def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter=='O'
	else:
		playerLetter=='X'

	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i
	#If the human player cannot win in one more move,
	#the for loop will eventually finish and execution continues

	move = chooseRandomMoveFromList(board,[1,3,7,9])
	if move!= None:
		return move
	
	if isSpaceFree(board, 5):
		return 
	return chooseRandomMoveFromList(board,[2,4,6,8])

#cheking if the board is full

def isBoardFull(board):
	for i in range(1,10):
		if isSpaceFree(board, i):
			return False
	return True

print('Welcome to Tic Tac Toe! <3')

while True:
	
	#reset the board
	theBoard=['']*10
	
	playerLetter, computerLetter = inputPlayerLetter()
	
	turn = whoGoesFirst()
	
	print('The'+ turn + 'will go first.')
	
	gameIsPlaying = True

	while gameIsPlaying:
	
		if turn== 'player':
		
			#players turn
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)
			
			if isWinner(theBoard, playerLetter):
				
				drawBoard(theBoard)
				print('Hoooray! You have won the game! <3')
				gameIsPlaying = False
			
			else:
				
				if isBoardFull(theBoard):
    			
					drawBoard(theBoard)
					print('The game is a tie!!')
					break
				
				else:
    				
					turn = 'computer'
		else:
    		
			#Computer's turn
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)
			
			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('The computer has beaten you! You lose.')

				gameIsPlaying = False

			else:
    			
				if isBoardFull(theBoard):
				
					drawBoard(theBoard)
					print('The game is a tie')
					break
				
				else:
					turn = 'player'
	if not playAgain():
		break
