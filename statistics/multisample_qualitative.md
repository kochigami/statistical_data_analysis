# 一元配置: 要因は1つ

## 各処理水準に異なる被験者が無作為に割り当てられている（注）場合： 

- completely randomized design (CR デザイン)
- 注：1人の被験者は，1回の実験で1つの条件しか試さない  
- 例：ロボット1, ロボット2, ロボット3 それぞれのふれ合い時間を比較する    
- （１つしかない要因：ロボットの種類）  

## 同一の被験者 / 被験者グループ（注）が全ての処理水準に参加している場合： 

- randomized block design (RB デザイン)
- 例：ロボット1, ロボット2, ロボット3との被験者ごとのふれ合い時間の比較   
- (要因１：ロボットの種類，要因２：個人差)  
- 注１：特定の剰余変数によって被験者をブロック化し，各ブロック内の被験者を各処理水準に無作為に割り当てる場合も含む
- 注２：ブロック化は，被験者をグループ化して扱うこと（被験者を個人としては扱わない）  

# 二元配置: 要因は2つ

## 要因１，要因２が共に被験者間変数であり，
## それぞれの要因の各処理水準に異なる被験者が無作為に割り当てられている場合：

- completely randomized factorial design (CRFpq デザイン)
- 例：「あるロボット」（複数の種類があり、1つ選ぶ）と「あるふれ合い方」（複数のふれ合い方があり，1つ選ぶ）の条件で，ロボットと複数の人に**1回**ふれ合ってもらう．  

## 要因１の各処理水準には異なる被験者が無作為に割り当てられていて，
## 要因２には同一の被験者（注）がすべての処理水準に参加している場合： 

- split-plot design (SPFpq デザイン)
- 注：特定の剰余変数に基づいて被験者をブロック化し，そのブロック内の被験者を各処理水準に無作為に割り当てる場合も含む
- 例：「あるロボット」（複数の種類があり、1つ選ぶ）と「あるふれ合い方」（複数のふれ合い方があり，全て選ぶ）の条件で，ロボットと複数の人にふれ合ってもらう．  

## 同一の被験者が要因１，２の全ての処理水準に参加している（注）場合：

- randomized block factorial design (RBFpq デザイン)
- 例：「あるロボット」（複数の種類があり、全て選ぶ）と「あるふれ合い方」（複数のふれ合い方があり，全て選ぶ）の条件で，ロボットと複数の人にふれ合ってもらう．  
- 注１：特定の剰余変数によって被験者をブロック化し，各ブロック内の被験者を各処理水準に無作為に割り当てる場合も含む
- 注２：ブロック化は，被験者をグループ化して扱うこと（被験者を個人としては扱わない）  

## サンプル

CR デザイン（データ数異なる）  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 1```  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 3```  

CR デザイン（データ数同じ）  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 2```  

RB デザイン  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 4```  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 5```  

CRFpq デザイン（データ数同じ）  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 7```  

CRFpq デザイン（データ数異なる）  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 6```  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 8```  

SPFpq デザイン（データ数同じ）  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 9```  

SPFpq デザイン（データ数異なる）  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 10```  

RBFpq デザイン  
```python sample_multiple_sample_test_of_interval_and_ratio_scale.py 11```  