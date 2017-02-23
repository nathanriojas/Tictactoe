tictactoe = []
winner = "null"

def grid():
	grid_output = "   0     1     2\n"

	for row in range (3):
		grid_output = grid_output + str(row) + " "
		for value in tictactoe[row]:
			grid_output = grid_output + value + "|"
		grid_output = grid_output[:-1] + "\n"
	return grid_output


def gridNotFull ():
	for rows in tictactoe:
		for elements in rows:
			if element == "_____":
				return True
	return False

def validInput (userInput):
	validList = ['00','01','02','10','11','12','20','21','22']
	if len(userInput) > 2 or userInput not in validList:
		return False
	return


def checkWinner():
	global winner
	for i in range (3):
		row = True
		col = True
		descDiag = True
		ascDiag = True

		for j in range (2):
			symbolR = str(tictactoe[i][j])
			symbolC = str(tictactoe[j][i])
			symbolAsc = str(tictactoe[j][j])
			symbolDesc = str(tictactoe[j][2-j])
			
			if (tictactoe[i][j] != tictactoe[i][j+1]):
				row = False
			if (tictactoe[j][i] != tictactoe[j+1][i]):
				col = False
			if (tictactoe[j][j] != tictactoe[j+1][j+1]):
				descDiag = False
			if (tictactoe[j][2-j] != tictactoe[j+1][1-j]):
				ascDiag = False

		if (row == True and symbolR != "_____"):
			winner = symbolR
			break
		elif (col == True and symbolC != "_____"):
			winner = symbolC
			break		
		elif (descDiag == True and symbolDesc != "_____"):
			winner = symbolDesc
			break
		elif (ascDiag == True and symbolAsc != "_____"):
			winner = symbolAsc
			break
		
def twoPlayer():

	print("Welcome to Tic Tac Toe! Player 1 is x and Player 2 is o\nEnter positions row first (Ex: 10 == middle row, first (0) column)\nLet's Play! \n")
	
	for moves in range (9):
		print(grid())
		if moves % 2 == 0:
			userIn = str(input("What's your move Player 1 (x)?: ")).strip(' ')
			while (tictactoe[int(userIn[0])][int(userIn[1])] != "_____"):
				print("Error: position already filled")
				userIn = str(input("What's your move Player 1?: ")).strip(' ')
			tictactoe[int(userIn[0])][int(userIn[1])] = "__x__"

		else: 
			userIn = str(input("What's your move Player 2 (o)?: "))
			while (tictactoe[int(userIn[0])][int(userIn[1])] != "_____"):
				print("Error: position already filled")
				userIn = str(input("What's your move Player 2?: ")).strip(' ') 
			tictactoe[int(userIn[0])][int(userIn[1])] = "__o__"

		checkWinner()
		if winner != "null":
			break

def versusComputer():
	print("Create this function")

def main():
	global winner
	global tictactoe

	for i in range (3):
		row = []
		for j in range (3):
			row.append("_____")
		tictactoe.append(row) 
	
	gamesetting = str(input("Would you like to play 2 player (Otherwise you will play against the computer)? (Y|N)")).strip(" ")
	
	if gamesetting == "Y" or gamesetting == "y":
		twoPlayer()
	elif gamesetting == "N" or gamesetting == "n":
		versusComputer()
	else:
		print("invalid")

	checkWinner()
	print("The winner is " + str(winner.strip("_")) + "!")
	
main()
