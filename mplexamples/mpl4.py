#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# the programs in this series, mpl0.py - mpl4.py,
# are examples based off of Kyran Dale's book,
# "Data Visualization with Python & JavaScript"

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('codeplexCreateDates.csv', delimiter=',', skip_header=0,
                     skip_footer=0, names=['x', 'xlabels', 'y'])

check = (data['y'] < 1000)
data = data[check]

plt.plot(data['x'], data['y'], color='r', label='my data')
# add the correct x labels
plt.xticks(data['x'][0::12],
           data['xlabels'][0::12],
           rotation='vertical')
plt.title('Number of monthly new project registrations on CodePlex, 2006-2017')
plt.ylabel('Count of new projects')

plt.figtext(0.85, 0.75, 'potential spam', ha='right', va='bottom')

