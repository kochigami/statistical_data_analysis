# 対応有り

- 名義尺度：コクランのQ検定  
- 順位尺度：フリードマンの検定  


# 対応無し

- 名義尺度：カイ二乗検定  
- 順位尺度：クラスカル・ウォリスの検定    


[用語の説明]

対応有り：例えば，同じ被験者に体験前後でアンケート 

対応無し：例えば，条件1、条件2ごとに異なる被験者にアンケート

名義尺度：Yes/ No 形式

順位尺度：グレード形式

# サンプル

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

# how to report results

## nominal

- Chi-square Test

```
A chi-square test of independence was performed to examine the relation between <ex. religion> and <ex. college interest>. 
The relation between these variables was significant, X^2(<dof ex. 1>) = <ex. 14.14>, p<.01. <ex. Catholic teens> were less likely to <ex. show an interest in attending college> than were <ex. Protestant teens>.
```

- Cochran's Q Test

```
A Cochran's Q Test was performed to compare an approval rating between <ex. candidate1>, <ex. candidate2> and <ex. <ex. candidate3>.
It indicated that 
was conducted and rendered a X^2(<fill dof, ex. 2>) = <Q value> which was significant (p < .01).

```

## ordinal

- Kruskal Wallis Test

```
A Kruskal Wallis Test indicated that there was a statistically significant difference between <fill dependent variable> (H(<fill dof>) = <fill H>, p=<fill p>), with a mean rank of <fill mean rank1> for <independent value1>, <fill mean rank2> for <independent value2>, <fill mean rank3> for <independent value3>.
```

- Friedman Test

```
A non-parametric Friedman test of differences among repeated measures was conducted and rendered a Chi-square value of <fill chi-square value, in program, S value> which was significant (p < .01).
```