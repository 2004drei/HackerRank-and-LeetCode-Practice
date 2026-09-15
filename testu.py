wordList = {'a':1, 'b':1, 'c':1}

first_value = list(wordList.values())[0]
all_same = all(v == first_value for v in wordList.values())
