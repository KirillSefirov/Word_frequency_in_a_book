sa = 'Hi, my name is Di!@#$%^&*()ma, I live in Vanco1234567890uver for a year already. Damir is a Software Developer lives with me'
import helper

def get_words_frequency_in_string(inserted_string):
    inserted_string = inserted_string.lower()

    inserted_string = helper.remove_extra_symbols(inserted_string)
    all_words = inserted_string.split(' ')
    all_words.sort()
    unique_words = set(all_words)
    result = {}
    unique_words_list = list(unique_words)
    unique_words_list.sort()

    for i in range(0, len(unique_words)):
        result[unique_words_list[i]] = all_words.count(unique_words_list[i])

    print(result)

get_words_frequency_in_string(sa)