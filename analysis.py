import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import is_numeric_dtype

cwd = os.getcwd()
data_dir = os.path.join(cwd, "data")
train_df = pd.read_csv(os.path.join(data_dir,"train.csv"))
greeks_df = pd.read_csv(os.path.join(data_dir, "greeks.csv"))

merge_df = pd.merge(left=train_df, right=greeks_df, how="left", on="Id")

for col in merge_df.columns:
    if merge_df[col].isna().any():
        print(col)
        print(f"Null values : {merge_df[col].isna().sum()}")

##null values:
# BQ
# CB
# CC
# DU
# EL
# FC
# FL
# FS
# GL

for col in merge_df.columns:
    if is_numeric_dtype(merge_df[col]):
        plt.figure(figsize=(18,10))
        plt.suptitle(f"{col}")
        plt.subplot(2,2,1)
        sns.histplot(merge_df[col])
        plt.subplot(2,2,2)
        sns.boxplot(merge_df[col])
        plt.subplot(2,2,3)
        sns.boxplot(x="Class", y=col, data=merge_df)
        plt.subplot(2,2,4)
        sns.kdeplot(hue="Class", x=col, data=merge_df, shade=True, alpha=0.75)
        plt.tight_layout()

        plt.show()

#AB Class 1 has more extreme values compared to 0 but not clearly distinguishable
#potential outlier

#AF extreme values have class 1

#AM check 600 value class 0

#AR check extreme values > 150

#AX check extreme vlue > 30

#AY have mostly zero values with some higher numbers

#BC have mostly 0 but class 1 have > 100

#BD > 10000 Class 1

#BQ class 1 median higher shift 50 - 150

#BR mostly 0 with extreme values > 50K - 1l

#CR, DA, DE slight median shift Class 1

#DI, DU slight higher median and high var Class 1

#EL many same high value

#FC, FD, FR (0), FS many small values

#GE extreme right skew, GF right skew

#GL bimodal








