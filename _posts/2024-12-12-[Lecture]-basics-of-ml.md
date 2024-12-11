---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- ML
title: '[Lecture] Basics of ML'
toc: true
---


## 머신러닝이란?

데이터로부터 규칙을 학습하는 프로그래밍 (혹은 패턴 인식)


## 지도/교사 학습(Supervised Learning)

- 데이터와 정답을 함께 제공하여 학습하게 하는 알고리즘
    - Regression(회귀) → 연속적인 값 예측(Continuous)
    - Classification(분류) → 이산적인 값 예측(Discrete)
![](/assets/images/lecture-basics_of_ml/image_20241212_043905_3ed9b15fa80842e0a6c4206cdfcdcaba.png)


### 지도학습의 목표

> 가장 이상적인 모델(Ideal model) $$F$$을 근사할 수 있는 현실 모델(Real model) $$f$$를 만드는 것\
→ 실제 출력값 $$y$$와 예측값 $$\hat y$$를 비슷하도록 $$f$$를 학습하자\
→ $$y$$와 $$\hat y$$의 차이 $$\Delta$$를 줄이자.


### 차이(Loss)를 정의하는 방법

절댓값 $$\lVert y-\hat y \rVert $$ 과 제곱값 $$(y-\hat y)^2$$

> **손실함수(**$$L$$**, Loss Function)**
- 최적화 문제에서는 손실함수를 최소화 하고자 함. 어떤 학습의 ‘비용’

### $$L$$, Loss Function

> 🥬 평균 제곱 오차(MSE, Mean Squared Error)\
$$L = \frac{1}{n} \sum_{i=1}^n(\hat y_i - y_i)^2$$

Loss를 최소화하는 방법에는 다음이 있다.

- **닫힌 해(Closed-form solution)**
    - 데이터와 손실 함수가 주어지면 최적의 모델이 계산을 통해 도출되는 것
    - e.g. 정규방정식(Normal Equation)
- **규칙 기반 최적화(Rule-based optimization)**
    - 사전에 지정된 규칙을 통해 손실 함수를 줄여 나가는 것
    - e.g. 의사결정나무(Decision Tree)
- **경사하강법(Gradient Descent)**
    - 반복해서 손실 함수를 줄이는 방향으로 움직이는 것

### Over/Underfitting

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-basics_of_ml/image_20241212_043908_0acfc2d8a78843a09134f6a93839ee4e.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
편향(Bias)과 분산(Variance)


![](/assets/images/lecture-basics_of_ml/image_20241212_043910_f2534cf84188412e9ed2a08c64ba4e35.png)

과적합을 방지하기 위해 Train/Test split을 한다.



</div>
</div>


### 지도학습의 전개

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-basics_of_ml/image_20241212_043912_06298eb8b3c94d4295530ddfc3cc7447.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
        1. 데이터 수집 및 분석/전처리
        1. Train/Test set으로 데이터 분할
        1. 모델 후보군 설정
        1. 손실 함수 및 탐색 방법 설정
        1. Training Set을 통한 모델 학습
            1. 필요시 Validation set으로 모델 성능 비교
        1. Test set을 통한 성능/과적합 확인
        1. (1-6) 반복
</div>
</div>


## 비지도/비교사 학습(Unsupervised Learning)

- 데이터만을 제공하여 학습하게 하는 알고리즘
    - Clustering
    - Recommendation System
![](/assets/images/lecture-basics_of_ml/image_20241212_043915_43ab70ef1d574cffb9d68d3711dda246.png)

