import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax
from graph_error import getPlotFromDataFrame

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

def calcul_moyenne(dataframe):
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

def calcul_min_max_annee(dataframe):
    year_climat = dataframe[~isnan(dataframe)]
    print('\n')
    print("Year Min : " + str(nanmin(year_climat)))
    print("Year Max : " + str(nanmax(year_climat)))

if __name__ == '__main__':
    climat = genfromtxt('../Data/Climat-erreur.csv', delimiter=';', dtype=float, skip_header=True)
    np.nan_to_num(climat, nan=0, posinf=35, neginf=-10)
    calcul_moyenne(climat)
    calcul_ecart_type(climat)
    calcul_min_max_mois(climat)
    calcul_min_max_annee(climat)
    getPlotFromDataFrame(months, climat)