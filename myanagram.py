import string
common_punctuations = list(string.punctuation)
def find_anagram(word, anagram):
    #convert to list with spaces as delimiters
    word_list , anagram_list = word.lower().split() , anagram.lower().split()
    #add all members of the list so that there will no more spaces if there are in the original string
    good_word = ''
    for each_word in word_list:
        for char in each_word:
            if char in common_punctuations:
                continue
            else:
                good_word += char

    good_anagram = ''
    for each_word in anagram_list:
        for char in each_word:
            if char in common_punctuations:
                continue
            else:
                good_anagram += char


    if sorted(good_word) == sorted(good_anagram):
        return True
    else:
        return False

print(find_anagram('ball','great'))

