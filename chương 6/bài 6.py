print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')
class StringManipulator:
    def __init__(self):
        self.input_string = ""     
    def get_String(self):
        self.input_string = input("Nhập chuỗi: ")
    
    def print_String(self):
        print(self.input_string.upper())

string_manipulator = StringManipulator()

string_manipulator.get_String()

string_manipulator.print_String()
