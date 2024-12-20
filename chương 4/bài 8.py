print('SV : LÊ QUANG TRUNG')
print('Mssv : 235752021610012')
words = input('Nhập dãy các từ: ').split()

max_length = max(len(word) for word in words)

longest_words = [word for word in words if len(word) == max_length]

print('Từ dài nhất và các từ có cùng độ dài nhất:')
for word in longest_words:
    print(word)
