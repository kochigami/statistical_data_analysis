# 2標本検定

## 同じ被験者に体験前後でアンケート (対応有り)

- Yes/ No 形式 (名義尺度)：マクネマーの検定
- グレード形式 (順位尺度)：ウィルコクソンの符号付き順位検定


## 同じ被験者のふれ合いについて、計量尺度に基づくデータ取得 (対応有り)

- ロボット1, ロボット2とのふれ合い時間の比較 (計量尺度)：対応のあるt検定


## 条件1、条件2ごとにアンケート (対応無し)

- Yes/ No 形式 (名義尺度)：カイ2乗検定  
コクラン・ルールを満たさない場合：フィッシャーの正確検定  
最近は、パソコンで計算できるからどんなときもフィッシャーの正確検定を用いるべきという意見もある。しかし、このパッケージではpythonでのオーバーフローの問題を回避できないので、コクラン・ルールを満たすかどうかの判定を行う。 

- グレード形式 (順位尺度)：ウィルコクソンの2標本検定/ ウィルコクソンの順位和検定/ マン・ホイットニィのU検定


## 条件1、条件2ごとに、計量尺度に基づくデータ取得 (対応無し)

- 条件ごとのふれ合い時間の比較 (計量尺度)：対応のないt検定

## サンプル

- 対応のある順位尺度検定
```python sample_u_test.py 1```
![](sample_fig/sample8.png)

- 対応のあるt検定

```python sample_t_test.py 3```
![](sample_fig/sample3.png)

- カイ二乗検定
```python sample_chi_squared_test.py```
![](sample_fig/sample10.png)

- 対応のないU検定
```python sample_u_test.py 2```
![](sample_fig/sample9.png)

- 対応のないt検定
```python sample_t_test.py 1```
![](sample_fig/sample1.png)

```python sample_t_test.py 2```
![](sample_fig/sample2.png)


# 多標本検定

## 分散分析

### 一元配置
### 二元配置

## サンプル

- one-way factrial ANOVA (一元配置要因分散分析、被験者間計画)
```python sample_t_test.py between```
![](sample_fig/sample4.png)
![](sample_fig/sample5.png)

- one-way repeated measures ANOVA (一元配置反復測定分散分析、被験者内計画)
```python sample_t_test.py within```
![](sample_fig/sample6.png)
![](sample_fig/sample7.png)



