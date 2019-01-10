# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 03:18:32 2019

@author: hp
"""
import numpy as np
from math import sqrt
import warnings
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')
'''
#Old formula
plot1 = [1,3]
plot2 = [2,5]

eucli_dist = sqrt( ( ( plot1[0]- plot2[0] )**2 ) + ( ( plot1[1]- plot2[1] )**2 )  )

print(eucli_dist)
'''
dataset = {'k':[ [1,2],[2,3],[3,1]  ],'r':[ [6,5],[7,7],[8,6]  ]}
new_features = [5,7]
'''
[ [ plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset ]
plt.scatter(new_features[0], new_features[1])
plt.show()
'''
def knn(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('k is set at a less value than the length of the data')
    distances = []
    
    for group in data:
        for features in data[group]:
            euc_dis = np.linalg.norm( np.array( features) -np.array(predict) )
            distances.append([euc_dis , group])
            
    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result


result = knn(dataset, new_features, k=3)

print(result)

[ [ plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset ]
plt.scatter(new_features[0], new_features[1], color=result)
plt.show()