board = [ [1,2,3],[4,5,6],[7,8,9] ]

def column_check(b):
	return len(set( [board[t][b] for t in range(3)] ))

def rcross_check():
	return len(set( [board[t][t] for t in range(3)] ))

def lcross_check():
	return len(set( [board[t][2-t] for t in range(3)] ))

def win_check():
	if ( len(set(board[0])) == 1 or len(set(board[1])) == 1 or len(set(board[2])) == 1 ) or ( column_check(0) == 1 or column_check(1) == 1 or column_check(2) == 1 ) or ( rcross_check() == 1 or lcross_check() == 1 ):
		return True
	else:
		return False

def print_board():
	for i in range(3):
		for j in range(3):
			if board[i][j] == 'x' or board[i][j] == 'o':
				print(board[i][j], end="")
			else:
				print('.', end="")
			if j!=2:
				print("|",end="")
		print()
		print("-|-|-")


print('''
11|12|13
--|--|--
21|22|23
--|--|--
31|32|33
Type Where you want to put x or o
''')	

x = 1
print_board()
for i in range(3):
	for j in range(3):
		if x%2!=0:
			p1 = input("Player-1 <x> ")
			board[int(p1[0])-1][int(p1[1])-1] = 'x'
		else:
			p1 = input("Player-2 <o> ")
			board[int(p1[0])-1][int(p1[1])-1] = 'o'

		print_board()

		if win_check():
			if x%2!=0:
				print("Player 1 Won!")
			else:
				print("Player 2 Won!")
			exit()
		x+=1