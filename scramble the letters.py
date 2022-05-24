from random import shuffle

def shuffle_word(text_list):
    text_list =list(text_list)
    shuffle(text_list)
    return "".join(text_list)

text_lists = ['idly','dosa','upma','kichdy']
result = [shuffle_word(word) for word in text_lists]
print(result)