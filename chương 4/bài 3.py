print('SV : LÊ QUANG TRUNG')
print('Mssv : 235752021610012')
s = input('Nhập chuỗi: ')
for ch in s:
    if ch not in [' ', '\t']:
        print(ch.upper())
