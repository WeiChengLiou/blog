title: 台灣公司關係圖
date: 2014-08-06 23:43
comments: true
slug: twcom
tags: 台灣公司關係圖
category: 台灣公司關係圖


## 從董監事名單觀察法人投資關係

台灣的企業種類分佈相當廣泛，有政府經營的國營企業、廣大的中小企業，家族企業為背景的財團，還有黨營事業，這些不同的市場參與者組成了現今的企業生態圈。但對於檯面上的
企業財團之間存在怎樣的競合關係，我們卻始終無法一覽全貌。近年來社會網絡分析 (Social Network Analysis）相當盛行，藉著觀察法人投資關係我們
可以更清楚政府、財團甚至黨營事業組成一個大群體。這群體的成員組成有誰？他們的規模究竟有多大？該如何界定他們的影響力？這些都將在下文逐一分析討論。


本研究資料來源為 <a href="http://gcis.nat.g0v.tw/">台灣公司關係圖 http://gcis.nat.g0v.tw/</a> 7 月份資料，整體樣本數為 1,447,188 家公司。由於資料來源並不含時間序列的變數，無法觀察不同時點的公司存活家數變化，故僅考慮營運中的企業。台灣整體營運中的企業數 (不含分公司) 約 619,154 家。其中有董監事名單或被列入董監事名單的公司約有 42,043 家，這些約佔整體營運中的企業 6.79% 左右。我們想了解的，就是這些公司為台灣形塑出來的企業生態圈概貌。


本報告將依以下順序進行探討：

* 樣本組成概貌
* 台灣整體企業網絡成份
* 誰是老大？誰是幕後藏鏡人？
* 企業影響力排名


## 台灣企業網絡生態圈


![png]({filename}/images/TWcompany_files/TWcompany_11_0.png)


根據不同企業間的法人投資關係，可將企業們分成大小不同的群體，進而繪出如上圖的台灣企業投資網路分佈（圓點大小代表企業數量多寡）。為簡化圖形複雜度，在此僅列出三家以
上公司形成的群體。圖中多數群體的規模（此處群體規模為群體內的企業家數）相近，但有一個群體規模明顯大於其他群體。這群體究竟有多大？他的群體規模是第二名的三百倍以上
。

這規模最大的群體，其交叉投資關係可繪成以下社會網路圖：


![png]({filename}/images/TWcompany_files/TWcompany_13_0.png)


上圖中紅點部份為該群體中直接投資公司數量前 25 名的公司。這些公司成員有官股行庫、財團與黨營事業。這些公司正位於群體的核心附近，透過子公司繼續投資其他公司形成
間接投資。其他也有財團間透過策略聯盟交叉投資，或是共同投資新事業結合成利益共同體。種種複雜的投資關係下建構出了一個超巨大關係企業集團。對於台灣大型企業集團的結構
與形成過程，可參考中研院李宗榮老師發表的研究文章
[1](http://newsletter.sinica.edu.tw/file/file/36/3602.pdf),
[2](http://sociology.ntu.edu.tw/ntusocial/journal/ts-13/1-4all.pdf)。

對於群體規模與相同規模的群體個數之間的關係，我們可繪成散佈圖如下：


![png]({filename}/images/TWcompany_files/TWcompany_16_0.png)


由圖可觀察到一些現象：

* 絕大多數公司僅存在少數法人投資關係。
* 規模越大的群體，其個數與群體規模成指數遞減的關係。
* 規模最大的群體有一萬個以上成員。

這些由法人投資而形成的群體可視為具有廣義上的集團關係。集團所帶來的好處，不僅是投資方提供資金，取得被投資方的經營利潤而已。這當中還帶來了更多的資訊、人脈等無形優
勢，幫助集團成員攫取更多利益。而集團的存在對經濟發展亦有指標性的影響，因為集團本身的規模優勢與市場地位而築成強勢的議價力量，會成為其他企業營運上不可忽視的因素之
一。


## 誰是老大哥？誰是藏鏡人？

在觀察到台灣存在這麼一個超大關係企業集團後，令人忍不住想了解其中的組成成份。

在此我們試從兩個面向探討：直接投資家數、直接投資加上間接投資家數，來觀察誰是當中的老大哥。

### 直接投資家數排名

整體而言，最多直接投資的公司有誰呢？
根據全體法人投資關係，列出前 25 大公司如下：


<table><tr><td>排名</td><td>單位名稱</td><td>祖先數</td><td>子孫數</td><td>直接被投資</td><td>直接投資</td><td>是否身處最大集團</td></tr><tr><td>1</td><td>兆豐國際商業銀行股份有限公司</td><td>8</td><td>291</td><td>1</td><td>96</td><td>O</td></tr><tr><td>2</td><td>中華開發工業銀行股份有限公司</td><td>20</td><td>304</td><td>1</td><td>79</td><td>O</td></tr><tr><td>3</td><td>南聯國際貿易股份有限公司</td><td>5</td><td>112</td><td>1</td><td>55</td><td>O</td></tr><tr><td>4</td><td>裕隆汽車製造股份有限公司</td><td>18</td><td>195</td><td>4</td><td>47</td><td>O</td></tr><tr><td>5</td><td>南和興產股份有限公司</td><td>13</td><td>53</td><td>10</td><td>45</td><td>O</td></tr><tr><td>6</td><td>統一企業股份有限公司</td><td>4</td><td>221</td><td>4</td><td>43</td><td>O</td></tr><tr><td>7</td><td>統一超商股份有限公司</td><td>5</td><td>77</td><td>2</td><td>39</td><td>O</td></tr><tr><td>8</td><td>寶島投資開發股份有限公司</td><td>0</td><td>36</td><td>0</td><td>36</td><td>X</td></tr><tr><td>9</td><td>東元電機股份有限公司</td><td>18</td><td>81</td><td>6</td><td>35</td><td>O</td></tr><tr><td>10</td><td>創新工業技術移轉股份有限公司</td><td>1</td><td>47</td><td>1</td><td>34</td><td>O</td></tr><tr><td>11</td><td>中國鋼鐵股份有限公司</td><td>120</td><td>155</td><td>7</td><td>33</td><td>O</td></tr><tr><td>12</td><td>行政院國家發展基金管理會</td><td>0</td><td>635</td><td>0</td><td>32</td><td>O</td></tr><tr><td>13</td><td>光陽工業股份有限公司</td><td>9</td><td>52</td><td>9</td><td>31</td><td>O</td></tr><tr><td>14</td><td>臺灣水泥股份有限公司</td><td>71</td><td>246</td><td>12</td><td>31</td><td>O</td></tr><tr><td>15</td><td>永豐餘投資控股股份有限公司</td><td>10</td><td>195</td><td>5</td><td>29</td><td>O</td></tr><tr><td>16</td><td>仁寶電腦工業股份有限公司</td><td>2</td><td>102</td><td>1</td><td>29</td><td>O</td></tr><tr><td>17</td><td>南亞塑膠工業股份有限公司</td><td>7</td><td>109</td><td>4</td><td>28</td><td>O</td></tr><tr><td>18</td><td>臺灣化學纖維股份有限公司</td><td>7</td><td>109</td><td>4</td><td>27</td><td>O</td></tr><tr><td>19</td><td>行政院國軍退除役官兵輔導委員會</td><td>0</td><td>53</td><td>0</td><td>27</td><td>O</td></tr><tr><td>20</td><td>中盈投資開發股份有限公司</td><td>120</td><td>155</td><td>1</td><td>26</td><td>O</td></tr><tr><td>21</td><td>太陽光電能源科技股份有限公司</td><td>3</td><td>29</td><td>2</td><td>25</td><td>X</td></tr><tr><td>22</td><td>中央投資股份有限公司</td><td>0</td><td>118</td><td>0</td><td>25</td><td>O</td></tr><tr><td>23</td><td>大同股份有限公司</td><td>1</td><td>65</td><td>1</td><td>25</td><td>O</td></tr><tr><td>24</td><td>中華電信股份有限公司</td><td>1</td><td>71</td><td>1</td><td>24</td><td>O</td></tr><tr><td>25</td><td>新光合成纖維股份有限公司</td><td>51</td><td>313</td><td>7</td><td>24</td><td>O</td></tr></table>


前五百大詳細內容見此：<a href="http://weichengliou.github.io/blog/downloads/data/html/outdeg_rank.html">HTML</a>, <a href="http://weichengliou.github.io/blog/downloads/data/csv/outdeg_rank.csv">CSV</a>


以上可觀察到前 25 名企業中，僅有兩間公司不屬於最大集團的一份子。事實上即使前 100 名中也僅有五間公司不屬於最大集團的一份子。（見下表）


<table><tr><td>名次</td><td>名稱</td><td>直接投資</td></tr><tr><td>7</td><td>寶島投資開發股份有限公司</td><td>36</td></tr><tr><td>20</td><td>太陽光電能源科技股份有限公司</td><td>25</td></tr><tr><td>33</td><td>鬥牛士股份有限公司</td><td>21</td></tr><tr><td>50</td><td>旭晟投資有限公司</td><td>17</td></tr><tr><td>51</td><td>皇科投資有限公司</td><td>17</td></tr><tr><td>56</td><td>中嘉網路股份有限公司</td><td>17</td></tr></table>


觀察前 25 名可以看到組成份子可略分三大類：財團、官股、黨營事業。前兩名的兆豐國際商業銀行與中華開發工業銀行，因過去的工業銀行背景，故至今仍佔有不少公司的董監
事席次。中華開發昔日具備官股與黨營事業背景，但時至今日已無黨營事業席次，而官股亦已僅剩一席。

國民黨麾下的中央投資，與大同公司、太陽光電能源科技公司同時列名第 21 名。自過去一黨專政時代開始，國民黨即擁有不少資產。雖然社會自過去一直不斷有要求國民黨歸還
黨產的聲音出現，但至今仍有堪與其他財團相比擬的轉投資公司家數。像國民黨這樣具有財團實力的政黨在世界各國當中已是少數，其身處台灣最大關係企業集團中的一員，更顯示了
其與財團之間利害關係密切。

對於直接投資前 50 名的公司，可繪出一階社會網路圖如下：


<a href="http://weichengliou.github.io/blog/downloads/data/html/outdeg_network.lv1.html">另開新頁</a>


![png]({filename}/images/TWcompany_files/TWcompany_25_1.png)


僅從一階社會網路圖來看，這些原本即身處最大關係企業集團之內的企業已形成一個群體，表示這些企業間的距離在兩度 (degree <= 2)
之內，足證這些企業間的關係密切。

### 直接投資＋間接投資排名

接下來試圖從直接投資＋間接投資（簡稱為子孫數）排名觀察。母公司投資子公司，子公司又投資孫公司，如此層層相連形成一廣大關係企業結構。雖說最上層公司未必能影響最下層
公司，但仍可視為有間接影響力。根據全體法人投資關係，列出子孫數前 25 大公司如下：


<table><tr><td>排名</td><td>單位名稱</td><td>祖先數</td><td>子孫數</td><td>直接被投資</td><td>直接投資</td><td>是否身處最大集團</td></tr><tr><td>0</td><td>財政部</td><td>0</td><td>719</td><td>0</td><td>11</td><td>O</td></tr><tr><td>1</td><td>臺灣金融控股股份有限公司</td><td>1</td><td>668</td><td>1</td><td>3</td><td>O</td></tr><tr><td>2</td><td>臺灣銀行股份有限公司</td><td>2</td><td>665</td><td>1</td><td>17</td><td>O</td></tr><tr><td>3</td><td>行政院國家發展基金管理會</td><td>0</td><td>635</td><td>0</td><td>32</td><td>O</td></tr><tr><td>4</td><td>東賢投資有限公司</td><td>0</td><td>495</td><td>0</td><td>13</td><td>O</td></tr><tr><td>5</td><td>財團法人新光吳火獅文教基金會</td><td>0</td><td>492</td><td>0</td><td>8</td><td>O</td></tr><tr><td>6</td><td>成安有限公司</td><td>0</td><td>480</td><td>0</td><td>4</td><td>O</td></tr><tr><td>7</td><td>雲山有限公司</td><td>0</td><td>479</td><td>0</td><td>3</td><td>O</td></tr><tr><td>8</td><td>傑成有限公司</td><td>0</td><td>477</td><td>0</td><td>2</td><td>O</td></tr><tr><td>9</td><td>逢星投資股份有限公司</td><td>3</td><td>475</td><td>3</td><td>3</td><td>O</td></tr><tr><td>10</td><td>新台建設股份有限公司</td><td>2</td><td>475</td><td>2</td><td>3</td><td>O</td></tr><tr><td>11</td><td>傑昌投資股份有限公司</td><td>3</td><td>474</td><td>3</td><td>2</td><td>O</td></tr><tr><td>12</td><td>兆邦投資股份有限公司</td><td>3</td><td>472</td><td>1</td><td>3</td><td>O</td></tr><tr><td>13</td><td>成玲投資股份有限公司</td><td>6</td><td>472</td><td>3</td><td>3</td><td>O</td></tr><tr><td>14</td><td>葛昌投資股份有限公司</td><td>6</td><td>472</td><td>3</td><td>3</td><td>O</td></tr><tr><td>15</td><td>新光國際投資股份有限公司</td><td>0</td><td>471</td><td>0</td><td>6</td><td>O</td></tr><tr><td>16</td><td>家邦投資股份有限公司</td><td>9</td><td>471</td><td>3</td><td>15</td><td>O</td></tr><tr><td>17</td><td>進賢投資股份有限公司</td><td>0</td><td>460</td><td>0</td><td>3</td><td>O</td></tr><tr><td>18</td><td>昕達投資股份有限公司</td><td>0</td><td>460</td><td>0</td><td>3</td><td>O</td></tr><tr><td>19</td><td>昕昌投資股份有限公司</td><td>0</td><td>460</td><td>0</td><td>1</td><td>O</td></tr><tr><td>20</td><td>昕陽投資股份有限公司</td><td>0</td><td>460</td><td>0</td><td>2</td><td>O</td></tr><tr><td>21</td><td>東興投資股份有限公司</td><td>3</td><td>459</td><td>3</td><td>7</td><td>O</td></tr><tr><td>22</td><td>瑞新興業股份有限公司</td><td>1</td><td>459</td><td>1</td><td>11</td><td>O</td></tr><tr><td>23</td><td>漢霖建設股份有限公司</td><td>0</td><td>458</td><td>0</td><td>3</td><td>O</td></tr><tr><td>24</td><td>恆昇國際企業有限公司</td><td>0</td><td>458</td><td>0</td><td>1</td><td>O</td></tr></table>


前五百大詳細內容見此：<a href="http://weichengliou.github.io/blog/downloads/data/html/des_rank.html">HTML</a>, <a href="http://weichengliou.github.io/blog/downloads/data/csv/des_rank.csv">CSV</a>


從子孫數排名有幾項觀察：

以財政部為首，影響最多公司（台灣金控與台灣銀行為官股行庫成員，由財政部直接投資），其亦身處最大集團之內。雖說此亦有公私利益混雜的疑慮，但與黨營事業的差別在於：政
府由全體人民投票決定，有可能政黨輪替，但是政黨則否。

而國發基金的成立宗旨在於改善產業結構、投資協助產業創新，其影響力排名第二。惟其評估標的方式與是否有受到有效監管則不在本文討論範圍之內。

除官股行庫與國發基金以外，其餘公司多以投資公司為主。此因現今經營控制財團企業的家族們，多以投資公司的形式控制企業。其直接投資家數多在十家以下，堪稱為財團幕後的藏
鏡人。值得注意的是，榜上排名前 25
名的公司中，有大半屬於泛新光集團（新光＋台新）的一份子，新光集團旗下成員眾多，大股東透過多家投資公司交叉持有旗下企業，故這些公司的子孫數中有大量重複對象。

關於這些企業間的關係，可以根據前 50 名企業繪製一階企業社會網路圖如下：


<a href="http://weichengliou.github.io/blog/downloads/data/html/des_network.html">另開新頁</a>


![png]({filename}/images/TWcompany_files/TWcompany_31_1.png)


從上圖可以看到，前 25 名的企業大致可分為兩大群體：官股與泛新光集團。一階的企業網絡圖共有 162 個點，佔不到該最大群體的 10％。若是延伸至三階共有 1986 個點，共佔該最大群體 14.87 %。


但是這種觀察方式僅能觀察得到官股與新光集團影響力龐大的結論，那麼其他家族與企業集團又如何呢？接下來將試圖應用社會網路分析的部份概念，來協助找出居於群體核心位置的
企業。

### 中間度排名

這部份應用近距中間度指標 (closeness centrality) 試圖找出居於核心位置的企業。先暫列排名前 25 名企業如下：


<table><tr><td>排名</td><td>單位名稱</td><td>祖先數</td><td>子孫數</td><td>直接被投資</td><td>直接投資</td><td>是否身處最大集團</td></tr><tr><td>1</td><td>臺灣銀行股份有限公司</td><td>2</td><td>665</td><td>1</td><td>17</td><td>O</td></tr><tr><td>2</td><td>財政部</td><td>0</td><td>719</td><td>0</td><td>11</td><td>O</td></tr><tr><td>3</td><td>兆豐國際商業銀行股份有限公司</td><td>8</td><td>291</td><td>1</td><td>96</td><td>O</td></tr><tr><td>4</td><td>臺灣金融控股股份有限公司</td><td>1</td><td>668</td><td>1</td><td>3</td><td>O</td></tr><tr><td>5</td><td>中華開發工業銀行股份有限公司</td><td>20</td><td>304</td><td>1</td><td>79</td><td>O</td></tr><tr><td>6</td><td>行政院國家發展基金管理會</td><td>0</td><td>635</td><td>0</td><td>32</td><td>O</td></tr><tr><td>7</td><td>兆豐金融控股股份有限公司</td><td>7</td><td>348</td><td>5</td><td>8</td><td>O</td></tr><tr><td>8</td><td>財團法人新光吳火獅文教基金會</td><td>0</td><td>492</td><td>0</td><td>8</td><td>O</td></tr><tr><td>9</td><td>統一企業股份有限公司</td><td>4</td><td>221</td><td>4</td><td>43</td><td>O</td></tr><tr><td>10</td><td>交通部</td><td>0</td><td>432</td><td>0</td><td>8</td><td>O</td></tr><tr><td>11</td><td>中華開發金融控股股份有限公司</td><td>19</td><td>316</td><td>5</td><td>2</td><td>O</td></tr><tr><td>12</td><td>中華郵政股份有限公司</td><td>1</td><td>362</td><td>1</td><td>3</td><td>O</td></tr><tr><td>13</td><td>家邦投資股份有限公司</td><td>9</td><td>471</td><td>3</td><td>15</td><td>O</td></tr><tr><td>14</td><td>兆豐國際商業銀行股份有限公司工會</td><td>0</td><td>350</td><td>0</td><td>2</td><td>O</td></tr><tr><td>15</td><td>進賢投資股份有限公司</td><td>0</td><td>460</td><td>0</td><td>3</td><td>O</td></tr><tr><td>16</td><td>東賢投資有限公司</td><td>0</td><td>495</td><td>0</td><td>13</td><td>O</td></tr><tr><td>17</td><td>裕隆汽車製造股份有限公司</td><td>18</td><td>195</td><td>4</td><td>47</td><td>O</td></tr><tr><td>18</td><td>綿豪實業股份有限公司</td><td>2</td><td>436</td><td>1</td><td>5</td><td>O</td></tr><tr><td>19</td><td>高權投資股份有限公司</td><td>0</td><td>222</td><td>0</td><td>7</td><td>O</td></tr><tr><td>20</td><td>德岳實業股份有限公司</td><td>1</td><td>450</td><td>1</td><td>3</td><td>O</td></tr><tr><td>21</td><td>興文投資股份有限公司</td><td>2</td><td>326</td><td>1</td><td>3</td><td>O</td></tr><tr><td>22</td><td>永原投資股份有限公司</td><td>0</td><td>231</td><td>0</td><td>7</td><td>O</td></tr><tr><td>23</td><td>東興投資股份有限公司</td><td>3</td><td>459</td><td>3</td><td>7</td><td>O</td></tr><tr><td>24</td><td>新光育樂股份有限公司</td><td>39</td><td>444</td><td>6</td><td>2</td><td>O</td></tr><tr><td>25</td><td>泰伯投資股份有限公司</td><td>0</td><td>229</td><td>0</td><td>5</td><td>O</td></tr></table>


前五百大詳細內容見此：<a href="http://weichengliou.github.io/blog/downloads/data/html/betw_rank.html">HTML</a>, <a href="http://weichengliou.github.io/blog/downloads/data/csv/betw_rank.csv">CSV</a>


排名前 25 名的企業，多半以官股行庫、國發基金與國營事業居多。其次為泛新光集團、統一集團與裕隆集團。

若是觀察前一百名企業的一階企業網路圖（見下圖），可看到多數企業集合成一個群體，表示這些企業間的距離大多在兩度以內，再次印證了這些企業間關係密切程度。其中新光集團
旗下企業佔了不少，可見其企業經營網絡之廣闊。


<a href="http://weichengliou.github.io/blog/downloads/data/html/clos_network.lv1.html">另開新頁</a>


![png]({filename}/images/TWcompany_files/TWcompany_39_1.png)


## 結語

本文試從社會網路分析角度揭示台灣經濟發展現況。從整體觀之，台灣存在一個由政府、財團與黨營事業組成之超巨大關係企業集團。關於其形成方式自有其歷史背景，並非本文探討
重點。然吾人必須了解，僅僅從法人投資而言，財團間的利益關係遠比我們想像的還要密切。更遑論因血親、姻親而組成的親族關係，將使這集團規模進一步擴大。

另外我們也發現黨營事業亦身處這個巨大利益共同體裡面，這點在政黨決策方向的制定與執行上，將不可避免地造成巨大影響。如何有效監督與減少政黨與財團間的裙帶關係影響，仍
有待全民共同努力。

本文研究僅為一個起點，後續將有更多的深入研究，協助我們更了解台灣的企業生態環境。

## 參考文獻

1. [李宗榮，〈台灣企業間的親屬網絡〉，《中央研究院週報》 No.
1216](http://newsletter.sinica.edu.tw/file/file/36/3602.pdf)
2. [李宗榮，2007，〈在國家與家族之間：企業控制與臺灣大型企業間網絡再探〉，《台灣社會學》，第13卷，頁173-242。(TSSCI)](http://s
ociology.ntu.edu.tw/ntusocial/journal/ts-13/1-4all.pdf)




<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/"
property="dct:title">Gilbert's Data Lab</span> by <a
xmlns:cc="http://creativecommons.org/ns#" href="http://WeiChengLiou.github.io/"
property="cc:attributionName" rel="cc:attributionURL">WeiCheng Liou</a> is
licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons
Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a
xmlns:dct="http://purl.org/dc/terms/" href="http://WeiChengLiou.github.io/"
rel="dct:source">http://WeiChengLiou.github.io/</a>.
