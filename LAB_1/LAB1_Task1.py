# # Завдання 1 : Робота з текстом

def dictGen (text):
    words = text.lower().replace(",", "").replace(".", "").split()
    # Видаляємо розділові знаки та розбиваємо рядок на слова
    word_counts = {}
    for word in words: # Підраховуємо кількість повторень слів
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

text = "Text example, that includes repeated words. Words words words."
print(text)

countDict = {}
countDict = dictGen(text)
frequent_words = []

# # .items() повертає пари (ключ, значення) у вигляді ітератора, де:
# # ключ — це слово
# значення — це кількість його повторень
for word, count in countDict.items():
    if count > 3:
        frequent_words.append(word)

for word in frequent_words:
    print(f"Words that are repeated more than 3 times : {word}")