import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np

def read_exel(path, sheet , collones):
    xls = pd.ExcelFile(path)
    xls.sheet_names[sheet]
    result = pd.read_excel(path, sheet_name=xls.sheet_names[sheet],  header=3, usecols=collones, engine='openpyxl')
    result = result
    print(result)
    return result

def excelToCsv(sheet):
    csvfile = 'Climat.csv'
    result = sheet.to_csv('../Data/' + csvfile, encoding='utf-8', index=False)
    return(result)

def getDataFrame(csv):
    df = pd.DataFrame(csv)
    print(df.head(10))

##def getPlotFromDataFrame(df):

def calcul_moyenne(datframe):
    print(datframe.describe(include="all"))
    #Remplacer les Nan par 0
    result = datframe.fillna(0)
    result = datframe.mean(axis=0)
    print(result)

if __name__ == '__main__':
   result = read_exel('../Data/Climat.xlsx', 1, "C:O")

   calcul_moyenne(result)

   #excelfile = read_exel('../Data/Climat.xlsx', 0)
   #excelToCsv(excelfile)
   #csvfile = pd.read_csv('../Data/Climat.csv')
   #getDataFrame(csvfile)
   