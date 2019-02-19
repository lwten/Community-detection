# 1. clique渗透算法
- **算法原理**

  对于一个图G而言，如果其中有一个完全子图（任意两个节点之间均存在边），节点数是k，那么这个完全子图就可称为一个k-clique。

  进而，如果两个k-clique之间存在k-1个共同的节点，那么就称这两个clique是“相邻”的。
  彼此相邻的这样一串clique构成最大集合，就可以称为一个社区（而且这样的社区是可以重叠的，即所谓的overlapping community，就是说有些节点可以同时属于多个社区）。
  下面前两张图表示两个3-clique形成了一个社区，第三张图是一个重叠社区的示意图。
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/3-clique.png" width="40%" />
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/community1.png" width="37%" />
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/communitys.jpg" width="32%"/>
  
  在NetworkX中可以直接调用clique渗透算法（且是唯一一个用于社区发现的算法），使用文档如下：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/k-clique.png"  />
  
- **利用clique渗透算法构建网络A和B**

  - **构建网络A**
  
  从自己构造的数据集里构造网络A（其中用户1,2,3,8是作弊团伙）：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/clique-A1.png"  />
  
  利用clique渗透算法求出网络A中有一个community（紫色）：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/clique-A2.png"  />
 
  - **构建网络B**
  
  网络B不能直接通过数据集的数据构建，需要进行预处理，首先求出使用相同IP发送数据的用户集，统计结果如下：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/clique-B0.png"  />
  
  构建的网络B如下：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/clique-B1.png"  />
  
  利用clique渗透算法求出网络B中有一个community（青色）：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/clique-B2.png"  />
  
  最后求网络A和B中community交集（覆盖率>80%）：
  
  <img src="https://github.com/lwten/Community-detection/blob/master/pic/clique-ans.png"  />
