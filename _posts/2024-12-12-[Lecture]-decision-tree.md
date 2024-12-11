---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- model
title: '[Lecture] Decision Tree'
toc: true
---

> 🦜 **Decision Tree**\
데이터를 뿌리(root)로부터 말단의 잎(leaf)까지 순차적으로 분기하는 모델

- 뿌리 마디(Root node): 시작되는 마디
- 자식 마디(Child node): 특정 마디에서 분열된 마디
- 부모 마디(Parent node): 특정 마디의 상위 마디
- 끝 마디(Terminal node): 자식 마디가 없는 마디
- 중간 마디(Internal node): 부모/자식 마디 모두 있는 마디
- 가지(Branch): 뿌리 마디에서 끝 마디까지 중 가능한 경로 중 하나
- 깊이(Depth): 가지 중 가장 많은 마디의 수


> Regression, Classification 모두 사용 가능하다.

---


# CART, Classification and Regression Tree Algorithm

---

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
        1. 가능한 분할 모두 탐색

![](/assets/images/lecture-decision_tree/image_20241212_050000_2192f2743a394d8886ad0baa2796611a.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
        1. 가능한 분할 중 하나 고정

![](/assets/images/lecture-decision_tree/image_20241212_050001_6e88306391c64239b04cbc60ee5547b0.png)

</div>
</div>

- 고정된 분할에 대해 예측값 계산
<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-decision_tree/image_20241212_050003_ea38400843604a5b9f479dd775b13d24.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-decision_tree/image_20241212_050004_4f50a6497d08403296c88dc2c9e69e37.png)

![](/assets/images/lecture-decision_tree/image_20241212_050006_94ecd09994b84964a8b3d3c78646cdfc.png)

</div>
</div>

- 두 분할 $$v_1, v_2$$ 중 더 작은 값이 위의 방법이므로, 위의 분할을 택한다.
![](/assets/images/lecture-decision_tree/image_20241212_050007_94c851b54ef34921b0834f0be57d55d2.png)

문제는
1. 어떤 속성(feature)로 분할할 것인가?
2. 언제까지 분할할 것인가?
    → 기본적으로 분류 후 집합이 한 클래스로 몰리면 분할 종료.

---


## 분할 속성 선택


### 1. Reduction in Variance

![](/assets/images/lecture-decision_tree/image_20241212_050008_22a7392ae45c41619fc95080f138394e.png)

위의 데이터에서 feature는 총 네 가지(predictors)이고, $$y$$값, 즉 target은 `Hours Played` 이다.

1. 먼저 target 변수에 대한 표준편차(분산)을 구한다.
    1. 총 14개의 데이터이므로 $$n = 14$$
    1. $Average = \bar x = \frac{\sum x}{n} = 39.8$
    1. $Standard \ Deviation = S = \sqrt{\frac{\sum (x - \bar x)^2}{n}} = 9.32$
    1. $Coefficient \ of \ Variation = CV = \frac{S}{\bar x} * 100\% = 23\%$
1. feature 중 ‘Outlook’으로 분류된 후 target 변수에 대한 표준편차를 구한다.
    1. $S(T, X) = \sum_{c \in X} P(c)S(c)$
    1. 
![](/assets/images/lecture-decision_tree/image_20241212_050010_d81e0fc9de504ec5b97113ad9dd5e81c.png)

    - 분산 간의 차를 구하면 9.32 - 7.66 = 1.66이다. 이를 Reduction in Std라고 하고,
**가장 분산 감소량이 많은 속성을 선택한다.**

---


### 2. Information Entropy

> 샘플 집합의 순도(purity)를 측정하는 데에 가장 자주 사용된다.

샘플 집합 $$D$$의 $$k$$번째 클래스 샘플이 차지하는 비율이 $$p_k(k = 1, 2, \cdots , \lVert y \rVert)$$라고 한다면

가 정보 엔트로피 값이 된다.

Ent(D)의 값이 작을수록 $$D$$의 순도는 높아진다.

---

