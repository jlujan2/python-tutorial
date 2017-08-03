import numpy as np

def possibilities(board):
    coordinates = []
    for col, row in enumerate(board, start=0):
        if len(np.where(row == 1)) > 0:
		    for num in np.where(row == 1):
			
			    coordinates.append((col, num))
    return coordinates
board = np.zeros((3,3))
board.itemset((1,1), 1)
print (possibilities(board))