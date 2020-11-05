import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs
from numpy import NaN
import seaborn as sns

def percent_to_int(dfs, cols):
    for df in dfs:
        for col in cols:
            df[col] = pd.to_numeric(df[col].map(lambda x: x.lstrip('+-').rstrip('%')))
    return dfs

def make_boxplots(df1, df2, lst_of_cols, label1='2019', label2='2020'):
    for i, ax in enumerate(axs.flatten()):
        ax.boxplot([df1[lst_of_cols[i]], df2[lst_of_cols[i]]])
        ax.set_xticks([1,2])
        ax.set_xticklabels([labe1, label2])
        ax.set_ylabel(lst_of_cols[i])

    fig.suptitle('Season to season comparison, 60 games', size=16)
    plt.tight_layout()
    fig.subplots_adjust(top=0.92)