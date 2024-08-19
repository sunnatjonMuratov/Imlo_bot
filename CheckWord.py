from uzwords import words
from difflib import get_close_matches


def checkWord(word, words=words):
    word = word.lower()  # User input
    matches = set(get_close_matches(word, words))  # similar words list
    available = False

    if word in matches:  
        available = True
        matches = word

    elif 'ҳ' in word:
        word = word.replace('ҳ', 'x')
        matches.update(get_close_matches(word, words))
    elif 'x' in word:
        word = word.replace('x', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}  # print correct and similar inputs words


def notMatches(word):
    newfile = set(get_close_matches(word, words))
    does_not_match = False
    if len(newfile) == 0:
        does_not_match = True
    return does_not_match


def mavjud(input_str):
    result = checkWord(input_str)
    response = ''
    if result['available']:
        response = f'✅{input_str.capitalize()}'
    elif not result['available'] and notMatches(input_str):
        return f"'{input_str}' - Бу сўз мавжуд эмас!\nЭслатма фақат кирилча сўз ёзинг"
    elif not result['available']:
        response = f'❌{input_str.capitalize()}\n'
        for text in result['matches']:
            response += f'✅{text.capitalize()}\n'
    return response


if __name__ == '__main__':
    print(checkWord('журналистик'))
    print(checkWord('ҳўшшаймқ'))
