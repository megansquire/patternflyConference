#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# the programs in this series, mpl0.py - mpl4.py,
# are examples based off of Kyran Dale's book,
# "Data Visualization with Python & JavaScript"
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('codeplexCreateDates.csv', delimiter=',', skip_header=0,
                     skip_footer=0, names=['x', 'xlabels', 'y'])

# remove points that are too high
check = (data['z'] < 1000)
data = data[check]

plt.plot(data['x'], data['y'], color='r', label='the data')

# add customizations
plt.title('Number of monthly new project registrations on CodePlex, 2006-2017')
plt.xlabel('Month Number')
plt.ylabel('Count of new projects')
plt.figtext(0.85, 0.75, 'potential spam', ha='right', va='bottom')
