---
categories:
- Studies
date: '2024-12-12'
tags:
- LG Aimers
title: '[LG Aimers] Linear Regression'
toc: true
---

- Hypothesis set $$H$$ : a set of lines
    - $h_w(x) = \theta_0 + \theta_1x_1 \cdots + \theta_dx_d = \theta^Tx$
    - $$\theta$$ : model parameter(learnable), $$d$$ : input feature dimension
    - $h_w(x) = \theta_0 + \theta_1k_1(x_1) + \cdots + \theta_dk_d(x_d) = \theta^Tk(x)$
        - e.g. $$k_n(x) = x^n$$
- Good for a first try
    - Simplicity: easy to implement and interpret
    - Generalization: higher chance $$E_{test} \approx E_{train}$$
    - Solve regression and classification problems


# Linear regression framework

1. Which predictor? - Hypothesis class
    1. $h_\theta = \theta_0 + \theta_1 x$
    1. Univariate linear model(input feature가 한개면 uni, 두개 이상이면multivariate)
1. How good is a predictor? - Loss function
    1. Minimizing MSE : $$\frac{1}{2m} \sum_{i=1}^m (h_\theta(x_i) - y_i)^2$$
1. How to compute the best predictor? - Optimization algorithm
    1. Gradient descent algorithm
    1. etc…


# Parameter optimization

Choose $$\theta_0$$, $$\theta_1$$ so that $$h_\theta (x)$$ is close to $$y$$ using ourt training set

- Gradient = $$\theta_1$$ = 기울기
- Offset = $$\theta_0$$ = y절편

## Cost function(Loss function)

- Goal: minimizing MSE
    - $J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x_i)-y_i)^2$
    - Minimize $$J(\theta_0, \theta_1)$$
![](/assets/images/lg_aimers-linear_regression/image_20241212_040414_d996dd49b63b4f479198b080fa89e7cc.png)

>*3D visualization of $$\theta_0$$, $$\theta_1$$, $$J$$; we call this Error surface*


## Optimization - Matrix representation in data

d-dimensional features.

- Data matrix $$X \in \mathbb{R}^{N \times (d+1)}$$
    - rows vector: inputs as $$x^m \in \mathbb{R}^{1 \times (d+1)}$$
        - $$X = \begin{bmatrix} 1 & x_1^0 & x_2^0 & \cdots & x_d^0 \\ 1 & x_1^1 & x_2^1 & \cdots & x_d^1 \\ 1 & x_1^2 & x_2^2 & \cdots & x_d^2 \\ \cdots & \cdots & \cdots & \cdots & \cdots \\ 1 & x_1^{N-1} & x_2^{N-1} & \cdots & x_d^{N-1} \end{bmatrix}$$
        - 앞 열의 1은 Offset을 의미함.
- Target vector


