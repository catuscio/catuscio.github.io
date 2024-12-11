---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
- Clustering
- 군집화
title: '[Lecture] Clustering'
toc: true
---


- Unsupervised Learning

### 군집화 적용 사례

- 데이터에 대한 이해 (Data Understanding)
    - 시장세분화 (Market Segmentation) : 유사한 소비집단을 그룹화 하는 작업
- 데이터에 대한 요약 (Data Summarization)
    - 큰 데이터에 대한 크기 축소 → 시각화에 도움
- 이상 탐지 (Anomaly Detection)
    - 이상치 (Outliers)들은 군집으로부터 멀리 떨어져 있다.
    - 이상치의 개수는 매우 적다
    - ‘일반적인 데이터란 무엇’인지 학습하고, 이상치 발견 시 대응한다.

### 군집화의 종류

- 분할식 클러스터링 (Partitional Clustering)
    - 데이터들을 서로 겹치지 않는 군집으로 분리한다. (K-means clustering)
- 계층적 클러스터링 (Hierarchical Clustering)
    - 데이터를 계층적으로 군집화한다. (agglomerative clustering, divisive clustering)
- 밀도 기반 클러스터링 (Density-based Clustering)
    - 데이터들의 밀도나 분포 형태를 활용하여 군집화를 진행 (DBSCAN)
<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-clustering/image_20241212_051948_a6f4eb3753e64d6d8753b58d019aa812.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-clustering/image_20241212_051950_29e4b81cce5b4816a9981f1a68e44dd1.png)

</div>
</div>


# K-Means Clustering; K-평균 군집화

- 분할식 클러스터링 → 군집 개수 = K
- 모든 클러스터는 centroid라고 하는 중심과 연관되어 있음 (mean or median)

## Algorithm

1. 데이터에서 K개의 임의의 centroid를 뽑아 initial cluster center로 사용한다.
1. 각각의 데이터 샘플을 가장 가까운 centroid에 할당한다.
1. Centroid를 추가된 샘플과의 중심으로 이동시킨다.
1. 다시 데이터 포인트들을 가장 가가운 centroid의 군집으로 이동시킨다
1. Repeat

- **종료 조건** : 더 이상 centroid가 움직이지 않거나 / 사용자가 지정한 tolerance나 maximum number of iteration 까지 반복
- 초기 K개의 centroid를 어떻게 정하냐에 따라 결과가 달라진다.
    - 여러 번 해보자 (잘 된다는 보장 없다..)
    - K개보다 많은 centroid를 랜덤하게 고르고 이들 중 거리가 먼 K개를 고르자
    - K-Means ++?
        - 각 점에 대해 거리 기반의 점수를 매김
        - Score가 높으면 뽑힐 확률 Up

## K 정하기

- 데이터 샘플 간 거리 측정은 **Squared Euclidean Distance**가 흔함.
- $$m$$-차원 공간의 두 점 $$x, y$$의 거리는,
    - $d(x,y)^2 = \sum_{j=1}^m (x_j - y_j)^2 = |x - y|_2^2$
        - $$j$$는 $$j$$번째 feature를 의미
- Squred euclidean distance를 사용할 때, k-means clustering은 **with-in cluster Sum of Squared Errors(SSE)**를 최소화하는 최적화 문제가 된다. (이를 cluster inertia라고도 함)


$$SSE = \sum_{i=1}^n \sum_{j=1}^k w^{(i,j)} |x^{(i)} - \mu^{(j)}|_2^2$$
- $$\mu^{(j)}$$는 cluster $$j$$의 centroid
- $$x^{(i)}$$가 cluster $$j$$에 포함 되면 $$w^{(i,j)} = 1$$ or $$w^{(i,j)} = 0$$
- 이걸 최소화 해야됨.
- e.g.
<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-clustering/image_20241212_051953_79a52895c5934b2eb6955d378c2a719a.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
centroid : $$(\frac{4}{3}, \frac{4}{3})$$

        - 우측 수식은
            - 왼쪽:x축
            - 오른쪽:y축
</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-clustering/image_20241212_051955_45bda6cee6ad4bc59431c90beb7a914d.png)

</div>
</div>

- **K⬆️ → SSE⬇️**
- Elbow method로 SSE의 감소량이 작아지는 구간에서 K를 선택하는 게 좋다.
![](/assets/images/lecture-clustering/image_20241212_051957_22802c9d02584b8b834d315146355529.png)


## 실루엣 (Silhouette plot)을 통한 클러스터링의 Quality 측정

- 실제 데이터로 실루엣 분석 실시(잘 된 경우)
![](/assets/images/lecture-clustering/image_20241212_051958_3f7ecf50dae94d8cbbcae8d40e3ff67f.png)

- 잘 안 된 경우
![](/assets/images/lecture-clustering/image_20241212_051959_7f1bfc208e7b42cd98ea20ca5da87ca4.png)


## K-평균 군집화의 단점

- 크기가 다른 군집에 대하여 취약하다
- 서로 다른 밀도를 가진 군집들에 대하여 취약하다.
- 구 형태(sphere)가 아닌 군집에 대하여 취약하다 → 밀도 기반 클러스터링 사용

## 정리

