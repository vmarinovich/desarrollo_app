#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:23:42 2020

@author: vladmarinovich
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importar el data set 
dataset = pd.read_csv("zdata.csv")
x = dataset.iloc [:, :-1].values
y = dataset.iloc [:, 3]. values

# tratamiento de los NAs

from sklearn.preprocessing import imputer
imputer = imputer(missing_values =  "nan", strategy = "mean", axis =0)
imputer = imputer.fit(x[:, 1:3]) 
x[:, 1:3] = imputer.transform(x[:, 1:3])

