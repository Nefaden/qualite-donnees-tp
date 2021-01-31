import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax
from graph import getPlotFromDataFrame
from test import getPlotFromDataFrameTest

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

def statistics(dataframe):
    for i, month in enumerate(months, start=0):
        avg_month = nanmean(dataframe, axis=0)
        print("\nMoyenne par mois :\n")
        # for i, avg_month in enumerate(avg_month, start=0):
        print(months[i] + " : " + str(avg_month))

        std_month = nanstd(dataframe, axis=0)
        print("\nÉcart-type par mois :\n")
        # for i, std_month in enumerate(std_month, start=0):
        print(months[i] + " : " + str(std_month))

        print("\nMin & max par mois :\n")
        min_month = nanmin(dataframe[:, i])
        max_month = nanmin(dataframe[:, i])
        # for i, month in enumerate(months, start=0):
        print("\n{}".format(month))
        print("Min : " + str(min_month))
        print("Max : " + str(max_month))

        year_climat = dataframe[~isnan(dataframe)]
        print('\n')
        print("Year Min : " + str(nanmin(year_climat)))
        print("Year Max : " + str(nanmax(year_climat)))

        # df = pd.DataFrame(dataframe)
        # roll = df.rolling(2, win_type='triang').sum()
        # print("Rolling mean : " + roll)

        getPlotFromDataFrameTest(months, climat, avg_month, std_month, min_month, max_month)

if __name__ == '__main__':
    climat = genfromtxt('Data/Climat.csv', delimiter=';', dtype=float, skip_header=True)
    statistics(climat)
    # calcul_rolling_mean(climat)
    # getPlotFromDataFrame(months, climat)