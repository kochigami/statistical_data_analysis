# 量的データ ２組の評価

## 対応有り

- 対応のあるt検定

## 対応無し

- 対応のない等分散のt検定（分散が等質な場合）

- Welchのt検定（分散が等質でない場合）


% t検定：2条件の平均値の差の検定


## サンプル

- 対応のあるt検定
```python sample_two_sample_test_of_interval_and_ratio_scale.py 1```
![](fig/sample_welch_test.png)

- 対応のないt検定
```python sample_two_sample_test_of_interval_and_ratio_scale.py 2```
![](fig/sample_unpaired_student_test.png)

```python sample_two_sample_test_of_interval_and_ratio_scale.py 3```
![](fig/sample_paired_student_test.png)

## How to report results

- A paired-samples t-test

```
A paired-samples t-test was conducted to compare <fill DV measure> in <fill IV level/ condition1> and <fill IV level / condition2> conditions.
There was a significant (not a significant) difference in the scores for <fill IV level1> (M=<fill average1> , SD=<fill SD1> ) and IV level2 (M=<fill average2> , SD=<fill SD2>) conditions; t(<fill df>)=<fill t value>, p=<fill p value>.
```

- an independent-samples t-test 

```
An independent-samples t-test was conducted to compare <fill DV measure> in <fill IV level/ condition1> and <fill IV level / condition2> conditions.
There was a significant (not a significant) difference in the scores for <fill IV level1> (M=<fill average1> , SD=<fill SD1> ) and IV level2 (M=<fill average2> , SD=<fill SD2>) conditions; t(<fill df>)=<fill t value>, p=<fill p value>.
```