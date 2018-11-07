# 質的データ ３組以上の評価

## 対応有り

- 名義尺度：コクランのQ検定  
- 順位尺度：フリードマンの検定  


## 対応無し

- 名義尺度：カイ二乗検定  
- 順位尺度：クラスカル・ウォリスの検定    


## サンプル

- 名義尺度

unpaired test (chi-square test):   
```python sample_multiple_sample_test_of_nominal_scale.py 1```

paired test (Cochran's Q test):  
```python sample_multiple_sample_test_of_nominal_scale.py 2```

- 順位尺度

unpaired test (Kruskal-Wallis test):  
```python sample_multiple_sample_test_of_ordinal_scale.py 1```

paired test (Friedman test):  
```python sample_multiple_sample_test_of_ordinal_scale.py 2```

## 英語でのレポートの方法

### 名義尺度

- カイ二乗検定 (Chi-square Test)

```
A chi-square test of independence was performed to examine the relation between religion and college interest. The relation between these variables was significant, X^2(1) = 14.14, p<.01. Catholic teens were less likely to show an interest in attending college than were Protestant teens.
```

- コクランのQ検定 (Cochran's Q Test)

```
A Cochran's Q Test was performed to compare an approval rating between candidate1, candidate2 and candidate3.
The relation between these variables was significant, X^2(2) = <Q value>, p<.01. Candidate1 was more likely to be approved than other candidates. 
```

### 順位尺度

- クラスカル・ウォリスの検定 (Kruskal Wallis Test)

```
A Kruskal Wallis Test indicated that there was a statistically significant difference between <fill dependent variable> (H(<fill dof>) = <fill H>, p=<fill p>), with a mean rank of <fill mean rank1> for <independent value1>, <fill mean rank2> for <independent value2>, <fill mean rank3> for <independent value3>. <indenpendent value1> was more likely to be faster than others. 
```

- フリードマンの検定 (Friedman Test)

```
A Friedman test of differences among <indenpendent value1>, <indenpendent value2> and <indenpendent value3> was conducted and rendered a Chi-square value of <fill chi-square value (in this statistical_data_analysis program, it is given as S value)> which was significant (p < .01). <indenpendent value1> was more likely to be favored than others.
```