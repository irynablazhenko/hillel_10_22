"""
Есть фрагмент текста, состоящий из предложений.
Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным
или восклицательным знаком (или несколькими такими знаками).
Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
Предложение может состоять из одного слова.
Составить предложение из первых слов предложений фрагмента.
Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
Предложение должно заканчиваться точкой.

def generate_sentence(text: str) -> str:
  pass

"Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.." ->
 "Hello and who or yes claro."
"Hola..." -> Hola.
"""
# -------------------------------------------------------------------------------------------------
import re

text = """Hello, cocroach. And where it is? Who, can - Do it?! Or vice versa!? Yes, it's difficult... Claro..
Hola..."""


pattern = "^([A-Z][a-z]*)|[.!?] ([A-Z][a-z]*)|\n([A-Z][a-z]*)"  # слово в начале строки | слово после символов [.!?] |
# слово после переноса строки

re_obj = re.compile(pattern)
res = re_obj.findall(text)
array_data = []
for i, value in enumerate(res):
    array_data += res[i]
i = 0
words = []
for i in array_data:
    if i:
        words.append(i)

j = 1
word_case = [array_data[0]]
while j < len(words):
    word_case.append(str(words[j]).lower())  # преобразования всех слов кроме первого в нижний регистр
    j += 1

sentence = ' '.join(str(x) for x in word_case)
sentence += '.'  # Окончание предложения
print(f'Итоговое предложение: {sentence}')

assert sentence == 'Hello and who or yes claro hola.'
