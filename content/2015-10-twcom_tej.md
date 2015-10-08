title: 台灣上市櫃公司網絡變化史
date: 2015-10-08 12:00
comments: true
slug: twcom_tej
tags: 台灣公司關係圖
category: 台灣公司關係圖


本文旨在應用臺灣上市櫃公司歷史公開資訊，
探討 1998-2014 年間上市櫃公司的企業投資網路。
資料來源以臺灣經濟新報 (TEJ) 資料庫為主，
但 <a href="http://www.mops.com.tw">公開資訊觀測站</a> 亦可找到相關資訊。
感謝中央研究院資訊所何建民老師與台灣大學會計系王泰昌教授協助指導研究。

從經濟部的營利事業登記資料可以得知，
眼下各大財團、國營企業、金融機構與黨營事業彼此交叉投資形成一個主要群體，
某種程度上可視為黨國資本主義時代下遺留的產物。
那麼這種企業間的投資網路，在過去具有什麼特徵？這些年來又產生那些變化？
乃至於我最想問的一個問題是：這種企業間的投資網絡對我們具有何種意義？

要想回答這些問題，需仰賴臺灣上市櫃公司與公開發行公司的公開資訊。
為了因應證交所的資訊要求，這些公司需定期揭露轉投資公司、對中國投資、董監事與大股東持股資訊，
而這些資訊成了我們建構不同時期企業投資網絡的最大資料來源。


在分析前先講結論：

1. 每年上市櫃公司家數逐年遞增。
2. 整體產業分佈以電子業為主。
3. 主要集團間共同或交叉投資，形成大群體現象一直存在。
4. 主要群體的公司數佔整體比重逐年上升，但密度逐年下降。 


## 基本分析

上市櫃公司家數與產業分佈可以下圖表示：

![png]({filename}/images/twcom_tej_files/indNewList.png)


那麼就投資關係而言，這些年究竟出現多少公司？


![png]({filename}/images/twcom_tej_files/yrNode.png)


主要資料來源大多來自於公司財報裡的長期投資項目。

長期投資項目並不僅止於國內，也包含國外的股權投資或百分百持股子公司。
2011 年以後，因為證交所要求於合併財報中揭露集團轉投資之故，
故一般投資人更有機會了解各集團整體轉投資概況。

董監事法人代表資訊乃指各上市櫃公司董監事名單中的法人代表資訊，
這部份資訊較長期投資資訊少。

最後是轉投資中國的資訊，
這部份資料自 1999 年開始陸續公佈越來越多資訊，
主要為各上市櫃公司在中國轉投資設立的工廠或子公司資訊。


若是將各公司間投資關係合併起來看，
依不同資料來源可以看到這些連結的數量變化。

![png]({filename}/images/twcom_tej_files/yrEdge.png)


由於對中國投資的部份，多半以在當地設廠或設立子公司為主，交叉投資的部份較少。
為了簡化分析，後續分析將以長期投資與董監事法人代表資訊為主。

從主要群體與整體的比較來看，
主要群體的成員 (node) 比重逐年上升，表示有越來越多公司經由投資或被投資的關係成為主要群體的一部分。
但主要群體的連結數 (edge) 比重雖略有下降，但整體約略維持在九成以上水準。表示九成以上的投資關係發生在主要群體之內，比較如下圖：

![png]({filename}/images/twcom_tej_files/yrRatio1.png)


根據不同來源資料，我們可以作各企業的平均連結數比較。
如下圖可見，整體而言平均連結數約在 2.4 ~ 2.6 之間，
與長期投資比較有關。

![png]({filename}/images/twcom_tej_files/avgdeg.source.png)


隨著資本市場逐年發展，
在上市櫃公司與集團投資公司數逐年增加的情況下，
只要各企業的平均連結數沒太大變化，
可了解整體與主要群體的網絡密度將逐年下降。


## 投資公司排名

本節將分別從董監事法人代表資訊與長期投資來看每年前十名的公司變化。
首先從董監事法人代表資訊來看投資公司排名，
該排名可以了解哪些公司擔任最多上市櫃公司的董監事：

![png]({filename}/images/twcom_tej_files/yr.out_deg1.Board.png)


每年前十名的公司不盡相同，
但除了開發工銀、中央投資、光華投資、交通銀行、兆豐商銀之外，
其餘公司投資數約略在 20 間公司之內。
有趣的是黨營事業群在上市櫃公司擔任董監事的家數，在 2000 年以後逐漸減少，
乃至於 2006 年以後僅擔任一間上市櫃公司董監事。
由此也可以見到政黨輪替的必要性。

為了更清楚每年度投資前十名公司的變化，
我們試著以 Heat Map 方式來觀察：

![png]({filename}/images/twcom_tej_files/out_deg1.mat.Board.png)


能在這 18 年中持續居於前十名的公司，主要都是政府、國營事業與大型財團。
在該圖中可看到隨著時代逐漸降低影響力的企業集團，如：和通創投、黨營事業、東森集團等。
另一方面亦可看到逐漸增加影響力的企業集團，即同屬旺中集團旗下的新紀元投資與中嘉網路。


若改從長期投資的資訊切入，觀察每年前十名的變化，我們又能獲得什麼資訊？

![png]({filename}/images/twcom_tej_files/yr.out_deg1.Ivst.png)

![png]({filename}/images/twcom_tej_files/out_deg1.mat.Ivst.png)


長期而言大部分公司投資數在一百家公司以內，
但開發工銀的投資數多數時候均傲視群雄，
一度更曾達到四百間公司以上，但往後投資數卻逐年減少。

另一個有趣的地方是，除了開發金之外，
投資數超過 150 的多半為金融業，
這點與金融業的自身的行業特性有關。

2011 年以後多出不少間財團轉投資成立的創業投資公司。
此乃託因於 2011 年開始，合併財報揭露集團轉投資資訊，
故我們方可見到這些創投公司的轉投資情形。


## 結論

目前我們已約略了解：
上市櫃公司間的企業投資網絡，
長期而言存在一主要群體，
且該群體結構長期而言相對穩定。

而黨營事業過去在該網絡中佔有相對重要的位置，
但 2000 年後影響力逐漸下降。

但該結構對整體環境影響為何？這可能並不能單從這些資訊即可回答。
但我們或許可以問的是：若我是有意在臺灣上市櫃的新創事業老闆或股東，
這樣的網絡結構是否對我有影響？
這問題將在下篇文章進一步探討。



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
