# import word_search_creator.py via the execfile function
execfile("word_search_creator.py")

# request name of word search
wordSearchName = raw_input("Name of word search: ")

# request words from user
wordListString = raw_input("Enter words (separated by a comma): ")
wordList = wordListString.split(",")

print wordList

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

print wordList

# create word search via the function in word_search_creator.py
wordSearchArray = createWordSearch(wordList)