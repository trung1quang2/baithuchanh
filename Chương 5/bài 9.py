print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')

def binary_search(arr, x):
    """Hàm tìm kiếm nhị phân"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return True

    return False
