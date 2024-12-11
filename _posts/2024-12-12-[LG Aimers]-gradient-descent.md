---
categories:
- Studies
date: '2024-12-12'
tags:
- LG Aimers
title: '[LG Aimers] Gradient Descent'
toc: true
---


# Overview

- We have some function (loss function)
    - $J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2$
- and want
    - $\min_{\theta_0, \theta_1}J(\theta_0, \theta_1)$
- Algorithm outline
    - Start with some initial parameters $$\theta_0, \theta_1$$
    - Keep changing the parameter to reduce the loss function until we hopefully end up at a minimum.
> 💡 repeat until convergence { \
$\theta_j := \theta_j - \alpha \frac{\partial}{\partial\theta_j}J(\theta_0, \theta_1)$ \
}

- **Gradient**: partial derivative of vector function
    - Direction of greatest increase (or decrease) of a function
- **Step size **$$\alpha$$: affects rate of the downside movement of the vector on error surface
    - Must be a positive number
    - **Hyper parameter**
    - If its too small, GD can be slow; if its too large, GD can overshoot the minimum and fail to converge (or diverge)
- $$\theta$$: **Learnable parameters**
- **Objective function **$$J$$: What we have to minimize
![](/assets/images/lg_aimers-gradient_descent/image_20241212_040434_6b7624ced73c4a6297784c0be242c82b.png)


# Batch gradient descent

> 💡 repeat until convergence {\
    $\theta_0 := \theta_0 - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})$ \
    $\theta_1 := \theta_1 - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)}) - y^{(i)})\cdot x^{(i)}$ \
}

Linear regression model

$$h_\theta(x) = \theta_0 + \theta_1 x$$

$$J(\theta_0, \theta_1) = \frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2$$

- 선형회귀 모델에서 목적함수 $$J$$의 편미분을 삽입하여 $$\theta_0, \theta_1$$을 바꿈.
- Sample size $$m$$이 너무 커지면 계산 복잡도가 늘어남.

# Stochastic gradient descent (SGD)

> 💡 repeat until convergence { \
$\theta_0 := \theta_0 - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})$ \
$\theta_1 := \theta_1 - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)}) - y^{(i)})\cdot x^{(i)}$ \
}

- SGD는 $$m=1$$로 계산한다.
- Batch GD에 비해 빠르지만, 각 샘플 하나하나마다 계산하므로 노이즈에 취약하다. (oscillation occur)

# Limitation : Local Optimum

$$\theta_j := \theta_j - \alpha \frac{\partial}{\partial\theta_j}J(\theta_0, \theta_1)$$

![](/assets/images/lg_aimers-gradient_descent/image_20241212_040435_81415798a20c48998c1d2d1f5fd78434.png)

>*GD algorithm의 시작 위치에 따라 local minimum과 global minimum 중 하나가 발생하게 되는 오류가 있다.*

- Critical points with zero slope: $$\nabla_xf(x)=0$$ gives no information about which direction to move
    - Gradient가 0이 되어 더 이상 작동하지 않계 되는 문제점.

# Ideas to avoid local minimum


## Momentum

과거에 Gradient가 업데이트 되어오던 방향 및 속도를 어느 정도 반영해서 현재 포인트에서 Gradient가 0이 되더라도 계속해서 학습을 진행할 수 있는 동력을 제공하게 되는 것

- SGD: widely used but slow and difficult to reach the minimum
- Momentum
    - speed up learnining in high curvature and small/noise gradient
    - Exponentially weighted moving average of past gradients (low pass filtering)
> 💡 
    $$v_t = \begin{cases} g_1, & t = 1\\ \rho v_{t-1} + (1-\rho)g_t, & t>1 \end{cases}$$
    > - $$v_t$$ : Momentum. Exponentially weighted moving average at time $$t$$
    > - $$g_t$$ : observation gradient at time $$t$$
    > - $$\rho$$ (0~1) : degree of weighting decrease (smoothing factor)

c.f) recursive equation → exponentially weighted average moving

$$v_t = \rho^k v_{t-k} + (1-\rho)[g_t + \rho g_{t-1} + \cdots + \rho^{k-1} g_{t-k+1}]$$


