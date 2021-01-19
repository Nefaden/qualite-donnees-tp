import mplcursors
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from matplotlib.widgets import Button
import numpy as np
from numpy import isnan, nanmin, nanmax, searchsorted, arange, array, append
# from cursor import SnaptoCursor

def getPlotFromDataFrame(months, climat):    
    year_array = array([])
    for i, month in enumerate(months, start=0):
        year_array = append(year_array, climat[:, i])
    year_array = year_array[~isnan(year_array)]

    month = 0
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)    
    plt.figure(num='Température Climat sans erreur')
    title = plt.title(f"Température du mois de {months[month]}")
    plt.xlabel('Jours')
    plt.ylabel('Température')
    
    plt.axis([1, 31, nanmin(year_array)-5, nanmax(year_array)+5])
    plt.grid(True)
    plot, = plt.plot(range(1, 32, 1), climat[:, month], "b:o", lw=2)

    class Index:
        ind = 0

        def next(self, event):
            if self.ind < 11:
                self.ind += 1
                title.set_text(f"Température du mois de {months[self.ind]}")
                plot.set_ydata(climat[:, self.ind])
                plt.draw()
            elif self.ind == 11:
                self.ind += 1
                title.set_text(f"Température sur l'année")
                x = [x for x in arange(365) if x%30==0 ]
                ax.set_xlim(right=365)
                ax.set_xticks(x)   
                ax.set_xticklabels(x)
                plot.set_xdata(range(0, len(year_array), 1))
                plot.set_ydata(year_array)
                plt.draw()

        def prev(self, event):
            if self.ind > 0:
                self.ind -= 1
                title.set_text(f"Température du mois de {months[self.ind]}")
                plot.set_ydata(climat[:, self.ind])
                if self.ind == 11:
                    x = [x for x in arange(31) if x%5==0 ]
                    ax.set_xlim(right=32)
                    ax.set_xticks(x)
                    ax.set_xticklabels(x)
                    plot.set_xdata(range(1, 32, 1))
                plt.draw()

    callback = Index()
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)

    # #cursor = Cursor(ax)
    # cursor = SnaptoCursor(plot, plot.get_xdata, plot.get_ydata)
    # cid =  plt.connect('motion_notify_event', cursor.mouse_move)

    plt.show()