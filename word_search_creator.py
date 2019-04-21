from copy import copy, deepcopy
import random

def createWordSearch(words):
	# grid side length is the length of the longest word
	# --> makes word search possible to generate with given words and grid size
	gridSideLength = len(max(words, key=len)) + 6

	# generate 2d array with side lengths of gridSideLength, with each item having a content of ""
	grid = []
	for rowIndex in range(gridSideLength):
		row = []
		for columnIndex in range(gridSideLength):
			row.append("")
		grid.append(row)

	# loop through words and place them randomly in the grid, either horizontally, vertically, or diagonally
	for word in words:
		# choose randomly between possible placement types (horizontal, vertical, and diagonal)
		placementType = random.choice(["horizontal", "vertical", "diagonal"])

		# placement location variable ( [x, y] )
		placementLocation = [0, 0]

		# placement status (when placed, placement status is True and while loop ends)
		placementStatus = False

		while(placementStatus == False):
			# create grid copy to be edited in testing
			#gridCopy = deepcopy(grid)

			# create random coordinates for placement location
			placementLocation = [random.randrange(gridSideLength), random.randrange(gridSideLength)]
			if(placementType == "horizontal" or placementType == "diagonal"):
				if(gridSideLength - len(word) == 0):
					placementLocation[0] = 0
				else:
					placementLocation[0] = random.randrange(gridSideLength - len(word))
			if(placementType == "vertical" or placementType == "diagonal"):
				if(gridSideLength - len(word) == 0):
					placementLocation[1] = 0
				else:
					placementLocation[1] = random.randrange(gridSideLength - len(word))
			
			# set placement status to True --> to be changed back to False if there is overlap in placement location
			placementStatus = True

			# loop through word and letter placement locations to check if placement location doesn't overlap with other words
			for letterIndex in range(len(word)):
				letter = word[letterIndex]
				letterLocation = [placementLocation[0], placementLocation[1]]
				if(placementType == "horizontal" or placementType == "diagonal"):
					letterLocation[0] += letterIndex
				if(placementType == "vertical" or placementType == "diagonal"):
					letterLocation[1] += letterIndex
				
				if(grid[letterLocation[0]][letterLocation[1]] != "" and grid[letterLocation[0]][letterLocation[1]] != letter):
					placementStatus = False

		for letterIndex in range(len(word)):
			letter = word[letterIndex]
			letterLocation = [placementLocation[0], placementLocation[1]]
			if(placementType == "horizontal" or placementType == "diagonal"):
				letterLocation[0] += letterIndex
			if(placementType == "vertical" or placementType == "diagonal"):
				letterLocation[1] += letterIndex
			
			grid[letterLocation[0]][letterLocation[1]] = letter

	# fill the rest of grid with random letters
	for rowIndex in range(len(grid)):
		row = deepcopy(grid[rowIndex])
		for itemIndex in range(len(row)):
			if(row[itemIndex] == ""):
				row[itemIndex] = random.choice(list("abcdefghijklmnopqrstuvwxyz"))
		grid[rowIndex] = deepcopy(row)

	return grid

# convert word search grid to printable string
def stringifyWordSearch(wordSearchArray):
	returnValue = ""
	for row in wordSearchArray:
		returnValue += " ".join(row) + "\n"
	# return concatenated rows, joined with a newline --> the [:-1] is to remove the last trailing newline
	return returnValue[:-1]

# test createWordSearch function with 8 randomly generated words
returnedWordSearch = createWordSearch(["seemly", "exotic", "obese", "disagreeable", "earn", "spark", "strengthen", "colossal"])
print stringifyWordSearch(returnedWordSearch)