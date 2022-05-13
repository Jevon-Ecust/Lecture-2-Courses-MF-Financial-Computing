
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_excel('data.xlsx')
# data=pd.read_csv
# data=pd.DataFrame(data)
print(data)
# log(price_t)-log(price_{t-1})
# 算收益要自己写
data=data.diff()
print(data)
names=data.columns
print(names)
names=names[1:-1]

# corr = data.corr(method='spearman')
corr = data.corr(method='pearson')
print(corr)

# sns.heatmap(corr)

c=corr
c[abs(corr)>0.8]=1
c[abs(corr)<=0.8]=0
c=c-np.eye(len(c))
print(c)

G= nx.from_numpy_array(np.array(c))


# # compute centrality
centrality = nx.betweenness_centrality(G)
degree = nx.degree_centrality(G)
# nx.closeness_centrality
print(degree)

pos = nx.spring_layout(G)  
nx.draw(G, pos=pos)
plt.show()


