---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- Data Analysis
- 데이터분석
- PCA
title: '[Lecture] Feature Selection & Dimensionality Reduction'
toc: true
---

---


# Feature Selection

- 과적합 문제 해결하기
    - Bias와 Variance는 상충 관계
    - 과적합 문제는 Bias를 줄여도 Variance가 너무 커져서 발생
    - Bias를 조금 포기해도 Variance를 줄일 수 있는 방법?
- Feature 개수 줄이기
    - 주요 특징을 선택하고 나머지는 사용 X
    - Feature Selection Algorithm
- 정규화 수행 (Regularization)
    - 우리가 추정하는 파라미터 값의 크기를 조절해보자

### 선형 회귀 모델 (최소제곱합)의 문제

- 예측력 (Prediction accuracy) : 최소제곱합을 이용하는 파라미터 추정은 Bias를 줄이지만 Outlier 등에 크게 민감하므로 Variance가 크다.
    - 변수의 개수를 줄이거나 parameter 크기를 줄여서 해결할 순 없을까?
→ 결국 bias를 조금 희생하면서 variance 줄이기

- 해석 가능성 (Interpretability) : 모델 해석력을 높이기 위해서는 보다 적은 feature 사용해야

### Solution

- Best Subset Selection
    - 특성이 p개 있을 때, 모델 성능이 가장 좋아지는 특성 k개만 고르자.
    - 총 $$\frac{p!}{k!(p-k)!}$$의 부분집합 수를 탐색해야 함 (computationally expensive)
- Forward-stepwise selection (greedy algorithm)
    - 절편으로부터 시작하여, 가장 성능을 높이는 특성을 하나씩 추가
    - 성능이 가장 높을 때 선택 종료
    - 통계적으로 p-value를 활용하여 선택 가능

## Forward-stepwise selection (greedy algorithm)

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052502_c1eb2af08e4644ebb8e7ffd85c6ef6e1.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
이렇게 feature를 하나씩 추가한다.

</div>
</div>


## Backward-stepwise selection

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052505_1f5850e9e602419d9d30f4b0c3328ff6.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
        - 전체 특성을 포함한 full model에서 하나씩 제거한다
        - 가장 유의미하지 않은 변수부터 제거

</div>
</div>


# Regularization

![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052506_ddc5b2a00f1e486586254bab94f1f244.png)

과적합 방지를 위해 모델 복잡성을 최대한 줄여보자.


## Ridge Regression (L2-정규화)

- $$\beta$$의 제곱합에 대하여 penalty 부여
- $$\lambda ≥ 0$$이 정규화의 수준을 결정 → $$\lambda$$가 커질수록 제약이 더 강하게 걸림
- 비교적 작은 $$\beta$$들로 모델이 결정됨
- Input에 대한 scaling이 우선적으로 진행되어야 효과 볼 수 있음
![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052507_770d0df7ff474e94bb7ec8619e59756f.png)


## Lasso Regression (L1-정규화)

- $$\beta$$의 절댓값 합에 대하여 penalty 부여
- $$\lambda≥0$$이 정규화의 수준 결정 → $$\lambda$$가 커질수록 제약이 더 강하게 걸림
- $$\beta$$ 중 0이 많이 포함되어 모델이 결정됨 (특성 선택의 효과)
- Input에 대한 Scaling이 우선적으로 진행되어야 효과 볼 수 있음
![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052509_8aa9d2d47b2d45aca870c38fe413476d.png)


## Ridge vs. Lasso

- Ridge의 $$\beta$$들은 0과 가까워지지만 0이 되진 않음
- Lasso의 $$\beta$$들은 실제 0으로 많이 구성됨

# 주성분 분석; Principal Component Analysis


### 차원의 저주 (Curse of Dimensionality)

차원이 커질수록 공간이 너무 희소해짐 → 과적합 발생

> 🔴 고차원의 데이터를 낮은 차원으로 표현
→ 데이터의 Variance를 최대한으로 유지할 수 있는 축들을 찾아보자


### 정사영(projection) 다시 생각해보기

![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052510_fdfa5487019c4b15af90910a2d1b8b84.png)

![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052511_ba4533c2211b476298d8d2c12d4e05cd.png)

$$b$$**의 길이가 1이면 **$$a$$**와 **$$b$$**의 내적 **$$a^Tb$$**이 **$$a$$**를 **$$b$$**라는 축으로 정사영시킨 좌표를 결정한다.**


## Maximum variance principal component

- $$v_1, v_2, \cdots, v_p$$를 $$p$$개의 principal component라고 하자.
- Data $$X$$는 모두 평균=0 으로 centering 되어 있음
- Sample Variance를 maximize하는 방향 $$v$$ 찾기
컬럼 별로 평균 내어 편차 행렬 생성

![](/assets/images/lecture-feature_selection__dimensionality_reduction/image_20241212_052512_2882ea7d5664462ab9dcc283416cceaf.png)


