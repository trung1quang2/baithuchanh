print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')
class RomanToInteger:
    def __init__(self):
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    
    def convert(self, roman: str) -> int:
        total = 0
        prev_value = 0

        for char in reversed(roman):
            current_value = self.roman_map[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            prev_value = current_value
        
        return total

roman_converter = RomanToInteger()

roman_number = "IX" 
print(f"Số La Mã {roman_number} tương ứng với số nguyên: {roman_converter.convert(roman_number)}")

roman_number = "MCMXCIV" 
print(f"Số La Mã {roman_number} tương ứng với số nguyên: {roman_converter.convert(roman_number)}")
