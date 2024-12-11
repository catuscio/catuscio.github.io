---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- Ensemble
- 앙상블
title: '[Lecture] Ensemble Methods'
toc: true
---

---


### Topology

- **객체 학습기 (Individual Learner)**
    - 앙상블 학습에 사용하는 개별 모델
- **동질적 앙상블 (Homogeneous Ensemble)**
    - 앙상블에 같은 형태의 객체 학습기만 사용할 경우
    - 동질적 앙상블에서 사용하는 객체 학습기는 **기초 학습기 (Base Learner)**라고 함
    - 이러한 학습 알고리즘을 기초 학습 알고리즘이라고 함
- **이질적 앙상블 (Heterogeneous Ensemble)**
    - 다른 형태의 객체 학습기 사용할 경우
    - **요소 학습기 (Component Learner)**라고 함

# 객체와 앙상블


### 이진 분류

![](/assets/images/lecture-ensemble_methods/image_20241212_052312_fa7ada2b29f540a3bb18c5e8c9389734.png)

![](/assets/images/lecture-ensemble_methods/image_20241212_052313_504ffb4335854563bdc80265b7454272.png)

- Hard Voting은 박정희식 / Soft Voting은 민주주의
> 🔴 앙상블 학습은 다수의 학습기가 결합해 단일 학습기보다 우수한 일반화 성능을 얻는다
- 일정 수준의 개별 모델의 정확성 필요하다.
- 다양성도 필요하다.


# Bagging & Random Forest


## 부트스트랩 샘플링 (Bootstrap Sampling)

- $$m$$개의 샘플이 있는 데이터셋 $$D$$에 대해, 샘플링을 거쳐 데이터셋 $$D’$$를 만든다.
- 복원추출로 $$m$$개의 데이터셋을 가진 $$D’$$ 생성 가능
- 따라서 어떤 샘플들은 아예 안 뽑힌다.
    - 전체 데이터셋 중 약 36.8%는 아예 안 들어간다
![](/assets/images/lecture-ensemble_methods/image_20241212_052315_11237b4d214f4a72aac1168740ee1469.png)


## Bagging; Bootstrap AGGregatING

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
        - **동질적 앙상블**
        - T번의 m회 복원 추출로 데이터셋 T개 구성
        - T개의 서로 다른 기초 학습기 훈련
        - 예측
            - 회귀 : 평균법
            - 분류 : 단순 투표

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-ensemble_methods/image_20241212_052317_ad9625940d3d4adc8ac62e3afca0401b.png)

</div>
</div>

- 각 기초 학습기는 초기 훈련 데이터의 63.2%만 학습
- 나머지 데이터로는 일반화 성능 측정 (Validation set)
→ OOB (Out-Of-Bag) 평가 진행 (가지치기, 검증 데이터셋의 역할)

![](/assets/images/lecture-ensemble_methods/image_20241212_052319_a4bebd3f507e4062b775392338754c6b.png)


### 배깅은 왜 좋을까?

**편향-분산 트레이드오프 (Bias-Variance Trade-off) 덕분**

- **Bias-Variance Decomposition**
실제 데이터의 관계를 $$y = f(x) + \epsilon,  \epsilon ~ N(0, \sigma^2)$$이라고 가정해보자.

학습할 모델을 $$\hat f(x)$$라 하면

$$MSE = E[(y-\hat y)^2] = Bias(\hat f(x))^2 + Var(\hat f(x)) + \sigma^2$$

> 🔴 X, Y가 독립일 때
1) E[XY] = E[X]E[Y]
2) Var(X+Y) = Var(X) + Var(Y)
3) E[X^2] = Var[X] + (E[X])^2 → 분산 = 제평+평

![](/assets/images/lecture-ensemble_methods/image_20241212_052320_564667d1a0db4bd4acc58da6c31f117b.png)

![](/assets/images/lecture-ensemble_methods/image_20241212_052322_54e41ee528644d3380144cf4fe372cc8.png)

배깅을 통해 Variance를 줄일 수 있다 (Low bias / High Variance 학습기들에 대해 효과적)

- T개의 i.i.d random variable (각각의 분산 : $$\sigma^2$$)을 평균 내면 분산은 $$\frac{1}{T}\sigma^2$$으로 감소한다.
    - 만약 서로 다른 RV라면 이들 간의 상관계수가 $$\rho$$일 때 분산은
$$\rho \sigma^2 + \frac{1-\rho}{T} \sigma^2$$

![](/assets/images/lecture-ensemble_methods/image_20241212_052323_678540773216428db92c3477fbb64426.png)

→ 상관관계 $$\rho$$를 줄이기 위해서는 서로 다른 모델이 필요하다.


## Random Forest

- 샘플링 뿐만 아니라 **속성 선택에 대해서도 랜덤성 부여**
- Decision Tree → 분할 속성 선택 시 최적의 속성 하나 선택
- 랜덤 포레스트는 각 노드에 대해 각 노드의 속성 집합 중 랜덤으로 k개의 속성 부분집합을 선택하고, 여기서 최적 속성을 선택한다.
- k는 임의성을 조절하는 파라미터.
- 추천 : $$k = \log_2d$$
![](/assets/images/lecture-ensemble_methods/image_20241212_052325_2f72215f77c94c82a00e308087f842ae.png)

![](/assets/images/lecture-ensemble_methods/image_20241212_052326_edfc69840d0645f7be4bb02fc464e4cb.png)

![](/assets/images/lecture-ensemble_methods/image_20241212_052327_d7a9770358684072b7ebc8a0dc94eeb5.png)

![](/assets/images/lecture-ensemble_methods/image_20241212_052329_a32ab61405084df5b65f2c2c2975bee7.png)

![](/assets/images/lecture-ensemble_methods/image_20241212_052330_6f012b1c6d0e4122a99b1f6343e01182.png)

- 랜덤 포레스트의 초기 성능은 좋지 않음
- 학습기 숫자가 늘어날 수록 배깅에 비해 좋은 성능 보임
- 배깅 보다 좋은 훈련 효율 → 배깅이 계산량이 많음
- `n_estimators` = T / `max_features` = k

