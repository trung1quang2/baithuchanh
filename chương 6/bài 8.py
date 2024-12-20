print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')
class ATM:
    def __init__(self):
        self.balance = 9000 

    def check_balance(self):
        print(f"Số dư tài khoản của bạn là: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} VND vào tài khoản. Số dư hiện tại là: {self.balance} VND")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        elif amount > self.balance:
            print("Số dư không đủ để rút tiền.")
        else:
            self.balance -= amount
            print(f"Đã rút {amount} VND. Số dư còn lại: {self.balance} VND")

    def exit(self):
        print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
        exit()

def atm_system():
    atm = ATM()
    
    while True:
        print("\n----- ATM -----")
        print("1. Kiểm tra số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Thoát")
        
        try:
            choice = int(input("Chọn một tùy chọn (1-4): "))
            
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Nhập số tiền bạn muốn nạp: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Nhập số tiền bạn muốn rút: "))
                atm.withdraw(amount)
            elif choice == 4:
                atm.exit()
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số hợp lệ.")
        
atm_system()
