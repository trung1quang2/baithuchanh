print ('sinh viên: LÊ QUANG TRUNG')
print(' MSSV: 235752021610012')
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        """Khởi tạo đối tượng Hinhchunhat với chiều dài và chiều rộng"""
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        """Tính diện tích của Hinhchunhat"""
        return self.chieu_dai * self.chieu_rong

hinh_chu_nhat = Hinhchunhat(5, 3)

print("Diện tích của hình chữ nhật là:", hinh_chu_nhat.dien_tich())
