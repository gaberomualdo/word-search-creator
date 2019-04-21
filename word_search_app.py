# import word_search_creator.py via the execfile function
execfile("word_search_creator.py")

# request name of word search
wordSearchName = raw_input("Name of word search: ")

# request words from user
wordListString = raw_input("Enter words (separated by a comma): ")
wordList = wordListString.split(",")

# list of accepted letters for words
acceptedLetters = list("abcdefghijklmnopqrstuvwxyz")

# filter word list into words with accepted letters
for wordIndex in range(len(wordList)):
	word = wordList[wordIndex]
	filteredWord = ""
	for letter in word:
		if letter in acceptedLetters:
			filteredWord += letter
	wordList[wordIndex] = filteredWord

# create word search via function in word_search_creator.py
wordSearchArray = createWordSearch(wordList)

# get stringified word search via function in word_search_creator.py, and split into rows
stringifiedWordSearch = stringifyWordSearch(wordSearchArray).split("\n")

print stringifiedWordSearch

# print word search with name and words to find
wordSearchArray[0]