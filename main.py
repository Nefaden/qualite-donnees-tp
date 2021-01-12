import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax
#from graph import getPlotFromDataFrame

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

def read_excel(path, sheet , colonnes):
    xls = pd.ExcelFile(path)
    xls.sheet_names[sheet]
    result = pd.read_excel(path, sheet_name=xls.sheet_names[sheet], index_col=0, header=2, usecols=colonnes, engine='openpyxl')
    #getPlotFromDataFrame(result)
    return result

def calcul_moyenne(dataframe):
    print(dataframe.describe(include="all"))
    avg_month = nanmean(dataframe, axis=0)
    print("\nMoyenne par mois :\n")
    for i, avg_month in enumerate(avg_month, start=0):
        print(months[i] + " : " + str(avg_month))

def calcul_ecart_type(dataframe):
    std_month = nanstd(dataframe, axis=0)
    print("\nÉcart-type par mois :\n")
    for i, std_month in enumerate(std_month, start=0):
        print(months[i] + " : " + str(std_month))

def calcul_min_max_mois(dataframe):
    print("\nMin & max par mois :\n")
    for i, month in enumerate(months, start=0):
        print("\n{}".format(month))
        print("Min : " + str(nanmin(dataframe[:, i])))
        print("Max : " + str(nanmax(dataframe[:, i])))

if __name__ == '__main__':
   excelfile = read_excel('Data/Climat.xlsx', 0, "C:O")
   #csvfile = pd.read_csv('Data/Climat.csv')
   csvfile = genfromtxt('Data/Climat.csv', delimiter=';', dtype=float, skip_header=True)
   calcul_moyenne(csvfile)
   calcul_ecart_type(csvfile)
   calcul_min_max_mois(csvfile)
   