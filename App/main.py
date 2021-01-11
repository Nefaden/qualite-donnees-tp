import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np

def read_excel(path, sheet , colonnes):
    xls = pd.ExcelFile(path)
    xls.sheet_names[sheet]
    result = pd.read_excel(path, sheet_name=xls.sheet_names[sheet], index_col=0, header=2, usecols=colonnes, engine='openpyxl')
    result.head()
    getPlotFromDataFrame(result)
    return result

def excelToCsv(sheet):
    csvfile = 'Climat.csv'
    result = sheet.to_csv('../Data/' + csvfile, encoding='utf-8', index=False)
    return(result)

def getDataFrame(csv):
    df = pd.DataFrame(csv)
    print(df.head(10))

def calcul_moyenne(dataframe):
    print(dataframe.describe(include="all"))
    #Remplacer les Nan par 0
    result = dataframe.fillna(0)
    result = dataframe.mean(axis=0)
    print(result)

def getPlotFromDataFrame(df):
    df1 = pd.DataFrame(df, columns=['Janvier'])
    print(df1)
    df1.plot(x ='Jour', y='Température', kind = 'line')
    plt.show()

if __name__ == '__main__':
   result = read_excel('../Data/Climat.xlsx', 0, "C:O")

   calcul_moyenne(result)

   #excelfile = read_excel('../Data/Climat.xlsx', 0)
   #excelToCsv(excelfile)
   #csvfile = pd.read_csv('../Data/Climat.csv')
   #getDataFrame(csvfile)
   