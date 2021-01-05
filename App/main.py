import pandas as pd
import openpyxl

#climat = pd.read_csv("../data/Climat.xlsx")

def read_exel(path, sheet):
    xls = pd.ExcelFile(path)
    xls.sheet_names[sheet]
    result = pd.read_excel(path, sheet_name=xls.sheet_names[sheet], engine='openpyxl')
    print(result)
    return result


if __name__ == '__main__':
   result = read_exel('../Data/Climat.xlsx', 0)