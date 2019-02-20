# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import community

def CreateGraph_A(f):
    G = nx.MultiDiGraph()
    head = f.readline().split()
    print(head)
    attr_len = len(head)-2
    line = f.readline().split()

    while line:
#        print(line)
        num = G.number_of_edges(line[0], line[1])
        G.add_edge(line[0], line[1])
        for i in range(attr_len):
            G[line[0]][line[1]][num][head[i+2]] = line[i+2]
        line = f.readline().split()
#        
    return G

def addtwodimdict(thedict, IP, node): 
    if IP in thedict:
        if node in thedict[IP]:
            thedict[IP][node]=thedict[IP][node]+1
        else:
            thedict[IP][node]=1
    else:
        thedict.update({IP:{node: 1}})

def CreateGraph_B(f):
    G = nx.MultiGraph()
    head = f.readline().split()
    line = f.readline().split()
    mapdict = dict()
    
    while line:
        addtwodimdict(mapdict, line[2], line[0])
        line = f.readline().split()
        
    for IP in mapdict.keys():
        print( IP, ":" , mapdict[IP])
        nodes = list( mapdict[IP].keys() )
        for i in range(len(nodes)):
            for j in range(i+1,len(nodes)):
#                print(nodes[i],nodes[j],min(mapdict[IP][str(nodes[i])],mapdict[IP][str(nodes[j])]))
                num = G.number_of_edges(nodes[i], nodes[j])
                G.add_edge(nodes[i], nodes[j])
                G[nodes[i]][nodes[j]][num]["share_IP"]=IP
                G[nodes[i]][nodes[j]][num]["coun"]=min(mapdict[IP][str(nodes[i])],mapdict[IP][str(nodes[j])])
     
    return G

if __name__ == "__main__":
     #-------读取文件并构建网络A-------#
     f = open('data.txt')
     A = CreateGraph_A(f)
     
     print("---------------------------------------------------------------------------------------------------------")
     print("Network A is shown as follow:")
     pos = nx.shell_layout(A)
     nx.draw(A, pos, with_labels = True)
     plt.show()
     
     print("---------------------------------------------------------------------------------------------------------")
     print("The edge information of Network A is as follow:")
     print(A.edges(data=True))
     print("---------------------------------------------------------------------------------------------------------")
     
     #-------发现网络A中的community-------#
     for u in A.edges:
         print(u)
     G = nx.Graph(A)
     pos = nx.shell_layout(G)
     nx.draw(G, pos, with_labels = True)
     plt.show()
     
     partition = community.best_partition(A)

     #drawing
     size = float(len(set(partition.values())))
     pos = nx.shell_layout(G)
     count = 0.
     for com in set(partition.values()) :
         count = count + 1.
         list_nodes = [nodes for nodes in partition.keys()
                                     if partition[nodes] == com]
         print(list_nodes)
         nx.draw_networkx_nodes(G, pos, list_nodes, 
                                    node_color = str(count / size))
    
    
     nx.draw_networkx_edges(G,pos, alpha=0.5)
     plt.show()  
     
     
#     H = nx.MultiGraph(A) # convert G to undirected graph
#     c_A = list(nx.k_clique_communities(H, 4))#查找具有社团结构的网络：地图，最小团块大小 ：完全连接K个节点的子图
#     print("Network A has", len(c_A) , "communitys!")
#     print("The information of communitys are as follow:")
#     #pos = nx.spring_layout(G)
#     
#     #-------community可视化-------#
#     nx.draw_networkx_nodes(A,pos)
#     count = 0
#     color = ['m','g','c','b','y','k','w']
#     for com in c_A :
#         count = count + 1
#         list_nodes = list(com)               
#         nx.draw_networkx_nodes(A, pos, list_nodes, node_color = color[count-1])
#         print("Community",count,"is:",list_nodes)
#     
#     nx.draw_networkx_edges(A,pos)
#     nx.draw_networkx_labels(A,pos)
#     plt.show()
#     print("---------------------------------------------------------------------------------------------------------")
#
#
#     #-------读取文件并构建网络B-------#
#     f = open('data.txt')
#     B = CreateGraph_B(f)
#     
#     print("---------------------------------------------------------------------------------------------------------")
#     print("Network B is shown as follow:")
#     pos = nx.shell_layout(B)
#     nx.draw(B, pos, with_labels = True)
#     plt.show()
#     
#     print("---------------------------------------------------------------------------------------------------------")
#     print("The edge information of Network B is as follow:")
#     print(B.edges(data=True))
#     print("---------------------------------------------------------------------------------------------------------")
#     
#     #-------发现网络B中的community-------#
#     c_B = list(nx.k_clique_communities(B, 5))#查找具有社团结构的网络：地图，最小团块大小 ：完全连接K个节点的子图
#     print("Network B has", len(c_B) , "communitys!")
#     print("The information of communitys are as follow:")
#     #pos = nx.spring_layout(G)
#     
#     #-------community可视化-------#
#     nx.draw_networkx_nodes(B,pos)
#     count = 0
#     color = ['c','g','b','m','y','k','w']
#     for com in c_B :
#         count = count + 1
#         list_nodes = list(com)               
#         nx.draw_networkx_nodes(B, pos, list_nodes, node_color = color[count-1])
#         print("Community",count,"is:",list_nodes)
#     
#     nx.draw_networkx_edges(B,pos)
#     nx.draw_networkx_labels(B,pos)
#     plt.show()
#     print("---------------------------------------------------------------------------------------------------------")
#     
#     #-------A和B的community交集-------#
#     ans = []
#     for comA in c_A:
#         for comB in c_B:
#             tmp = list(set(comA).intersection(set(comB)))
#             if(len(tmp)>=(len(comA)*0.8)):
#                 ans.append(tmp)             
#     print("The cheat gruops are as follow:")
#     for i in ans:
#        print(i)
#    
#     print("---------------------------------------------------------------------------------------------------------")