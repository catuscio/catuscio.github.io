---
categories:
- Studies
date: '2024-12-12'
tags:
- Lecture
title: '[Lecture] Support Vector Machine, SVM'
toc: true
---


# 마진과 서포트 벡터

- 데이터를 잘 분리하는 초평면을 찾는 게 목표.
- 분류를 실행하면 클래스를 나누는 **결정 경계(Decision Boundary)**가 생긴다.

### 용어 정리
- **서포트 벡터**
    - 결정 경계와 가장 가까운 점              

![](/assets/images/lecture-support_vector_machine_svm/image_20241212_050604_fa12cf88789c4c6cbffd5b9f1ac96824.png)


- **마진**
    - 결정 경계와 서포트 벡터 사이의 거리
    - 결정 경계에서 양쪽 서포트 벡터로의 거리는 같다.

![](/assets/images/lecture-support_vector_machine_svm/image_20241212_050606_5834a50341ca4b6ca86aabd0d63f29e0.png)


> 마진을 최대화(Margin Maximization)하는 결정 경계를 구하자.

---


# 수학적 모델링


## Hyperplane; 초평면

- n차원 공간에서 한 차원 낮은 n-1차원의 subspace.
- 예시
    - 2차원 공간 직선의 방정식
        - 법선벡터 $$w = [w_1, w_2]^T$$에 대해, 원점과의 거리가 $$d$$인 직선의 방정식은
$$w_1x_1 + w_2x_2 + d = 0 \ , \ \lVert w \rVert = 1$$

    - 3차원 공간 평면의 방정식
        - $$w = [w_1, w_2, w_3]^T$$
$$w_1x_1 + w_2x_2 + w_3x_3 + d = 0 \ , \ \lVert w \rVert = 1$$

> 따라서 초평면의 일반식은 다음과 같다.
$$w^Tx + b = 0$$

- $$w$$는 법선 벡터로 초평면의 방향을 결정
- $$b$$는 초평면과 원점과의 거리를 결정
- 초평면과 원점 사이의 거리 $$d$$는
    - $$d = \frac{|w^Tx + b|}{\lVert w \rVert}$$
![](/assets/images/lecture-support_vector_machine_svm/image_20241212_050614_8097f069f1aa4303a1158583295d4ebf.png)


