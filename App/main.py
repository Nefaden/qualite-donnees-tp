import pandas as pd

#climat = pd.read_csv("../data/Climat.xlsx")

def read_exel(path, sheet):
    result = pd.read_excel(path, sheet_name=None, engine='openpyxl')
    print(result)
    return result


if __name__ == '__main__':
    read_exel('../Data/Climat.xlsx', 'SI')