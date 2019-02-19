# Community-detection
复杂网络中的几种社区发现算法

## 构造问题及数据集toy
  网络中节点1，2，3，4都是用户，用户之间可能互相给对方发数据，每个人发不发和给谁发都是随机。
  假设我们认为谁收到的数据最多为胜者，那这个时候可能存在作弊的用户。
  一些作弊用户使用同一个ip地址通过一直互相发数据来取得比赛胜利。
  
  数据集如data.txt所示，解题思路如下：
  构建两个网络A，B，网络A以发数据作为edge，网络B以相同IP作为edge。
  即网络A中，edge的两端是发送方和接收方的关系，而在网络B中，edge的两端是两个IP相同的用户。
  根据community detection的思路，网络A的community是那些发数据较为频繁的用户集合，网络B中的community是IP较为集中的用户集合。
  如果A和B中community的重合率很高的话，那么它们就有可能是作弊用户。
  
  通过NetworkX构建有向图，那么网络A中edge的属性应该为count（连接次数）和amount（金额）。
  网络B中应该不带任何属性，只要两个节点曾经用过相同的IP，那么两者之间即有一条edge。
  利用NetworkX构建多重有向图，发送次数通过计算边的重数可得。
  构造网络具体说明：
  - 网络A（多重有向图）的节点为各用户，如果用户1以IP（255.255.255.0）向用户2发送金额为30的数据，那么添加一条有向边（用户1→用户2），边强度为30。
  - 网络B（多重无向图）的节点为各用户，如果用户1以IP（255.255.255.0）向其他用户发送了5次数据，用户2以同样IP（255.255.255.0）向其他用户发送了2次数据，那么添加一条无向边（用户1—用户2），边强度为min（5,2）=2。
  
  
## 1. clique渗透算法
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
