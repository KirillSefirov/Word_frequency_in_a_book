

def remove_extra_symbols(inserted_string):
    inserted_string = inserted_string.replace('!', '')
    inserted_string = inserted_string.replace('@', '')
    inserted_string = inserted_string.replace('#', '')
    inserted_string = inserted_string.replace('$', '')
    inserted_string = inserted_string.replace('%', '')
    inserted_string = inserted_string.replace('^', '')
    inserted_string = inserted_string.replace('&', '')
    inserted_string = inserted_string.replace('*', '')
    inserted_string = inserted_string.replace('(', '')
    inserted_string = inserted_string.replace(')', '')
    inserted_string = inserted_string.replace('`', '')
    inserted_string = inserted_string.replace('~', '')
    inserted_string = inserted_string.replace('{', '')
    inserted_string = inserted_string.replace('}', '')
    inserted_string = inserted_string.replace('[', '')
    inserted_string = inserted_string.replace(']', '')
    inserted_string = inserted_string.replace(';', '')
    inserted_string = inserted_string.replace(':', '')
    inserted_string = inserted_string.replace("'", '')
    inserted_string = inserted_string.replace('"', '')
    inserted_string = inserted_string.replace('<', '')
    inserted_string = inserted_string.replace('>', '')
    inserted_string = inserted_string.replace(',', '')
    inserted_string = inserted_string.replace('.', '')
    inserted_string = inserted_string.replace('/', '')
    inserted_string = inserted_string.replace('?', '')
    inserted_string = inserted_string.replace('\/', '')
    inserted_string = inserted_string.replace('№', '')
    inserted_string = inserted_string.replace('+', '')
    inserted_string = inserted_string.replace('=', '')
    inserted_string = inserted_string.replace('1', '')
    inserted_string = inserted_string.replace('2', '')
    inserted_string = inserted_string.replace('3', '')
    inserted_string = inserted_string.replace('4', '')
    inserted_string = inserted_string.replace('5', '')
    inserted_string = inserted_string.replace('6', '')
    inserted_string = inserted_string.replace('7', '')
    inserted_string = inserted_string.replace('8', '')
    inserted_string = inserted_string.replace('9', '')
    inserted_string = inserted_string.replace('0', '')
    inserted_string = inserted_string.replace('-', '')
    return inserted_string
