print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')
from sort_and_find import find_min_max

def main():
    n = int(input('Nhập số lượng phần tử: '))

    numbers = []
    for _ in range(n):
        number = int(input('Nhập giá trị: '))
        numbers.append(number)

    min_val, max_val = find_min_max(numbers)

    if min_val is not None and max_val is not None:
        print('Phần tử nhỏ nhất:', min_val)
        print('Phần tử lớn nhất:', max_val)
    else:
        print('Danh sách rỗng, không có giá trị lớn nhất và nhỏ nhất.')

if __name__ == "__main__":
    main()
