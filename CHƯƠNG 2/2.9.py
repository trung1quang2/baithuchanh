print('Lê Quang Trung')
print('mã sv : 235752021610012')
string = input("Nhập vào một chuỗi ký tự: ")

char_count = {}

for char in string:

    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Số lần xuất hiện của các ký tự trong chuỗi:", char_count)
