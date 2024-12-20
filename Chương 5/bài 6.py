print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')
def sort_list(lst):
    """Sắp xếp danh sách theo thứ tự tăng dần"""
    return sorted(lst)

def find_max(lst):
    """Tìm phần tử lớn nhất trong danh sách"""
    return max(lst)

def find_min(lst):
    """Tìm phần tử nhỏ nhất trong danh sách"""
    return min(lst)

def find_max_index(lst):
    """Tìm vị trí của phần tử lớn nhất trong danh sách"""
    max_value = max(lst)
    return lst.index(max_value)

def find_min_index(lst):
    """Tìm vị trí của phần tử nhỏ nhất trong danh sách"""
    min_value = min(lst)
    return lst.index(min_value)
