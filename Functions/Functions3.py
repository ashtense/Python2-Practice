# string manipulation function(for string split on the basis of a qualifier.
def split_words(incomming_word):
    arr_words = incomming_word.split(' ')
    return arr_words


def sort_words(incoming_words):
    # string manipulation function(for sorting through a word array)
    # maybe present in python's base library.
    return sorted(incoming_words)


def pop_from_array(incoming_words):
    return incoming_words.pop(1)


def pop_from_array_from_behind(incoming_words):
    return incoming_words.pop(-1)


def sort_sentence(incoming_word):
    words = split_words(incoming_word)
    return sort_words(words)


print "this function will split words."
arrSplittedWords = split_words("Hello Everyone day of reckoning.")
print arrSplittedWords

print "this function will sort words."
arrSortedWords = sort_words(arrSplittedWords)
print arrSortedWords

print "this function just pops things from an array and returns"
print pop_from_array(arrSortedWords)
print pop_from_array_from_behind(arrSortedWords)

print "this function sorts sentence on word basis"
print sort_sentence("Hello everyone this is Ashwani Solanki")
