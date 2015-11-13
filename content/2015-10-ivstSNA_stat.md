title: 投資公司投資成效檢定
date: 2015-10-21 14:00
comments: true
slug: ivstSNA_stat
tags: 台灣公司關係圖
category: 台灣公司關係圖


這篇文章是作為[前篇文章]({filename}2015-10-ivstSNA.md)的補充，提供統計檢定結果給有興趣深入了解的人。
主要藉著單一母體比例假設檢定，逐年檢定我們關心的項目是否明顯大於或小於 50%。
會採用逐年檢定的原因，
因為每年的資料並不完全獨立，
有些公司可能持有某公司好幾年後才撐到 IPO，
如此同組 投資-被投資 公司配對樣本就會連續出現好幾年，
所以這邊試著逐年檢定觀察，也可了解比例變化的趨勢。
圓圈為樣本平均，綠色棒為 99% 信賴區間，虛線為虛無假設的目標值。


## 新上市櫃公司中法人董監比例是否偏高？

![png]({filename}/images/ivstSNA_stat_files/ErrIvstRatio.New.png)

除了 2000 年以外，幾乎皆明顯高於五成。


## 興櫃公司中法人董監比例是否偏高？

![png]({filename}/images/ivstSNA_stat_files/ErrIvstRatio.Reg.png)

每年均明顯高於五成，且樣本平均高於新上市櫃公司的法人董監比例。


## 新上市櫃公司中主要群體比例是否偏高？

![png]({filename}/images/ivstSNA_stat_files/ErrMaxGrpRatio.New.png)

2002 年以前樣本平均大多高於五成，且 1998 年時明顯高於五成。
而 2003 年以後樣本平均逐年下降， 十二年的資料裡有六年明顯低於五成。
IPO 成功公司中的主要群體比例正逐年下降。


## 興櫃公司中主要群體比例是否偏高？

![png]({filename}/images/ivstSNA_stat_files/ErrMaxGrpRatio.Reg.png)

2008 年以前主要群體比例並不明顯低於五成，
但 2011 年以後明顯低於五成，
表示近年來主要群體在興櫃市場的投資意願不足。


## 有法人代表的新上市櫃公司中主要群體比例

![png]({filename}/images/ivstSNA_stat_files/ErrMaxGrp2Ivst.New.png)

2002 年以前主要群體比例明顯較高，
但 2003 年以後並無顯著差異。


## 有法人代表的興櫃公司中主要群體比例

![png]({filename}/images/ivstSNA_stat_files/ErrMaxGrp2Ivst.Reg.png)

2009 年以前八年的資料中，有五年明顯高於五成。
2010 年以後變得較不顯著，但 2014 年明顯低於五成。


