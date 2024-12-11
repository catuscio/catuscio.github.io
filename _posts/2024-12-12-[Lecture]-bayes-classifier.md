---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- Bayes
- 베이즈
- 확률
title: '[Lecture] Bayes Classifier'
toc: true
---


## Topology

- **조건부 확률 $$P(A \vert B)$$ :** B라고 했을 때 C일 확률
- **주변 확률 (Marginal probability) $$P(x)$$:** $$x$$ 자체의 분포.
- **사전 확률 (Prior probability) $$P(c)$$ :** 사전에 알고 있는 확률. $$c$$는 추정하고자 하는 값.
- **사후 확률 (Posterior probability) $$P(c \vert x)$$ :** $$x$$를 $$c$$로 분류했을 때 맞았을 확률
- **손실 (Loss) $$\lambda_{ij}$$ :** $$c_j$$인 $$x$$를 $$c_i$$로 분류했을 때의 손실. 0 or 1
- **기대 손실 (Expected loss) $$R(c \vert x)$$ :** $$x$$를 $$c$$로 분류했을 때 틀렸을 확률
- **우도 (Likelihood) $$P(x \vert c)$$ :** $$x$$의 분류가 $$c$$일 확률

# Bayesian Decision Theory


## **다중 분류 예시 (multi-class classification)**

> **목표 : 기대 손실 $$R(c \vert x)$$ 최소화**


### 정의

- $$N$$개의 분류 레이블 $$Y=\{ c_1, c_2, \cdots, c_N \}$$이 있고, **사후 확률 (Posterior probability) **$$P(c_i  \vert  x)$$에 기반하여 **샘플 **$$x$$**를 **$$c_i$$**로 분류**했을 때 발생하는 기대 손실 (expected loss)를 구할 수 있다.
- 이 때 $$\lambda_{ij}$$는 실제 레이블이 $$c_j$$인 샘플이 $$c_i$$로 잘못 분류했을 때 발생하는 손실
    - $$R(c_i  \vert  x) = \sum_{j=1}^N \lambda_{ij} P(c_j \vert x)$$
    - $$x$$를 $$c_i$$로 분류했을 때 기대 손실(expected loss)
= (실제로는 $$c_j$$인 데이터의 손실) $$\times$$ (사후 확률)

- 판별 기준 $$h:X→Y$$를 찾아 전체 손실을 최소화해야 한다.
    - $R(h)=\mathbb{E}_x[R(h(x)) \vert x)]$
> 🔴 $$x$$를 $$c_i$$로 분류했을 때 **기대 손실(expected loss)**


### 해결

- 각 샘플 $$x$$에 대해 손실 $$R(h(x) \vert x)$$ 최소화 → 전체 리스크 최소화
- **베이즈 결정 규칙**
    - 각 샘플에 대하여 $$R(c \vert x)$$를 최소화하는 클래스 레이블 선택
        - $h^*(x) = \mathrm{argmin}_{c \in Y} R(c \vert x)$
    - $$h^*$$<u>는 베이즈 최적 분류기 (Bayes Optimal Classifer)!</u>
- 만약 목표가 분류기의 오차율 (misclassification rate)을 최소화 하는 것이라면
    - $\lambda_{ij} = \begin{cases} 0, & \text{if } i = j \\ 1, & \text{otherwise} \end{cases}$
    - $$R(c_i  \vert  x) = 1 - P(c_i  \vert  x)$$ (conditionl risk) 이므로
    - $$h^*(x) = \mathrm{argmax}_{c \in Y} P(c \vert x)$$ → (R을 P로 바꿈)
- <u>각 샘플 </u>$$x$$<u>에 대해 사후 확률 </u>$$P(c \vert x)$$<u>를 최대화 할 수 있는 클래스 레이블을 선택!</u>
> 🔴 1. 전체 손실 $$R(h)=\mathbb{E}_x[R(h(x)) \vert x)]$$를 최소화 해야 하므로
각 샘플에 대한 손실 $$R(h(x) \vert x)$$을 최소화 한다.

2. 이를 수식으로 나타내면 $$h^*(x) = \mathrm{argmin}_{c \in Y} R(c \vert x)$$

3. R = 1 - P 이므로 다른 표현으로는 $$h^*(x) = \mathrm{argmax}_{c \in Y} P(c \vert x)$$


