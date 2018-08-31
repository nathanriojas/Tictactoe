import msvcrt

class TicTacToe(object):
	def __init__(self):
		self.grid = [[1,1,1],[1,1,1],[1,1,1]]
		self.gridView = "_________"
	def viewGrid(self):
		print(" 123\nA" + self.gridView[:3] + "\nB" + self.gridView[3:6] + "\nC" + self.gridView[6:])
	def isEmpty(self,coordR,coordC):
		return self.grid[coordR][coordC] == 1
	def isValidInput(self,inputString):
		inputString = inputString.replace(" ","")
		inputString = inputString.upper()
		if len(inputString) != 2 or ord(inputString[0]) not in [65,66,67] or inputString[1] not in ['1','2','3']:
			return False
		return True
	def updateGrid(self,coordR,coordC, value):
		self.grid[coordR][coordC] = value
		stringIndex = 3*coordR + coordC
		self.gridView[stringIndex] = value 
	def checkWinner(self):
		for rows in self.grid:
			if len(set(rows)) == 1:
				return rows[0]
		diagonal1 = []
		diagonal2 = []
		for diags in range(len(self.grid)):
			diagonal1.append(self.grid[diags][diags])
			diagonal2.append(self.grid[len(self.grid)-diags][diags])
		if len(set(diagonal1)) == 1:
			return diagonal1[0]
		if len(set(diagonal2)) == 1:
			return diagonal2[0]
		for cols in range(len(self.grid)):
			tempList = []
			for rows in range(len(self.grid)):
				tempList.append(self.grid[[rows][cols]])
			if len(set(tempList)) == 1:
				return rows[0]
		return 0
	def twoPlayer(self):
		print("Welcome to Two Player Tic Tac Toe! Press Esc at any time to stop the match \n")
		moveCount = 0
		player = 0
		while moveCount < 9:
			self.viewGrid()
			if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':
				print ("Aborting game...")
				break
			print ("Make your move Player " + str(player + 1) + "! Enter the row followed by column (i.e C2)")
			move = str(input())	
			if not self.isValidInput(move):
				print("Not a valid input! Enter the row followed by the column")
				continue
			player = 1^player
			moveCount += 1
def main():
	newGame = TicTacToe()
	newGame.twoPlayer()
main()


