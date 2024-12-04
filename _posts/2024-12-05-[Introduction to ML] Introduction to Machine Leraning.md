---
title: Introduction to Machine Learning
date: 2024-12-03 11:25:44 +09:00
author: Gyumin Choi
categories: 
  - Studies
tags: [LG Aimers]
paginate: true
---
### 서울대학교 김건희 교수

# Machine Learning(ML)

> A branch of artificial intelligence, concerned with the design and development of algorithms that allow computers to evolve behaviors based on empirical data
> 

- Herbert Simon’s def.

> Learning is any process by which a system improves performance from experience
> 
- Arthur Smuel’s definition

> Machine Learning is a field of study that gives computers the ability to learn without being explicitly programmed
> 
- Tom Mitchell’s def.

> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.
> 
> - T : classification, regression, detection…
> - P : error rate, accuracy, likelihood, margin…
> - E : data

<aside>
💡 Machine Learning improve task T, with respect to performance metric P, based on experience E.
- T : playing chess
- P : percentage of games won against an opponent
- E : playing practice games against itself

</aside>

![Traditional programming VS. Machine Learning](https://prod-files-secure.s3.us-west-2.amazonaws.com/5c6e92f3-b74f-4dac-a333-3c840d4281e7/7a94f5e1-2b26-4626-bc6d-f9caf4329b59/Untitled.png)

Traditional programming VS. Machine Learning

# Goal of ML: Generalization(일반화)

### Definition of learning

- A form of abstraction where common properties of specific instances are formulated as general concepts or claims.
- It extracts the essence of a concept based on its analysis of similarities from many discrete objects.

### Objective of learning

- Not to learn an exact representation of the training data itself
- To build a statistical model of the process that generates the data

# No Free Lunch Theorem for ML

- No machine learning algorithm is universally any better than any othe
- “NO ABSOLUTE BEST ALGORITHM”

# Types of Learning

## Supervised Learning

- Training data includes desired outputs

<aside>
💡 Given $(x_1, y_1), (x_2, y_2), …, (x_n, y_n)$, learn a function $f(x)$ to predict $y$ given $x$.

</aside>

- Classification: $y$ is categorical
- Regression: $y$ is continuous
- $x$ can be multi-dimensional

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5c6e92f3-b74f-4dac-a333-3c840d4281e7/845a4095-9367-4eb6-82c7-2f1e61ee49d4/Untitled.png)

## Unsupervised Learning

Training data does not include desired outputs

<aside>
💡 Given $x_1, x_2, …, x_n$, find a hidden structure(e.g., clusters)

</aside>

- Classification: $y$ is categorical
- Clustering, anomaly detection, density estimation, … e.g., Genomics: group individuals by genetic similarity

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5c6e92f3-b74f-4dac-a333-3c840d4281e7/125d1114-f1a7-4441-8946-16d8aaf207fd/Untitled.png)

## Semi-supervised learning

Some of training data includes desired outputs

- One of the bottlenecks of learning is the labeling of examples.
- Often done manually and time consuming
- Can we label only a small number of examples and make use of a large number of unlabeled examples to learn? Possible in many cases!

Two scenarios

- LU learning: Learning with a small set of Labeled examples and a large set of Unlabeled examples
- PU learning: Learning with Positive and Unlabeled examples(no labeled negative examples)

(LU와는 다르게 PU는 모든 클래스에 대한 몇 개의 레이블 데이터를 주는 게 아니라, 특정 클래스에 한해서만 레이블 데이터를 제공)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5c6e92f3-b74f-4dac-a333-3c840d4281e7/2c3bc8e6-b43b-45c7-8081-c788fb0057c9/Untitled.png)

Similar data points have similar labels; unlabeled data can help identify the boundary more accurately.

## Reinforcement Learning

No fixed dataset but an environment

Rewards from sequence of actions

- A feedback loop between the learning system and its environment
    - Does not experience a fixed dataset
    - No supervisor, but only rewards(Learning “fills in the details”)
    - Feedback could be delyed, not instantaneous
    - Agent’s actions affect the subsequent data it receives

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5c6e92f3-b74f-4dac-a333-3c840d4281e7/38811d80-416d-4009-9dd5-7ca34250ad9d/Untitled.png)