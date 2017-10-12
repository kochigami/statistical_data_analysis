# T検定

## サンプル
```cd src/sample_t_test.py```

## 前提
- 各条件の平均値の差を比較する
- 前提：各組のサンプル数は同じ

## 1. 対応のあるt検定

- 条件A, Bの比較をする時に、各々の条件を同じ人が試している時に用いる
- sample:
```python sample_t_test.py 3```
![](sample_fig/sample3.png)

```python sample_t_test.py 4```
![](sample_fig/sample4.png)

## 2. 対応のないt検定

- 条件A, Bの比較をする時に、各々の条件を別の人が試している時に用いる
- sample:
```python sample_t_test.py 1```
![](sample_fig/sample1.png)

```python sample_t_test.py 2```
![](sample_fig/sample2.png)

# 分散分析

## 前提

- 被験者間計画での実装（今後改良）

## 1. 一元配置

- 分析対象の要因が1つで、その1つが3つ以上の水準に分かれている時に用いる


## 2. 二元配置

- 分析対象の要因が2つで、その2つを組み合わせて分析を行う時に用いる