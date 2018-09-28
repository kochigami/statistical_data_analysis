# 調べたい要因は1つ：一元配置

## 1人の被験者は，1回の実験で1つの条件しか試さない場合

- completely randomized design (CR デザイン)

例

ロボット1, ロボット2, ロボット3 それぞれのふれ合い時間を比較する    

## 1人の被験者/ 1つの被験者グループは，1回の実験で全ての条件を試す場合

- randomized block design (RB デザイン)

例

ロボット1, ロボット2, ロボット3との被験者ごとのふれ合い時間の比較   

(要因１：ロボットの種類，要因２：個人差）


# 調べたい要因は2つ（要因1, 要因2）：二元配置

## 1人の被験者は，1回の実験で要因1・要因2共に，1つの条件しか試さない場合

- completely randomized factorial design (CRFpq デザイン)

例

「あるロボット」（複数の種類があり、1つ選ぶ）と「あるふれ合い方」（複数のふれ合い方があり，1つ選ぶ）の条件で，ロボットと複数の人に**1回**ふれ合ってもらう．  

## 1人の被験者 / 1つの被験者グループは，1回の実験で1つの要因1の条件と，全ての要因2の条件を試す場合

- split-plot design (SPFpq デザイン)


例

「あるロボット」（複数の種類があり、1つ選ぶ）と「あるふれ合い方」（複数のふれ合い方があり，全て選ぶ）の条件で，ロボットと複数の人にふれ合ってもらう．  

## 1人の被験者 / 1つの被験者グループは1回の実験で全ての要因1, 要因2の条件を試す場合

- randomized block factorial design (RBFpq デザイン)


例

「あるロボット」（複数の種類があり、全て選ぶ）と「あるふれ合い方」（複数のふれ合い方があり，全て選ぶ）の条件で，ロボットと複数の人にふれ合ってもらう．  


[注]

被験者グループ：


- 特定の剰余変数によって被験者をブロック化し，各ブロック内の被験者を各処理水準に無作為に割り当てる場合
- ブロック化は，被験者をグループ化して扱うこと（被験者を個人としては扱わない）  


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

# How to report results

- A one-way between subjects ANOVA

```
A one-way between subjects ANOVA was conducted to compare the effect of <name of the effect (IV); ex. type of athelete> on the <dependent variable; ex. number of pizza slices eaten>.

An analysis of variance showed that the effect of <name of the effect (IV)> on <dependent variable> was significant at the p<.05 level, F(<between groups dof, within groups dof>)=<F value>, p=<p value>. 

Post hoc comparisons using the <test name; ex. Tukey HSD test> indicated that the mean score for the <condition 1> (M=<mean value>, SD=<sd value>) was significantly different than the <condition 2> (M=<mean value>, SD=<sd value>). However, the <condition 3> (M=<mean value>, SD=<sd value>) did not significantly differ from <codition 1> and <condition 2>.
```

- A one-way repeated measures ANOVA

```
A one-way repeated measures ANOVA was conducted to compare the effect of <name of the effect (IV); ex. time of eating pizza slices> on the <dependent variable; ex. pizza slices consumed, before, during and after the season>.

These data consist of the <time of 30 people>. Each <person> was tested under <three times>. 

The results of a one-way repeated measures ANOVA show that the <time of eating pizza slices> was significantly affected by <pizza slices consimed, before, during and after the season>, F(4, 36) = 18.36, p<.001.

<Ver.1>
Post hoc comparisons using the <test name; ex. Tukey HSD test> indicated that the mean score for the <condition 1> (M=<mean value>, SD=<sd value>) was significantly different than the <condition 2> (M=<mean value>, SD=<sd value>). 
No other comparisons were significant.

<Ver. 2>
Three paired samples t-tests were used to make post hoc comparisons between conditions. 

A first paired samples t-test indicated that there was a significant difference between <the number of pizza slices eaten> <before> (M=<3.0>, SD=<.76>) and <during> (M=<6.3>, SD=<.71>) <the season>; t(<7>)=<6.62>, p=.<.000>.

A second paired samples t-test indicated that there was a significant difference between <the number of pizza slices eaten> <during> (M=<6.3>, SD=<.71>) and <after> (M=<1.4>, SD=<.52>) <the season>; t(<7>)=<13.91>, p=.<.000>.

A third paired samples t-test indicated that there was a significant difference between <the number of pizza slices eaten> <before> (M=<3.0>, SD=<.76>) and <after> (M=<1.4>, SD=<.52>) <the season>; t(<7>)=<6.18>, p=.<.000>.
```

- A two-way between subjects ANOVA (A factrial ANOVA)

```
A two-way between subjects ANOVA was conducted on the influence of two independent variables (<two varables>; ex. athlete type, age) on the number of <independent variable; ex. slices of pizza eaten in one sitting>. 

<Dependent variable1; ex. Athlete type> included <three> levels (<type1, type2, type3; ex. football, basketball, soccer players>) and <Dependent variable2; age> consisted of <two> levels (<type1, type2; ex. younger, older>). 

All effects were statistically significant at the .05 significance level except for <the Age factor>.

The main effect for <athelete> type yielded an F ratio of F(<2>, <63>)=<136.2>, p<.001, indicating a significant difference between <football players> (M=<9.39>, SD=<1.99>), <basketball players> (M=<5.17>, SD=<1.40>) and <soccer players> (M=<2.52>, SD=<1.53>).

The main effect for <age> yielded an F ratio of F(<1>, <63>)=<2.9>, p>.05, indicating the effect for age was not significant, younger (M=<5.97>, SD=<3.97>) and older (M=<5.39>, SD=<2.34>).

The interaction effect was significant, F(<2>, <63>)=<13.36>, p < .001.

Post hoc comparisons using the <test name; ex. Tukey HSD test> indicated that the mean score for the <condition 1> (M=<mean value>, SD=<sd value>) was significantly different than the <condition 2> (M=<mean value>, SD=<sd value>). 
No other comparisons were significant.
```

- A two-way mixed ANOVA (with one within-subjects factor and one between-groups factor)

```
The sleep quality (percentage of time spent in delta sleep) of women with secure, anxious or avoidant attachment styles (N = 3 x 10) was measured when sleeping with and without their partners. 

If a harmonious relationship has a stress reducing effect, we expect sleep quality to improve in the presence of their partner especially for securely attached women. 

A 3 x 2 ANOVA with Attachment Style as an independent factor and absence or Presence of Partner as a within-subjects factor was run. 

The analysis revealed a main effect of Partner Presence (F(1, 27) = 90.74, p < .001) in the predicted direction, a main effect of Attachment Style (F(2, 27) = 17.47, p < .001) and an interaction between Partner Presence and Attachment Style (F(2, 27) = 50.57, p > .001). 

As predicted, women with secure attachment styles slept better than either of the other two groups (p = .001) and they experienced the greatest improvement in sleep quality by the presence of their partners.
```

- A two-way repeated measures ANOVA 

```
We can report that there was a significant main effect of <looks>, F(<2>, <18>)=<66.44>, p<.001.
We can report that there was a significant main effect of <charisma>, F(<2>, <18>) =<274.89>, p<.001.
We can report that there was a significant interaction between <the attractiveness of the date and the charisma of the date>, F(<looks x charisma dof>, <error(looks x charisma) dof>) = <34.91>, p<.001.
```