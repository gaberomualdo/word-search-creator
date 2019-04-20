def createWordSearch(words):
	# grid side length is the length of the longest word
	# --> makes word search possible to generate with given words and grid size
	gridSideLength = len(max(words, key=len))

	# generate 2d array with side lengths of gridSideLength, with each item having a content of ""
	grid = [["*"]*gridSideLength]*gridSideLength

	return grid

	# loop through words and place them randomly in the grid, either horizontally, vertically, or diagonally
	for word in words:
		# === CODE HERE ===
		pass
	pass

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