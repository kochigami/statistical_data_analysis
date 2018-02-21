# 同じ被験者に体験前後でアンケート (対応有り)

- Yes/ No 形式 (名義尺度)：マクニマーの検定
- グレード形式 (順位尺度)：符号付き順位和検定

# 条件1、条件2ごとにアンケート (対応無し)

- Yes/ No 形式 (名義尺度)：カイ2乗検定  
コクラン・ルールを満たさない場合：フィッシャーの直接法  
最近は，パソコンで計算できるからどんなときもフィッシャーの直接法を用いるべきという意見もある．しかし，このパッケージではpythonでのオーバーフローの問題を回避できないので，コクラン・ルールを満たすかどうかの判定を行う．

- グレード形式 (順位尺度)：マン・ホイトニーの検定

# サンプル

paired test + big data: 
```python sample_two_sample_test_of_nominal_scale.py 1```

paired test + small data:
```python sample_two_sample_test_of_nominal_scale.py 2```

unpaired test + big data:
```python sample_two_sample_test_of_nominal_scale.py 3```
![](sample_fig/sample_nominal_chi_squared.png)

unpaired test + small data:
```python sample_two_sample_test_of_nominal_scale.py 4```

paired-utest (sign test):
```python sample_two_sample_test_of_ordinal_scale.py 1```
![](sample_fig/sample_sign_test.png)

paired-utest (z test):
```python sample_two_sample_test_of_ordinal_scale.py 2```

unpaired-ttest (mann-whitney test):
```python sample_two_sample_test_of_ordinal_scale.py 3```
![](sample_fig/sample_mann_whitney.png)
