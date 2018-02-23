# 同じ被験者の条件ごとの計量尺度に基づくデータの比較 (例：ふれ合い時間）  

- 1. 対応のある2条件の平均値の差の検定  
- 例：同じ被験者で，ロボット1，ロボット2とのふれ合い時間を比較

# 異なる被験者の条件ごとの計量尺度に基づくデータの比較 (例：ふれ合い時間）  

- 1. 対応のない2条件の平均値の差の検定（分散が等質な場合）  
- 2. 対応のない2条件の平均値の差の検定（分散が等質でない場合）
- 例：異なる被験者で，ロボット1，ロボット2とのふれ合い時間のデータを集めて比較  

# サンプル

- 対応のあるt検定
```python sample_two_sample_test_of_interval_and_ratio_scale.py 1```
![](sample_fig/sample_welch_test.png)

- 対応のないt検定
```python sample_two_sample_test_of_interval_and_ratio_scale.py 2```
![](sample_fig/sample_unpaired_student_test.png)

```python sample_two_sample_test_of_interval_and_ratio_scale.py 3```
![](sample_fig/sample_paired_student_test.png)