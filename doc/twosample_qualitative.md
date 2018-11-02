# 質的データ ２組の評価

## 対応有り

- 名義尺度：マクニマーの検定
- 順位尺度：符号付き順位和検定 (Wilcoxon Signed-ranks test)


## 対応無し

- 名義尺度：カイ2乗検定 

または，コクラン・ルールを満たさない場合：フィッシャーの直接法 （注） 

- 順位尺度：マン・ホイトニーの検定


（注） 最近は，パソコンで計算できるからどんなときもフィッシャーの直接法を用いるべきという意見もある．しかし，このパッケージではpythonでのオーバーフローの問題を回避できないので，コクラン・ルールを満たすかどうかの判定を行う．  

## サンプル

- 名義尺度

paired test (McNemar test):   
```python sample_two_sample_test_of_nominal_scale.py 1```

unpaired test + big data (chi-square test):  
```python sample_two_sample_test_of_nominal_scale.py 2```

unpaired test + small data (Fisher's exact test):  
```python sample_two_sample_test_of_nominal_scale.py 3```

- 順位尺度

paired sample, signed test + small data:  
```python sample_two_sample_test_of_ordinal_scale.py 1```

paired sample, signed test + big data:  
```python sample_two_sample_test_of_ordinal_scale.py 2```

paired sample, signed rank sum test:    
```python sample_two_sample_test_of_ordinal_scale.py 3```

unpaired sample, mann-whitney test:  
```python sample_two_sample_test_of_ordinal_scale.py 4```

## how to report results

### nominal

- McNemar Test

```
A McNemar Test was performed to examine the relation between <ex. approval of product A> and <ex. a lecture from a company>.
The relation between these variables was significant, X^2(<dof ex. 1>) = <ex. 14.14>, p<.01. <ex. People before taking a lecture from a company> were less likely to <ex. show an approval of productA> than were <ex. people after taking a lecture from a company>.
```

- Chi-square Test

```
A chi-square test of independence was performed to examine the relation between <ex. religion> and <ex. college interest>. 
The relation between these variables was significant, X^2(<dof ex. 1>) = <ex. 14.14>, p<.01. <ex. Catholic teens> were less likely to <ex. show an interest in attending college> than were <ex. Protestant teens>.
```

- Fisher's Exact Test 

```
ex. 
Fisher's Exact Test indicated that primary outcome results indicated a non-significant reduction in the acquisition of plasma cell endometritis in the antibiotic group with a prevalence of 28% (9/32), compared to 50% (14/28) in the placebo group (p=0.11). 
reference: http://www.pmean.com/08/ReportingFishersExact.html

```

### ordinal

- Mann Whitney U test

```
補足
To study the differences in <dependent variable> between <level1 of the independent variable> and <level2 of the independent variable>, we used the Mann-Whitney U test to analyse <dependent variable>. We ran the Mann-Whitney U test using <type of independent variable> as the grouping variable and <dependent variable> as the dependent variable.
```

```
A Mann-Whitney test indicated that the <fill dependent variable> was greater for <fill level1 of the independent variable> (Mdn = <fill median1>) than for <fill level2 of the independent variable> (Mdn = <fill median2>), U=<fill U>, p=<fill p>.   
```

- Sign test

```
A sign test indicated that <fill time2 of independent variable; ex. post-test ranks> (Mdn = <fill median1>) was statistically significantly higher than <fill time1 of independent variable; ex. pre-test ranks> (Mdn = <fill median2>); Z=<fill Z>, p= <fill p>.
```

- Wilcoxon Signed-ranks test

```
A Wilcoxon Signed-Ranks Test indicated that <fill time2 of independent variable; ex. post-test ranks> (Mdn = <fill median1>) was statistically significantly higher than <fill time1 of independent variable; ex. pre-test ranks> (Mdn = <fill median2>); Z=<fill Z>, p= <fill p>. 

# if the reason you used a Wilcoxon Signed-Ranks Test is because your data is very skewed or non-normal, just report it the same way but replace "ranks" with "scores".
```
