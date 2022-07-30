# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = ['абв', 'выв', 'ывтс', '2312', 'фыф', 'абвавб']
print(f'Исходный текст --> {text}')
search = "абв"
new_words = []
for word in text:
    if search not in word:
        new_words.append(word)
print(f'Текст без "{search}"  --> {new_words}')
