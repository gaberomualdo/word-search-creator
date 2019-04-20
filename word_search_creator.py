def createWordSearch(words):
	gridSideLength = 0
	for word in words:
		# grid side length is 4 added to the length of the longest word
		# --> makes word search harder and possible to generate with given words and grid size
		if(gridSideLength - 4 < len(word)):
			gridSideLength = len(word) + 4