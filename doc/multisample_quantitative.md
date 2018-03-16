# 条件1、条件2ごとにアンケート (対応無し)

- Yes/ No 形式 (名義尺度)：カイ二乗検定  
- グレード形式 (順位尺度)：クラスカル・ウォリスの検定    

# 同じ被験者に体験前後でアンケート (対応有り)

- Yes/ No 形式 (名義尺度)：コクランのQ検定  
- グレード形式 (順位尺度)：フリードマンの検定  

# サンプル

- 名義尺度

unpaired test (chi-square test):   
```python sample_two_sample_test_of_nominal_scale.py 1```

paired test (Cochran's Q test):  
```python sample_two_sample_test_of_nominal_scale.py 2```

- 順位尺度

unpaired test (Kruskal-Wallis test):  
```python sample_two_sample_test_of_ordinal_scale.py 1```

paired test (Friedman test):  
```python sample_two_sample_test_of_ordinal_scale.py 2```