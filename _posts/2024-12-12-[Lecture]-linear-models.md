---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- model
title: '[Lecture] Linear Models'
toc: true
---


# Linear Regression; 선형 회귀

> 🦜 **Linear Model; 선형 모델**\
독립변수 $$x$$로 종속변수 $$y$$를 예측하는 모델
→ 속성들의 선형 조합을 통해 예측하는 함수를 학습하는 모델


### $$f(x) = \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_d x_d + b$$

- Parameter; 파라미터
    - 학습을 통해 얻어야 하는 값
    - $$\beta, b$$
**→ **$$f(x) = \beta^T x + b$$** (벡터 형태)**


# 선형회귀의 손실함수 (Loss function)

> MSE, Mean Squared Error; 평균 제곱 오차

$$MSE = \frac{1}{m} \sum_{i=1}^m (f(x_i) - y_i)^2 = \frac{1}{m} \sum_{i=1}^m (y_i - (b + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_d x_{id}))^2$$

- Input feature가 하나 뿐인 경우
    - $f(x_i) = \beta x_i + b$
    - $MSE = \frac{1}{m} \sum_{i=1}^m (y_i - (\beta x_i + b))^2$

## Least Square Method; 최소제곱법

$$\beta, b$$를 찾는 것은 $$E_{(\beta, b)} = \sum_{i=1}^m (y_i - \beta x_i - b)^2$$를 최소화 하는 과정이다.

![](/assets/images/lecture-linear_models/image_20241212_045756_1b468c15130f4aabafb0d5eb3f0a140d.png)

이므로

![](/assets/images/lecture-linear_models/image_20241212_045758_7c41103b25474299b56337364fa3f832.png)

이다.


## Multivariate Linear Regression

> Feature가 여러 개라면 행렬 형태로 표현한다.

![](/assets/images/lecture-linear_models/image_20241212_045758_2e8bf034a74c411c98e4564e0e2af1fb.png)


