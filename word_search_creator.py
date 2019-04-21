from copy import copy, deepcopy
import random

# function to yield an error (by requesting second index of empty array) --> used to move to the except section within try-except statements
def yieldError():
	return [][1]

def createWordSearch(words):
	# grid side length is the length of the longest word
	# --> makes word search possible to generate with given words and grid size
	gridSideLength = len(max(words, key=len))

	# generate 2d array with side lengths of gridSideLength, with each item having a content of ""
	grid = [[""]*gridSideLength]*gridSideLength

	# loop through words and place them randomly in the grid, either horizontally, vertically, or diagonally
	for word in words:
		# make copy of current grid for later use
		currentGrid = deepcopy(grid)
		print currentGrid

		# list of all possible grids after word is placed in grid
		possibleNewGrids = []

		# loop rows and columns
		for rowIndex in range(len(grid)):
			row = deepcopy(grid[rowIndex])
			for itemIndex in range(len(row)):
				# get possible grids for horizontal, vertical, and diagonal placement
				for placementType in ["horizontal", "vertical", "diagonal"]:
					if(placementType == "horizontal"):
						# loop through and place each letter of word
						for letterIndex in range(len(word)):
							letter = word[letterIndex]
							try:
								if(row[itemIndex + letterIndex].replace(letter, "") == ""):
									row[itemIndex + letterIndex] = letter
								else:
									yieldError()
							except:
								break
						if(letterIndex == len(word) - 1):
							grid[rowIndex] = deepcopy(row)
							possibleNewGrids.append(deepcopy(grid))
						grid = deepcopy(currentGrid)

					elif(placementType == "vertical"):
						pass
					elif(placementType == "diagonal"):
						pass

		grid = deepcopy(random.choice(possibleNewGrids))

	# fill the rest of grid with random letters
	for rowIndex in range(len(grid)):
		row = deepcopy(grid[rowIndex])
		for itemIndex in range(len(row)):
			if(row[itemIndex] == ""):
				row[itemIndex] = random.choice(list("*"))
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