---
categories:
- 개발
date: '2024-12-05'
tags: []
title: Introduction to Machine Learning
toc: true
---

### 서울대학교 김건희 교수
# Machine Learning(ML)
 - Herbert Simon’s def.
 - Arthur Smuel’s definition
 - Tom Mitchell’s def.
 > 💡 Machine Learning improve task T, with respect to performance metric P, based on experience E.
- T : playing chess
- P : percentage of games won against an opponent
- E : playing practice games against itself
![Traditional programming VS. Machine Learning](/assets/images/introduction_to_machine_learning/image_20241205_084428.png)
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
> 💡 Given (x_1, y_1), (x_2, y_2), …, (x_n, y_n), learn a function f(x) to predict y given x.
- Classification: y is categorical
- Regression: y is continuous
- x can be multi-dimensional
![](/assets/images/introduction_to_machine_learning/image_20241205_084429.png)
## Unsupervised Learning
Training data does not include desired outputs> 💡 Given x_1, x_2, …, x_n, find a hidden structure(e.g., clusters)
- Classification: y is categorical
- Clustering, anomaly detection, density estimation, … e.g., Genomics: group individuals by genetic similarity
![](/assets/images/introduction_to_machine_learning/image_20241205_084430.png)
## Semi-supervised learning
Some of training data includes desired outputs- One of the bottlenecks of learning is the labeling of examples.
- Often done manually and time consuming
- Can we label only a small number of examples and make use of a large number of unlabeled examples to learn? Possible in many cases!
Two scenarios- LU learning: Learning with a small set of Labeled examples and a large set of Unlabeled examples
- PU learning: Learning with Positive and Unlabeled examples(no labeled negative examples)
(LU와는 다르게 PU는 모든 클래스에 대한 몇 개의 레이블 데이터를 주는 게 아니라, 특정 클래스에 한해서만 레이블 데이터를 제공)![](/assets/images/introduction_to_machine_learning/image_20241205_084431.png)
Similar data points have similar labels; unlabeled data can help identify the boundary more accurately.## Reinforcement Learning
No fixed dataset but an environmentRewards from sequence of actions- A feedback loop between the learning system and its environment
![](/assets/images/introduction_to_machine_learning/image_20241205_084432.png)