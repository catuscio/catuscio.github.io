---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- Classification
- 분류
title: '[Lecture] Classifications: Other Issues'
toc: true
---

---


# k-NN; k-Nearest Neighbors


## 필요한 것들

- 클래스 라벨로 분류된 훈련 데이터셋
- 데이터 간의 ‘거리’를 측정하기 위한 proximity metric.
    - Euclidean distance : $$\sqrt{\sum_{i=1}^p (x_i - y_i)^2}$$
    - Manhattan : $$\sum_{i=1}^p \lVert x_i - y_i \rVert$$
    - Minkowski : $$(\sum_{i=1}^p (|x_i - y_i|^p))^{\frac{1}{p}}$$
![](/assets/images/lecture-classifications_other_issues/image_20241212_051639_73fb2a1c99624de6a0fb518bcd42c0df.png)

- k-최근접 이웃에 대한 파라미터 k
- Weighting Scheme
    - Unweighted classification : k개의 최근접 이웃 중 더 많은 클래스를 선택
    - Distance-weighted classification : 거리 d에 따라 weighted voting
        - 거리가 가까운 이웃에게 더 많은 가중치를 부여
            - $w(d) = 1/d^2$
            - $w(x, x_i) = \frac{\exp(-d(x,x_i))}{\sum_{j \in N_k (x_k)} \exp(-d(x, x_i))}$
- k 정하기
    - k가 너무 작으면 노이즈 데이터에 민감
    - k가 너무 크면 다른 클래스의 데이터를 많이 포함시킬 수 있음
    - Rule of Thumb : $$k < \sqrt n$$ is the number of examples
    - k가 커질 수록 경계가 smooth 해짐

### k-NN의 특징

- **Advantages**
    - Training 과정이 따로 필요하지 않다
    - 해석 가능하다
- **Disadvantages**
    - 개별 데이터에 대한 분류가 expensive 하다
    - 알맞은 거리 metric 고르기가 어려울 수 있다
    - 너무 많은 속성을 사용하는 것이 문제가 될 수 있다 → subset selection

# 분류 성능 평가


## Confusion Matrix; 혼동행렬

![](/assets/images/lecture-classifications_other_issues/image_20241212_051644_15e7b19a67f04b89928e10b3038a7311.png)

- $\text{Accuracy} = \frac{TP + TN}{TP + FN + FP + TN}$
    - **정확도;** 전체에서 맞춘 거 확률
- $\text{Precision} = \frac{TP}{TP+FP}$
    - **정밀도;** Yes 예측 중 맞춘 거 확률
- $\text{Recall} = \frac{TP}{TP+FN}$
    - **재현율;** 진짜 Yes 중 맞춘 거 확률
- $\text{F1 score} = \frac{2 * Precision * Recall}{Precision + Recall}$
    - Precision과 Recall의 조화 평균 (harmonic average)

## Cutoff value 정하기


### TPR / FPR Tradeoffs

- **TPR** : 실제 양성 중 모델이 양성으로 예측한 비율; sensitivity. Recall과 같음.
    - $\text{TPR} = \frac{TP}{TP + FN}$
- **FPR** : 실제 음성 중 모델이 음성으로 예측한 비율
    - $\text{FPR} = \frac{FP}{FP+TN}$
![](/assets/images/lecture-classifications_other_issues/image_20241212_051647_e35dd84d91374164966ae2e3b564a80c.png)


## ROC 커브 그려보기

**Receiver Operating Characteristic** Curve

x축은 FPR, y축은 TPR

![](/assets/images/lecture-classifications_other_issues/image_20241212_051648_4b479ab724074105881556a6ef9621fd.png)


### AUC; Area Under ROC curve

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-classifications_other_issues/image_20241212_051650_972b7a0e7c6944e3ae2bc6e6410095c8.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
        - 이상적인 경우 : AUC=1
        - Random guess : AUC=0.5
</div>
</div>

![](/assets/images/lecture-classifications_other_issues/image_20241212_051652_6de41ca825624e639951ebcfa40855c1.png)

