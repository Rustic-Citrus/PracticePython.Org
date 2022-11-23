def reverse_word_order(sentence):
    """Takes a string and reverses the order of the words."""
    list_of_words = sentence.split()
    list_of_words.reverse()
    new_sentence = ' '.join(list_of_words)
    return new_sentence

user_sentence = input('Type any sentence of at least two words: ')
print(reverse_word_order(user_sentence))
