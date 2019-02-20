# 2. GN算法
- **算法原理**

   两个重要概念的定义：
 
   - 边介数：所有节点对之间的最短路径中经过该边的最短路径数，边介数大的边往往是连接不同community之间的边。
   - 模块度：目前常用的一种衡量网络社区结构强度的方法，可以用来定量的衡量网络社区划分质量，其值越接近1，表示网络划分出的社区结构的强度越强，也就是划分质量越好。
   因此可以通过最大化模块度Q来获得最优的网络社区划分。
   - GN算法伪代码如下：
   ```
    1) 计算当前网络的边介数和模块度Q值，并存储模块度Q值和当前网络中社团分割情况；
    2) 除去边介数最高的边；
    3) 计算当前网络的模块度Q值，如果此Q值比原来的大，则将现在的Q值和网络中社团分割情况存储更新，否则，进行下一次网络分割；
    4) 所有边分割完毕，返回当前的模块度Q值和community分割情况。

   ```
   
- **实验结果**
  
  - 网络A中聚类结果：
  
    <img src="https://github.com/lwten/Community-detection/blob/master/pic/GN-A1.png" width="50%"/>
  
  - 网络B中聚类结果：
  
    <img src="https://github.com/lwten/Community-detection/blob/master/pic/GN-B1.png" width="47%"/>
    
  - 最后的交集结果：
    
    <img src="https://github.com/lwten/Community-detection/blob/master/pic/GN-ans.png" width="30%"/>
    
  可以看到GN算法准确性不如之前，识别出来的作弊用户中，用户5被误分为作弊用户，而且GN算法复杂度较高，每次寻求最佳社区分块时，都需要计算每个点之间的最短路径。
  不过GN算法也考虑了边的权重（根据模块度进行更新），所以当处理更为复杂网络的时候，GN算法比k-clique算法更为有效。
