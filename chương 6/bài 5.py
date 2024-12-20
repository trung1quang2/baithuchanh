print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')
class ReverseWords:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

input_string = "hello .py"

reverse = ReverseWords(input_string)

output = reverse.reverse_words()
print(f"Kết quả sau khi đảo ngược: '{output}'")
