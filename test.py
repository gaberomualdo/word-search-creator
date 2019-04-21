# import word_search_creator.py via the execfile function
execfile("word_search_creator.py")

# test createWordSearch function with 8 randomly generated words
returnedWordSearch = createWordSearch(["seemly", "exotic", "obese", "disagreeable", "earn", "spark", "strengthen", "colossal"])
print stringifyWordSearch(returnedWordSearch)
