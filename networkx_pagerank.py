import networkx as nx
import matplotlib.pyplot as plt 

G = nx.DiGraph()
edges = [("A","B"),("A","C"),("A","D"),("B","A"), ("B","D"),("C","A"),("D","B"),("D","C")]

for edge in edges:
    G.add_edge(edge[0], edge[1])

#有向图可视化
layout = nx.spring_layout(G)
nx.draw(G, pos = layout, with_labels= True, hold = False)
plt.show()

#计算简化模型的PR值
pr = nx.pagerank(G, alpha = 1)
print("简化模型的PR值： ", pr)

#计算随机模型的PR值
pr = nx.pagerank(G, alpha = 0.85)
print("随机模型的PR值： ", pr)