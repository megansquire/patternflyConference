#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# the programs in this series, mpl0.py - mpl4.py,
# are examples based off of Kyran Dale's book,
# "Data Visualization with Python & JavaScript"

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('codeplexCreateDates.csv', delimiter=',', skip_header=0,
                     skip_footer=0, names=['x', 'y', 'z'])
print(data)

# remove data points that are too high (spam projects)
check = (data['z'] < 1000)
data = data[check]

plt.plot(data['x'], data['z'], color='r', label='the data')
