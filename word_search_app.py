# import word_search_creator.py via the execfile function
execfile("word_search_creator.py")

# request name of word search
wordSearchName = raw_input("\nName of word search: ")

# request words from user
wordListString = raw_input("Enter words (separated by a comma): ")
wordList = wordListString.lower().split(",")

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

# print word search name correctly centered
paddingLength = int(round((4 + len(max(wordList, key=len)) + len(stringifiedWordSearch[0]) - len(wordSearchName) - 2) / 2) + 1)

print ""
print ("=" * paddingLength) + " " + wordSearchName + " " + ("=" * paddingLength)
print ""

# regenerate word list to fit initial user-inputted letter-cases
wordList = wordListString.split(",")

# list of accepted letters for words
acceptedLetters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# filter word list into words with accepted letters
for wordIndex in range(len(wordList)):
	word = wordList[wordIndex]
	filteredWord = ""
	for letter in word:
		if letter in acceptedLetters:
			filteredWord += letter
	wordList[wordIndex] = filteredWord

# print word search along with words to find
for rowIndex in range(len(stringifiedWordSearch)):
	if(rowIndex < len(wordList)):
		print stringifiedWordSearch[rowIndex] + "    " + wordList[rowIndex]
	else:
		print stringifiedWordSearch[rowIndex]
print ""
