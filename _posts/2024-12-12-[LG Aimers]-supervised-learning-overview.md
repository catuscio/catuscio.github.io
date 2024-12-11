---
categories:
- Studies
date: '2024-12-12'
tags:
- LG Aimers
title: '[LG Aimers] Supervised Learning Overview'
toc: true
---


### 지도학습의 예시

- Image Classification
- Text Classification
- Next Word Prediction
- Translation
- Price Prediction

# Mathematical Approach

> 🔴 기본 가정은 다음과 같다.
- Data: $x \in X$ usually a vector
- Label: $y \in Y$
- Dataset: $(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \cdots (x^{(n)}, y^{(n)})$


# Before Machine Learning


### Rule-based Algorithms (based on expertise, knowledge)

전문가들의 도메인 지식에 기반한 Rule을 입력하여 수행. Rule이 복잡한 경우에는 수행이 어려움.


### Machine Learning

- Data based
데이터를 제공하면 알고리즘이 알아서 수행함.

> Machine Learning is…
*“the field of study that gives computers the ability to learn without being explicitly programmed.”*
- Arthur Lee Samuel

컴퓨터가 스스로 학습하게 하고, 컴퓨터 혹은 알고리즘이 스스로 규칙을 파악하도록 함.


---


# Supervised Learning: Setup

- True function: $$f^*$$, where $$f^*(x^{(i)}) = y^{(i)}$$    (정답 함수)
- Want to find $$g(x) \approx f^*(x)$$
- Function class: $$G$$
- Goal:
    - $g_\theta \approx f^*(x)$
    - $g_\theta \in G$
$$G$$** 클래스 안에 있는 **$$g_\theta$$** 함수 중 정답 함수에 가장 근사한 함수를 찾는 게 목적.**


## “가장 근사하는”의 기준

- 모든 Input $$x$$에 대해 정답 함수와 근사해야 한다. (Infeasible)
    - $g_\theta \approx f^*(x)$
- 그 Input 중에서도 주어진 데이터셋에 대해서 근사해야 한다.
    - $g_\theta(x^{(i)}) \approx f^*(x^{(i)}) = y^{(i)}$
- 함수값의 근사도를 비교할 수 있어야 한다 (측정 가능해야 한다)
**→ Loss를 통해 계산**

- **Pointwise Loss; 하나의 데이터값에 대한 손실**
    - MSE, Cross-entropy, etc.
    - $l(g_\theta(x^{(i)}, y^{(i)})$
- **Loss; 전체 손실**
    - $L(\theta) = \sum_{i=1}^n l(g_\theta(x^{(i)}, y^{(i)})$

## $$\therefore$$ Supervised Learning Pipeline

1. **함수 클래스 좁히기**
    1. 세상 모든 함수 중 정답 함수에 가까운 함수 유형 선택 (모델 선택)
1. **손실 함수 선택**
    1. MSE, Cross-Entropy 등
1. **손실 계산**
    1. Pointwise Loss를 계산해 Total Loss 계산
1. **문제 풀이**
    1. 손실함수로 표현된 수식 풀이
    1. 파라미터별로 묶어 수식 표현 후 미적분 적용

---