**예제**

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-decision_tree/image_20241212_050012_f964b634e42347609ae78d6fa2854770.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
$$Ent(D) = -\sum_{k=1}^2 p_k \log_2 p_k = -\frac{4}{6} \log_2 \frac{4}{6} + (-\frac{2}{6} log_2 \frac{2}{6})$$

이 된다.

</div>
</div>

---


### 3. Information Gain

Categorical variable $$a$$가 가질 수 있는 값이 $$V$$개 $${a^1, a^2, \cdots , a^V}$$ 있다고 할 때, $$a$$속성으로 분할하면 얻게 되는 정보 이득은

가 된다.

- 총 $$V$$개의 노드로 분할한다.
- $$v$$번째 분할 노드는 $$D$$의 속성 $$a$$에서 $$a^V$$값을 가지는 샘플을 모두 포함한다($$D^v$$).
> 가장 정보 이득이 큰 속성을 선택한다.

**예시**

1. ‘color’라는 feature(coloumn)을 선택하고, 해당 feature가 가질 수 있는 값의 개수 $$V$$를 구한다.
![](/assets/images/lecture-decision_tree/image_20241212_050013_f6e98e8f795540e0be4f846a1781b44e.png)

1. ‘green’의 샘플은 6개
’dark’의 샘플6개
’light’의 샘플은 5개 이고
이들에 대한 각각의 정보 엔트로피 값을 구한다.
![](/assets/images/lecture-decision_tree/image_20241212_050014_b06276bbd4b5490c8f49b85c141d0bae.png)

1. target에 대한 Entropy 값은 0.998이다 (ripe/unripe로 구분되는 속성으로 간주)
이제 정보 이득 값을 구한다.

![](/assets/images/lecture-decision_tree/image_20241212_050017_925576943fe44e7ba5b1f82dee490965.png)

1. 이제 다른 feature들에 대한 정보 이득 값도 구한다.
그 결과 ‘texture’ 컬럼이 가장 정보 이득률이 높았다.
![](/assets/images/lecture-decision_tree/image_20241212_050018_3d1ef8dc9cde419b9376a8fed38f7ad7.png)


### 4. Gain Ratio

Information Gain은 취할 수 있는 값의 수가 비교적 많은 속성에 유리하다. 따라서 이들의 ratio를 구한다.


### 5. Gini Index

샘플 집합 내 순도를 측정하는 다른 방법이다.

지니계수는 집합 $$D$$에서 임의의 두 개의 샘플을 골랐을 때, 고른 두 샘플이 서로 다른 클래스일 확률을 나타낸다.

**예제**

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-decision_tree/image_20241212_050020_228940c7c69f44008ea2a5f496402c7d.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
총 9개의 샘플 중 A, B 클래스로 분류하는 feature $$v_1$$를 가정하자.

그럼 각각의 지니값은 위와 같이 나오게 되고, 각 클래스가 전체에서 차지하는 비율을 지니값에 곱하여 합을 구하면 된다.

</div>
</div>

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-decision_tree/image_20241212_050022_56af3124c46e4bdc842d6478bb9f8465.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
$$Gini(D^A) = 1 - \frac{2}{2}^2 = 0$$

$$Gini(D^B) = 1 - \frac{7}{7}^2 = 0$$

$$Gini \ index(v_2) = \frac{2}{9} \cdot 0 + \frac{7}{9} \cdot 0 = 0$$

</div>
</div>

**예제**

![](/assets/images/lecture-decision_tree/image_20241212_050024_53800e4cd9c440d791087fde4e81d487.png)

---


# Pruning; 가지치기

- 과도한 반복을 가지 수를 너무 많이 만들어낸다.
- 그러면 과적합이 된다.
- 따라서 사전 가지치기(Pre-pruning)와 사후 가지치기(Post pruning)을 사용한다.
    - 사전 가지치기
        - 트리 생성 과정에서 각 노드에 대해 분할 전 미리 예측하여 노드 분할이 트리의 일반적 성능을 향상시킬 수 있다면 분할, 아니면 중지
    - 사후 가지치기
        - 트리를 완성하고, 상향식으로 위 노드가 터미널 노드로 바뀌었을 때 일반화 성능이 향상된다면 하위 트리 삭제.

