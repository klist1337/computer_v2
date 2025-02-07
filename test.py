import re

pattern = r"^([+-]?\d*\.?\d+)?([+-]?(?:\d*\.?\d*\*?i|i\*\d*\.?\d+))?$"

def extract_parts(complex_str):
    match = re.match(pattern, complex_str)
    if match:
        real_part = match.group(1) 
        imaginary_part = match.group(2)
        if real_part is None:
            real_part = "0"
        if imaginary_part is None:
            imaginary_part = "0"
        return real_part, imaginary_part
    return "Error"


tests = ["2+5i", "-3.5-6.2i", "2.71-i", "i*2+3", "-i", "4", "+5.6*i-3.2", "6+2*i"]

for test in tests:
    result = extract_parts(test)
    if result != "Error" :
        print(f"{test}: real= {result[0]} imaginary = {result[1]}")
    else:
        print(f"{test}: error")