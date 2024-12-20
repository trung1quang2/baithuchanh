print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')
import numpy as np

students = np.array([
    ('Nguyen Van A', 1.75, 'Lop 10'),
    ('Tran Thi B', 1.62, 'Lop 11'),
    ('Le Van C', 1.80, 'Lop 12'),
    ('Pham Thi D', 1.55, 'Lop 10')
], dtype=[('name', 'U20'), ('height', 'f4'), ('class', 'U10')])

sorted_students = np.sort(students, order='height')

print("Danh sách sinh viên sắp xếp theo chiều cao:")
for student in sorted_students:
    print(student)