## 베이즈 정리 (Bayes Theorem)

> **목표 : 사후 확률 $$P(c \vert x)$$ 도출**

$$P(c \vert x) = \frac{P(c)P(x \vert c)}{P(x)}$$

(사후 확률) = (사전 확률) $$\times$$(우도) $$\div$$ (주변 확률)

- Marginal probability $$P(x)$$는 상수
- Prior probability $$P(c)$$는 출현 빈도를 통해 계산 가능
- Likelihood는 어케 구함?

# 최대 우도 측정; Maximum Likelihood Estimation

우도가 정해진 형식이 있고, 파라미터 $$\theta_c$$에 의해서만 결정됨

$$D_c$$로 훈련세트 $$D$$에서 $$c$$클래스 샘플로 구성된 집합을 나타내고, 이런 샘플들이 독립항등분포(iid)라고 가정했을 때, 데이터세트 $$D_c$$에 대한 파라미터 $$\theta_c$$의 우도는 다음과 같다.

$$P(D_c \vert \theta_c) = \prod_{x \in D_c} P(x \vert \theta_c)$$

곱셈을 피해 로그 우도를 사용하면

$$LL(\theta_c)=\log P(D_c \vert \theta_c) = \sum_{x \in D_c} \log P(x \vert \theta_c)$$


## MLE; Maximum Likelihood Estimation

![](/assets/images/lecture-bayes_classifier/image_20241212_051024_f65caaf05cf0401f8c25f21cc0bba451.png)

동전 던지기 : $$D = (x_1, x_2, \cdots, x_7) = (H, H, T, T, H, H, H)$$

각 샘플들이 아래의 베르누이 분포를 따르며, 독립적이라고 한다면 MLE로 추정한 $$\theta$$는?

$$P(x \vert \theta) = \begin{cases} \theta & x = H \\ 1-\theta & \text{if } x=T \end{cases}$$

**sol**

$\text{Likelihood} = \theta^5(1-\theta)^2$

을 maximize 하는 $$\theta$$를 구하자.

$LL = 5\ln\theta + 2\ln(1-\theta)$

양 변에 음수 취하면

$-LL = -5\ln\theta - 2\ln(1-\theta)$

LL이 0이 되도록 하는 $$\theta$$ 값은

$-\frac{5}{\theta} + \frac{2}{1-\theta} =0$

양변에 $$\theta(1-\theta)$$를 곱하면

$\theta = \frac{5}{7}$


### MLE의 한계

- 추정 결과의 정확성이 **가정하는 확률 분포 형식이 잠재적인 실제 데이터 분포와 얼마나 일치하는지에 과하게 의존**한다.
- 이상한 확률 분포 쓰면 좆될 수 있다!

# 나이브 베이즈 분류기; Naive Bayes Classifier

파라미터화 없이 (== 분포 가정 없이) 분류할 수 있는 방법은 없을까?

문제는 우도가 **모든 속성(feature)에 대한 결합 확률**이기 때문에 유한한 훈련 샘플만으로는 추정이 어렵다.

따라서 나이브 베이즈 분류기는 **속성 조건독립 가설 (Attribute Conditional Independence Assumption)을 이용한다.**

이건 걍 과제 봐라~~



## 계산 방법

- Prior
전체 데이터 D에 대해 c 클래스 샘플로 구성된 집합을 D_c라고 하면, 클래스 prior는

$P(c) = \frac{ \vert D_c \vert }{ \vert D \vert }$

- Likelihood
$$D_{c,x_i}$$를 $$D_c$$ 중에 속성 i상에서의 값이 $$x_i$$인 샘플로 구성된 집합으로 나타낸다면, 속성별 우도 $$P(x_i \vert c)$$는

$$P(x_i \vert c) = \frac{ \vert D_{c,x_i} \vert }{ \vert D_c \vert }$$

$$= \frac{1}{\sqrt{2\pi}\sigma_{c,i}} \exp (-\frac{(x_i - \mu_{c,i})^2}{2\sigma_{c,i}^2})$$


## 라플라시안 보정 (Laplacian Correction)

해당 컬럼의 클래스 개수를 N이라 하자.

![](/assets/images/lecture-bayes_classifier/image_20241212_051026_8adf0c8a1d61437ea9be66f005b6cd4b.png)

$\ln{(2\pi\sigma_c^2)^{-\frac{n}{2}}}$


