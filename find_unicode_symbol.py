import sys
import unicodedata


# Set defaults for the range of code points to search
START_CP, END_CP = ord(' '), sys.maxunicode + 1 


def find(*query_words, start=START_CP, end=END_CP):
    query = {word.upper() for word in query_words}
    word_part = query_words[0].upper() if len(query_words) == 1 else None

    for code_point in range(start, end):
        # Get the Unicode character for code
        char = chr(code_point)
        # Get the name of the character, or None if the code point is unassigned
        name = unicodedata.name(char, None)

        if name and (query.issubset(name.split()) or word_part in name):
            print(f'U+{code_point:04X}\t{char}\t{name}')


def main(words):
    if words:
        find(*words)
    else:
        print('Please provide words to find')


if __name__ == '__main__':
    main(sys.argv[1:])

