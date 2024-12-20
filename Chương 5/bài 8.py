print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')

def Sequential_Search(dlist, item):
    """Hàm tìm kiếm tuyến tính"""
    for index, element in enumerate(dlist):
        if element == item:
            return True, index
    return False, -1
