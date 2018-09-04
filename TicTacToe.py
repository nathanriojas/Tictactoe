class TicTacToe(object):
	def __init__(self):
		# grid will be used to check the winner and gridView generates the game visualization
		self.grid = [[1,1,1],[1,1,1],[1,1,1]]
		self.gridView = "_________"
	def viewGrid(self):
		# separate gridView every three characters for the 3x3 board
		print("\n  123\nA " + self.gridView[:3] + "\nB " + self.gridView[3:6] + "\nC " + self.gridView[6:])
	# Asks the user to choose X or O lower or uppercase to return and throws an error if neither is input
	def chooseSide(self):
		character = ""
		loops = 0
		while character not in ["x","X","o","O"]:
			if loops:
				print("Oops not a valid choice, please choose X or O!\n")
			character = str(input("Player 1: X or O? "))
			# allow the user to quit within this method as well
			if self.quitGame(character):
				return 0
			loops = 1
		return character.upper()
	# Checks if grid list at the input position is empty by looking for the initialized 1 value
	def isEmpty(self,coordR,coordC):
		return self.grid[coordR][coordC] == 1
	# Checks that the input for the X or O is in the format required to populate the board
	def isValidInput(self,inputString):
		# the input string should be two characters and A, B, or C is the first character and 1, 2, or 3 is the second
		if len(inputString) != 2 or ord(inputString[0]) not in [65,66,67] or inputString[1] not in ['1','2','3']:
			return False
		return True
	# Updates the 2D grid list with the value at the indices input, converts indices to the string position to
	# update the gridView
	def updateGrid(self,coordR,coordC, value):
		self.grid[coordR][coordC] = value
		stringIndex = 3*coordR + coordC
		# slice string to add user's value
		self.gridView = self.gridView[:stringIndex] + value + self.gridView[stringIndex+1:]
	def quitGame(self,quitString):
		if quitString == "QUIT" or quitString == "quit":
			return 1
		return 0
	# Look at the rows, diagonals, and columns to determine if one of these arrays contains the same value
	# not equal to the initialized 1 value using sets
	def checkWinner(self):
		# check that the rows have a winner
		for rows in self.grid:
			if len(set(rows)) == 1 and 1 not in rows:
				return rows[0]
		diagonal1 = []
		diagonal2 = []
		# check that the diaognals have a winner
		for diags in range(len(self.grid)):
			diagonal1.append(self.grid[diags][diags])
			diagonal2.append(self.grid[len(self.grid)-1-diags][diags])
		if len(set(diagonal1)) == 1 and 1 not in diagonal1:
			return diagonal1[0]
		if len(set(diagonal2)) == 1  and 1 not in diagonal2:
			return diagonal2[0]
		# check that the columns have winner
		for cols in range(len(self.grid)):
			tempList = []
			for rows in range(len(self.grid)):
				tempList.append(self.grid[rows][cols])
			if len(set(tempList)) == 1 and 1 not in tempList:
				return tempList[0]
		return 0
	# Run the actual game for a total of 9 moves, but check that each move is a valid move, i.e. no duplicates
	# or overlapping inputs. Enable the players to quit at any time.
	def twoPlayer(self):
		print("Let's play Tic Tac Toe! Type quit at any time to stop the match \n")
		moveCount = 0
		playerSymbol = ["X","O"]
		rowDict = {"A":0,"B":1,"C":2}
		# determine whether player 1 wants X or O to create the move request string
		ch = self.chooseSide()
		if ch == 0:
			print("\nGame terminated...See Ya!")
			return
		# associate players with either 0 or 1 based on their choice of X or O to update the grid throughout the game
		player = playerSymbol.index(ch)
		while moveCount < 9:
			# display the grid to show the user the board with the coordinates to enter
			self.viewGrid()
			print ("\nMake your move Player " + playerSymbol[player] + "! Enter the row followed by column (i.e C2)")
			move = str(input())
			if self.quitGame(move):
				print("\nGame terminated...See Ya!")
				return
			# remove any unecessary spaces and make characters uppercase
			move = move.replace(" ","")
			move = move.upper()
			# check that the user did not enter invalid strings for grid coordinates and maintain the player's turn if so
			if not self.isValidInput(move):
				print("\nNot a valid input! Enter the row followed by the column\n")
				continue
			# check that the space is not filled for the grid coordinates and maintain the player's turn if so
			if not self.isEmpty(rowDict[move[0]],int(move[1])-1):
				print("\n" + move + " is already filled, please enter a different move\n")
				continue
			# update the grid list and gridView since a valid move was played
			self.updateGrid(rowDict[move[0]],int(move[1])-1,playerSymbol[player])
			# end the game if a winning move was played
			if self.checkWinner():
				self.viewGrid()
				print("\nPlayer " + playerSymbol[player] + " wins! Good Game.")
				return
			# switch the current player's turn to the opposite player
			player = 1^player
			moveCount += 1
		# over 9 moves have been played so the grid is full and there is no winner
		self.viewGrid()
		print("\nLooks like we have a draw!")
		return

def main():
	newGame = TicTacToe()
	newGame.twoPlayer()
main()
