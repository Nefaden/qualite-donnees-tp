import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def getPlotFromDataFrame(df):
    df1 = pd.DataFrame(df, columns=['Janvier'])
    print(df1)
    df1.plot(x ='Jour', y='Température', kind = 'line')
    plt.show()