---
categories:
- Studies
date: '2024-12-05'
tags:
- LG Aimers
title: Bias and Variance
toc: true
---


# Formal Definitions of ML
1. 먼저 학습 데이터와 모델 클래스(or hyper class)를 설정한다.
- Given training data and selected model class(a.k.a hypothesis class)
1. 주어진 모델에 대해 데이터에 알맞는 parameter를 예측한다.
- Goal: find (w, b) that predicts well on S (parameter estimation)
- Loss function(손실 함수): model의 예측값과 정답값이 틀릴 수록 큰 값을 반환하여 model을 평가
1. 학습이 최적화 문제로 변환된다.
- Learning objective (optimation)
즉, 최종적으로는 Loss를 최소화하는 w와 b를 찾는 과정이다.
# Generalization(일반화)
- An ML model’s ability to perform well on new unseen data rather than just the data that it was trained on.
Generalization(일반화)이 잘 되지 않으면(poor generalization) Overfitting이 발생할 수 있다.
# Generalizion Error
- Objective of learning
- True distiribution: P(x, y) (x와 y와의 모든 상관관계를 나타내는 집합)
- Train: Fit a hypothesis h(x)

## Generalization Error
- L_p(h) = E_{P(x, y)} [L(y, h(x))] (true distribution을 따르는 데이터에 대한 loss의 기댓값)
- Prediction loss on all possible cases
- Generalization: ability to perform well on previously unseen input
- Underfitting: Generalization error < Training error
- Overfitting: Generalization error > Training error
- Training an ML algorithm well
즉 먼저 Overfitting을 내고, 그 다음에 error를 낮추는 방식이 보편적이다.
# Model’s Capacity
![1. A linear function
2. A quadratic function
3. A polynomial of degree 9](/assets/images/bias_and_variance/image_20241205_090703.png)

좋은 모델은 무조건 복잡할(large capacity) 필요가 없다(오컴의 면도날).
# Typical Relation between Capacity and Error
Informally, a capacity is the function’s ability to fit a wide variety of functions.![](/assets/images/bias_and_variance/image_20241205_090703.png)

- Capacity가 높을 수록 training error는 무조건 줄어든다.
- 단, validation error는 증가할 수 있다.
- 즉, 최적의 지점을 가지는 capacity의 모델을 채택하는 것이 중요하다.

# Regularization(정규화)
- 최적화 문제 풀이를 위한 목적 함수(generalization loss가 최소화 되는 함수)를 찾는 것.
- Given an ML algorithm, a preference for one solution in its hypothesis space to another.
- The main objective of regularization is to reduce its generalization error but not its training error.
![최적의 capacity를 가지는 model을 선정하는 것도 좋지만, 좋은 regularization을 하는 것도 방법이다.](/assets/images/bias_and_variance/image_20241205_090704.png)


# Bias/Variance Decomposition
![](/assets/images/bias_and_variance/image_20241205_090704.png)


## Trade-off between Bias and Variance
- Two sources of error in an estimator: bias and variance
- Increasing capacity tends to increase variance and decrease bias
둘 다 낮추는 방법 중 하나로 Ensemble Learning이 활용된다.
# Overfitting vs Underfitting
- High variance implies **Overfitting**
Variance를 잡는 가장 좋은 방법은 training data를 많이 모으는 것이다.- High bias implies **Underfitting**
Bias를 잡는 방법은 model의 complexity를 올리는 것이다.