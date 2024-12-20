print('SV : LÊ QUANG TRUNG')
print('Mssv : 235752021610012')
s = input('Nhập chuỗi: ')

new_s = ''.join([ch for ch in s if not ch.isdigit()])

print('Chuỗi mới:', new_s)
