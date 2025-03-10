import re

tests = ["2+5i", "-3.5-6.2i", "2.71-i", "2*i+3", "-i", "4", "+5.6*i-3.2", "6+2*i"]


def parse_complex(z):
    z = z.replace("*", "")
    # handle case pure imaginary number like yi in ]-1, 1[
    match = re.match(r"^[+-]?\d*\.?\d+i$", z)
    if match:
        imag_part = match.group()
        imag_part = imag_part.split('i')[0]
        return 0, imag_part

    # case z = x + yi and pure real and pure imaginary like -i and i
    match = re.match(r"^([+-]?\d*\.?\d+)?([+-]?\d*\.?\d*)?i?$", z)
    if not match :
        part = z.split('i')
        if part[0] in ['', '+', '-'] :
            imag_part = float(part[0] + "1")
            real_part = float(part[1])
            return real_part, imag_part
        part = [s for s in part if s]
        imag, real = part
        imag_part = float(imag)
        real_part = float(real) 
        return real_part, imag_part
    if z == "i" :
        return 0, 1.0
    real, imag = match.groups()
    real_part = float(real) if real else 0
    if imag in ['+', '-']:
        imag_part = float(imag + "1")
    else:
        imag_part = float(imag) if imag else 0 
    return real_part, imag_part

print(parse_complex("-4i-4"))
# for test in tests :
#     parse_complex(test)
# for test in tests:
#     print(test)
#     parse_complex(test)