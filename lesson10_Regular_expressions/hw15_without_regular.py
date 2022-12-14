text = 'Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it`s difficult... Claro..'
text2 = 'Holla....'


def get_sentenses_from_text(text: str) -> list:
    symbols = ['.', '!', '?']
    sentences = []
    sentence = ''
    for s in text:
        if s not in symbols:
            sentence += s
        else:
            sentences.append(sentence)
            sentence = ''
    return [sentence.strip() for sentence in sentences if sentence]


def get_first_word_from_sentence(sentence: str) -> str:
    first_word = ''
    for s in sentence:
        if s.isalpha():
            first_word += s
        else:
            break
    return first_word


def generate_sentence(text: str) -> str:
    result = ''
    words = [get_first_word_from_sentence(sentence) for sentence in get_sentenses_from_text(text)]
    if words:
        result = ' '.join(words).capitalize()
    return result + '.'


print(generate_sentence(text))
print(generate_sentence(text2))