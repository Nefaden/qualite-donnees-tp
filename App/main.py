import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np

def read_exel(path, sheet):
    xls = pd.ExcelFile(path)
    xls.sheet_names[sheet]
    result = pd.read_excel(path, sheet_name=xls.sheet_names[sheet], engine='openpyxl')
    print(result)
    return result

def excelToCsv(sheet):
    csvfile = 'Climat.csv'
    result = sheet.to_csv('../Data/' + csvfile, encoding='utf-8', index=False)
    return(result)

def getDataFrame(csv):
    df = pd.DataFrame(csv)
    print(df.dtypes)
    getPlotFromDataFrame(df)

def getPlotFromDataFrame(df):
    df1 = pd.DataFrame(df, columns=['Jour','Température'])
    plot = df.plot(x ='Jour', y='Température', kind = 'line')
    print(plot)

if __name__ == '__main__':
   excelfile = read_exel('../Data/Climat.xlsx', 0)
   excelToCsv(excelfile)
   csvfile = pd.read_csv('../Data/Climat 2.csv')
   getDataFrame(csvfile)
   