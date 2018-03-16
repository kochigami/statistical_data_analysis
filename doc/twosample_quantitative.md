# 同じ被験者に体験前後でアンケート (対応有り)

- Yes/ No 形式 (名義尺度)：マクニマーの検定
- グレード形式 (順位尺度)：符号付き順位和検定

# 条件1、条件2ごとに異なる被験者に試してもらい，アンケート (対応無し)

- Yes/ No 形式 (名義尺度)：カイ2乗検定  
コクラン・ルールを満たさない場合：フィッシャーの直接法  
最近は，パソコンで計算できるからどんなときもフィッシャーの直接法を用いるべきという意見もある．しかし，このパッケージではpythonでのオーバーフローの問題を回避できないので，コクラン・ルールを満たすかどうかの判定を行う．

- グレード形式 (順位尺度)：マン・ホイトニーの検定

# サンプル

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
