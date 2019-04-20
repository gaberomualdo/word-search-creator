def createWordSearch(words):
	# grid side length is the length of the longest word
	# --> makes word search possible to generate with given words and grid size
	gridSideLength = max(words, key=len)

	# generate 2d array with side lengths of gridSideLength, with each item having a content of ""
	grid = [["*"]*gridSideLength]*gridSideLength

	return grid

	# loop through words and place them randomly in the grid, either horizontally, vertically, or diagonally
	for word in words:
		# === CODE HERE ===
		pass
	pass

# test createWordSearch function with 8 randomly generated words
returnedWordSearch = createWordSearch(["seemly", "exotic", "obese", "disagreeable", "earn", "spark", "strengthen", "colossal"])
for row in returnedWordSearch:
	print ' '.join(row)