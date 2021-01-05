import pandas as pd
import openpyxl

#climat = pd.read_csv("../data/Climat.xlsx")

def read_exel(path, sheet):
    wb = openpyxl.load_workbook(path)
    sheets = wb.sheetnames
    ws = wb[sheets[sheet]]
    #result = pd.read_excel(path, sheet_name=None, engine='openpyxl')
    #print(result)
    #return result
    print(ws)
    return ws


if __name__ == '__main__':
   result = read_exel('../Data/Climat.xlsx', 0)