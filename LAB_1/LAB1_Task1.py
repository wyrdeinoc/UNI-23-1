# # �������� 1 : ������ � �������

def dictGen (text):
    words = text.lower().replace(",", "").replace(".", "").split()
    # ��������� ������� ����� �� ��������� ����� �� �����
    word_counts = {}
    for word in words: # ϳ��������� ������� ��������� ���
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

# # .items() ������� ���� (����, ��������) � ������ ���������, ��:
# # ���� � �� �����
# �������� � �� ������� ���� ���������
for word, count in countDict.items():
    if count > 3:
        frequent_words.append(word)

for word in frequent_words:
    print(f"Words that are repeated more than 3 times : {word}")