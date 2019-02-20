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

def list2dict(a):
    b = {}
    cnt = 0
    for com in a:
        for i in com:
            b[i]=cnt
        cnt = cnt + 1
    
    return b

def GN(G):
    G_cloned = G.copy()
    G_tmp = G.copy()
    partition = [[n for n in G.nodes()]]
    max_Q = 0.0
    
    while len(G_tmp.edges()) != 0:
        edge = max(nx.edge_betweenness(G_tmp).items(),key=lambda item:item[1])[0]
        G_tmp.remove_edge(edge[0], edge[1])
        components = [list(c) for c in list(nx.connected_components(G_tmp))]
#        print( len(G_tmp.edges()))
        if len(components) != len(partition):
            components_tmp = list2dict(components)
            cur_Q = community.modularity(components_tmp, G_cloned, weight='weight')
#            print(cur_Q)
            if cur_Q > max_Q:
                max_Q = cur_Q
                partition = components
    print ("max_Q = ", max_Q)
#    print ("partitions are: ", partition)
    return partition




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

     G = nx.Graph(A)
     for u,v in G.edges():
         G[u][v]['weight'] = A.number_of_edges(u,v) + A.number_of_edges(v,u)
#     print(G.edges(data=True))
    
     pos = nx.shell_layout(G)
     nx.draw(G, pos, with_labels = True)
     plt.show()
     
#     partition_A = community.best_partition(G)
     partition_A = GN(G)
     
     #drawing
     print("Network A has", len(partition_A) , "communitys!")
     print("The information of communitys are as follow:")
     #pos = nx.spring_layout(G)
     
     #-------community可视化-------#
     nx.draw_networkx_nodes(G,pos)
     count = 0
     color = ['m','g','c','b','y','k','w']
     for com in partition_A :
         count = count + 1
         list_nodes = list(com)               
         nx.draw_networkx_nodes(G, pos, list_nodes, node_color = color[count-1])
         print("Community",count,"is:",list_nodes)
     
     nx.draw_networkx_edges(G,pos)
     nx.draw_networkx_labels(G,pos)
     plt.show()
     print("---------------------------------------------------------------------------------------------------------")



     #-------读取文件并构建网络B-------#
     f = open('data.txt')
     B = CreateGraph_B(f)
     
     print("---------------------------------------------------------------------------------------------------------")
     print("Network B is shown as follow:")
     pos = nx.shell_layout(B)
     nx.draw(B, pos, with_labels = True)
     plt.show()
     
     print("---------------------------------------------------------------------------------------------------------")
     print("The edge information of Network B is as follow:")
     print(B.edges(data=True))
     print("---------------------------------------------------------------------------------------------------------")
     
     #-------发现网络A中的community-------#

     G2 = nx.Graph(B)
     for u,v in G2.edges():
         G2[u][v]['weight'] = 0
         a = 2
         b = 0.5
         for i in range(B.number_of_edges(u,v)):
             G2[u][v]['weight'] = G2[u][v]['weight'] + a * 1 + b * B[u][v][i]['coun']
#     print(G2.edges(data=True))
     
#     partition_B = community.best_partition(G2)

     partition_B = GN(G2)
     
     #drawing
     print("Network B has", len(partition_B) , "communitys!")
     print("The information of communitys are as follow:")
     #pos = nx.spring_layout(G)
     
     #-------community可视化-------#
     nx.draw_networkx_nodes(G2,pos)
     count = 0
     color = ['m','g','c','b','y','k','w']
     for com in partition_B :
         count = count + 1
         list_nodes = list(com)               
         nx.draw_networkx_nodes(G2, pos, list_nodes, node_color = color[count-1])
         print("Community",count,"is:",list_nodes)
     
     nx.draw_networkx_edges(G2,pos)
     nx.draw_networkx_labels(G2,pos)
     plt.show()
     print("---------------------------------------------------------------------------------------------------------")

    
     #-------A和B的community交集-------#
     ans = []
     for comA in partition_A:
         for comB in partition_B:
             tmp = list(set(comA).intersection(set(comB)))
             if(len(tmp)>1 and len(tmp)>=(len(comA)*0.8)):
                 ans.append(tmp)             
     print("The cheat gruops are as follow:")
     for i in ans:
        print(i)
    
     print("---------------------------------------------------------------------------------------------------------")