- **Advantages**
    - 이해가 쉽고, 구현이 간단하다
    - 큰 데이터셋에 대하여도 비교적 빠른 시간에 군집화를 해낼 수 있다.
- **Disadvantages**
    - K를 정하고 시작하여야 한다.
    - 초기 centroid에 따라 군집화 결과가 달라질 수 있다.
    - Outlier에 대하여 민감하다 → mean 대신 median을 사용하여 해결 가능

# 계층적 클러스터링; Hierarchical Clustering

- Dendrogram을 그릴 수 있고
- 클러스터 수를 초기에 정해줄 필요가 없다
- $$n \times n$$ 거리행렬을 계산해야 되므로 비용이 많이 들 수 있으며
- 데이터를 한번만 통과시키므로 초기에 데이터가 잘못된 군집에 속하게 되면 수정이 불가능 하다.

## 응집적 클러스터링 (Agglomerative Clustering)

- 서로 가장 가까운 두 군집을 연결한다
    1. 데이터 간의 거리는 유클리드 거리를 사용한다
    1. 군집 간의 거리는 다양한 방법이 있다.

### 군집 간 거리 계산 법

- **단일 연결법 (Single Linkage)**
    - 두 군집의 샘플 간의 최소 거리를 사용하여, 최소 거리가 가장 작은 군집끼리 합친다.
![](/assets/images/lecture-clustering/image_20241212_052001_68791f47a5d34ce5886737c8e29f3196.png)

- **완전 연결법 (Complete Linkage)**
    - 두 군집의 샘플 간의 최대 거리를 사용하여 군집끼리 합친다.
![](/assets/images/lecture-clustering/image_20241212_052003_e0703a94bb4d4b64a543705e501b09d3.png)

- **평균 연결법 (Average Linkage)**
    - 군집 내 모든 샘플 간의 평균 거리 (가장 많이 사용됨)
    - Outlier / noise에 강건하다.
![](/assets/images/lecture-clustering/image_20241212_052005_11731061a5844ea3a177957c1b99cad6.png)

![](/assets/images/lecture-clustering/image_20241212_052006_735362b03d1546ca91ce1d3813039346.png)

<div class='column-list' style='display: flex; gap: 1em;'>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-clustering/image_20241212_052007_64a81e4b9d2b4f7d8c620e3604928638.png)

</div>
<div class='column' style='flex: 1; padding: 0.5em; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;'>
![](/assets/images/lecture-clustering/image_20241212_052009_462705c7c1e746f58fecd6daa2c0b87e.png)

</div>
</div>


## 분할적 클러스터링 (Divisive Clustering)

- 한 군집에서 출발하여 서로 가장 거리가 먼 군집으로 분할해 나간다.
![](/assets/images/lecture-clustering/image_20241212_052010_c33a3675a7d64eac87b8ff3858c44f56.png)


## 정리

- 정해야 할 파라미터
    - Linkage 방법, 거리 metric
    - 최종 군집의 개수 (Dendrogram의 수평선 개수)
- 장점
    - 덴드로그램 제공
    - 군집의 개수를 초기에 설정하지 않아도 된다
- 단점
    - 두 군집을 연결하면 이를 취소할 수 없다
    - 거리 계산이 많아 계산 비용이 크다

# 밀도 기반 클러스터링 (Density-based Clustering)

- 구형 cluster를 가정하거나
- cluster 수를 안 정해도 됨
- 이상치 (Noise point)에 대한 해법
- 기하학적 모양의 군집도 잘 찾아낸다.

## DBSCAN

1. 각 점들은 세 가지 유형이 있다.
    1. 정해진 반지름 $$\varepsilon$$ 내에 이웃하는 점이 MinPts(정해준다)개 이상이면 **core point**
    1. core point의 반지름 $$\varepsilon$$ 안에 있으나, 이웃 점의 개수가 MinPts보다 적으면 **border point**
    1. 다른 건 다 **noise point**
1. 각 점에 이런 label을 부여한 뒤 다음을 거친다.
    1. core point 별로 독립된 군집을 형성하고, $$\varepsilon$$ 안에 여러 core point가 있으면 이를 연결하여 군집 형성
    1. 각 border point를 core point에 맞는 집단에 할당한다.
![](/assets/images/lecture-clustering/image_20241212_052013_602e6fa610224dd8ae7da1ddc9a78502.png)


### How?

- 반지름 $$\varepsilon$$과 MinPts는 어케 정함?
    - MinPts=k일 때, $$\varepsilon$$은 모든 데이터에 대한 k번째 가까운 이웃과의 거리를 계산한 plot에서 elbow로 선택한다.
- Cluster 개수는 안 정한다.
    - $$\varepsilon$$이 개수를 조절해준다.
    - $$\varepsilon$$**⬆️ → cluster⬇️**
    - $$\varepsilon$$**⬇️ → cluster⬆️**
![](/assets/images/lecture-clustering/image_20241212_052014_4c31acb79eff4a398794a83ec5d5c4c8.png)


### 정리

- 정해야 할 파라미터
    - $$\epsilon$$, MinPts
    - 거리 metric
- 장점
    - 군집 개수 안 정함
    - 다양한 모양의 군집 포착
    - Outlier/noise에 robust
- 단점
    - 밀도 차이가 큰 군집에 대해 잘 군집화 불가
    - 파라미터에 따라 결과 대동소

