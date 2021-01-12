import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax

csvfile = pd.read_csv('../Data/Climat.csv')
getPlotFromDataFrame(csvfile)

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

def getPlotFromDataFrame(csvfile):
    df = pd.DataFrame(csvfile, columns=['Jour','Température'])
    print(df)
    df.index.name='Jour'
    df['Jour']=df.index
    df = df.reset_index(drop=True)
    df.plot(x ='Jour', y='Température', kind = 'line')
    #plt.show()
