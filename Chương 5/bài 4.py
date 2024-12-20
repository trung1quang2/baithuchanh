print('Sinh viên: Lê Quang Trung')
print("Mã số SV: 235752021610012")

import numpy as np

def main():
    array = np.arange(12, 38)
    print("Mảng được tạo:")
    print(array)
    
    reversed_array = array[::-1]
    print("Mảng đảo ngược:")
    print(reversed_array)

if __name__ == "__main__":
    main()
