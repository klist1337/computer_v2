
import sys
import re
from variables_types import *
dict1 = {}

def getValue(varName: str):
    for key, expr in dict1.items():
        if key == varName.lower():
            print(dict1[key])
    print(dict1)


def typesParser(varName:str):
    getValue(varName)
 
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
        dict1[varName.lower()] = expr
        typesParser(varName)
        # print(dict1)
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