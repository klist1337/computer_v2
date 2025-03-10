
import sys
import re
from variables_types import *
from helper import *
dict1 = {}

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

def getval(var_name:str):
    for key, expr in dict1.items():
        if key.replace(' ', '') == var_name.lower():
            return dict1[key]
    return "not defined"

def parsertype(expr: str):
    withoutSpc = re.sub("\s", "", expr)
    print(withoutSpc)
    pattern = r"^[+-]?\d*\.?\d+(?:[+-]\d*\.?\d*\*?i)?$|^[+-]?\d*\.?\d*\*?i(?:[+-]\d*\.?\d+)?$|^[+-]?i(?:\*\d*\.?\d+)?(?:[+-]\d*\.?\d+)?$"

    if re.fullmatch(pattern, withoutSpc):
        #invalide complexe type ix + u    
       match = re.match(r"^([+-]?i\*\d*\.?\d*)([+-]?\d*\.?\d+)$", withoutSpc)
       if match:
            return types.NOTVALID, withoutSpc
       return [types.COMPLEX, withoutSpc]
    return expr

def getValue(varName: str, expr):
    for key, expr in dict1.items():
        if key == varName.lower():
            value = dict1[key]
            # print(value)
            return value
    # print(dict1)
    return expr

def get_types(varName:str, expr:str):
    parsingType = parsertype(expr)
    match parsingType[0]:
        case types.COMPLEX:
            real, imag = parse_complex(parsingType[1])
            return ComplexNumber(real, imag)
        case types.NOTVALID:
            return "not a valid type"
        case _:
            return "number or funtion or matrice"

def replace_in_dict(expr: str, var_name: str) :
    for key, value in dict1.items():
        print(f"{var_name} -- {value}")
        if var_name.lower() == value.replace(' ', ''):
            dict1[key] = expr

def parser(input: str):
    if input.find('=', 0) == -1 :
        print("Please make an assignment")
        return
    arr = input.split('=')
    arr = [s for s in arr if s]
    if len(arr) > 1:
        if arr[1].isspace() == True :
            print("The assignment value should'nt be empty")
            return
        varName = input.split('=')[0]
        expr = input.split('=')[1]
        parts = re.findall(r"(\w+)", expr)
        # replace expr by his value inside dictionnary if it already exist
        # replace_in_dict(expr, varName)
        # replace all variable inside expression by they value if they exist already
        new_expr = expr
        for part in parts:
            print(part)
            if getval(part) != "not defined" :
                repl = getval(part)
                new_expr = expr.replace(part, repl, len(part))
                dict1[varName.lower()] = new_expr
        #we need to check the value of variable before assignement
        dict1[varName.lower()] = new_expr
        # replace_in_dict(expr, varName)
        value = getValue(varName, new_expr)
        # print(eval(value))
        
        # print(value)

        value = get_types(varName, expr)
        print(value)
        print(dict1)
    else:
        print("The assignment value should'nt be empty")
        return

def main() :
        while (1):
            try :
                print(">", end=' ')
                input_string = input()
                if input_string == "quit" or input_string == "exit":
                    break
                parser(input_string)
            except KeyboardInterrupt:
                print('\n', end='')
                print('quit')
                break
            except EOFError:
                print('\n', end='')
                print('quit')
                break

if __name__ == "__main__":
    main()